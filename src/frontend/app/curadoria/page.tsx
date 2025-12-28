'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { useAuth, useAuthenticatedFetch } from '@/lib/auth'

interface Photo {
  id: number
  file_name: string
  file_path: string
  description: string | null
  status: string
  visibility: string
  created_at: string
}

export default function CuradoriaPage() {
  const { user, isAuthenticated, isLoading: authLoading } = useAuth()
  const router = useRouter()
  const authFetch = useAuthenticatedFetch()
  
  const [photos, setPhotos] = useState<Photo[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [selectedPhoto, setSelectedPhoto] = useState<Photo | null>(null)
  const [curatingId, setCuratingId] = useState<number | null>(null)

  // Verificar permissão
  useEffect(() => {
    if (!authLoading) {
      if (!isAuthenticated) {
        router.push('/login')
        return
      }
      if (user && !['curator', 'admin'].includes(user.role_name)) {
        router.push('/dashboard?error=acesso_negado')
      }
    }
  }, [authLoading, isAuthenticated, user, router])

  // Carregar fotos pendentes
  useEffect(() => {
    if (isAuthenticated && user && ['curator', 'admin'].includes(user.role_name)) {
      loadPendingPhotos()
    }
  }, [isAuthenticated, user])

  const loadPendingPhotos = async () => {
    try {
      // Usando endpoint público que filtra por status
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || ''}/public/search?status=bruta&limit=50`)
      if (res.ok) {
        const data = await res.json()
        setPhotos(data.photos || [])
      }
    } catch (error) {
      console.error('Erro ao carregar fotos:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const handleCurate = async (photoId: number, newStatus: string, newVisibility: string) => {
    setCuratingId(photoId)
    try {
      const res = await authFetch(`/photos/${photoId}/curate`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          status: newStatus, 
          visibility: newVisibility 
        })
      })
      
      if (res.ok) {
        // Remover da lista ou atualizar
        setPhotos(photos.filter(p => p.id !== photoId))
        setSelectedPhoto(null)
      } else {
        const error = await res.json()
        alert(error.detail || 'Erro ao curar foto')
      }
    } catch (error) {
      alert('Erro de conexão')
    } finally {
      setCuratingId(null)
    }
  }

  if (authLoading || isLoading) {
    return (
      <main className="max-w-6xl mx-auto p-6">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded w-1/3 mb-8"></div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map(i => (
              <div key={i} className="h-64 bg-gray-200 rounded-xl"></div>
            ))}
          </div>
        </div>
      </main>
    )
  }

  if (!user || !['curator', 'admin'].includes(user.role_name)) {
    return null
  }

  return (
    <main className="max-w-6xl mx-auto p-6">
      {/* Cabeçalho */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <Link href="/dashboard" className="text-sm text-gray-500 hover:text-gray-700 mb-2 inline-block">
            ← Voltar ao painel
          </Link>
          <h1 className="text-3xl font-bold text-gray-900">Curadoria</h1>
          <p className="text-gray-600 mt-1">
            {photos.length} {photos.length === 1 ? 'foto aguardando' : 'fotos aguardando'} revisão
          </p>
        </div>
      </div>

      {/* Lista de fotos */}
      {photos.length === 0 ? (
        <div className="text-center py-16 bg-gray-50 rounded-xl">
          <p className="text-gray-500 text-lg mb-4">🎉 Nenhuma foto pendente!</p>
          <p className="text-gray-400">Todas as fotos foram revisadas.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {photos.map(photo => (
            <div key={photo.id} className="bg-white rounded-xl shadow-sm border overflow-hidden">
              <div className="aspect-video bg-gray-100 relative">
                <img
                  src={`${process.env.NEXT_PUBLIC_API_URL || ''}/storage/${photo.file_path}`}
                  alt={photo.description || 'Foto'}
                  className="w-full h-full object-cover"
                  onError={(e) => {
                    e.currentTarget.src = '/placeholder.svg'
                  }}
                />
              </div>
              <div className="p-4">
                <p className="text-sm text-gray-600 mb-3 line-clamp-2">
                  {photo.description || 'Sem descrição'}
                </p>
                <div className="flex gap-2">
                  <button
                    onClick={() => handleCurate(photo.id, 'validada', 'publica')}
                    disabled={curatingId === photo.id}
                    className="flex-1 bg-emerald-600 text-white text-sm py-2 px-3 rounded-lg hover:bg-emerald-700 disabled:opacity-50"
                  >
                    ✅ Aprovar
                  </button>
                  <button
                    onClick={() => handleCurate(photo.id, 'catalogada', 'restrita')}
                    disabled={curatingId === photo.id}
                    className="flex-1 bg-amber-600 text-white text-sm py-2 px-3 rounded-lg hover:bg-amber-700 disabled:opacity-50"
                  >
                    📋 Catalogar
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  )
}
