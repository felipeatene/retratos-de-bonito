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
  status: 'bruta' | 'catalogada' | 'validada'
  visibility: string
  created_at: string
}

export default function MinhasFotosPage() {
  const { isAuthenticated, isLoading: authLoading } = useAuth()
  const router = useRouter()
  const authFetch = useAuthenticatedFetch()
  
  const [photos, setPhotos] = useState<Photo[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [filter, setFilter] = useState<string>('all')

  // Redirecionar se não estiver logado
  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      router.push('/login')
    }
  }, [authLoading, isAuthenticated, router])

  // Carregar fotos
  useEffect(() => {
    if (isAuthenticated) {
      loadPhotos()
    }
  }, [isAuthenticated])

  const loadPhotos = async () => {
    try {
      const res = await authFetch('/photos/my')
      if (res.ok) {
        const data = await res.json()
        setPhotos(data)
      }
    } catch (error) {
      console.error('Erro ao carregar fotos:', error)
    } finally {
      setIsLoading(false)
    }
  }

  // Filtrar fotos
  const filteredPhotos = photos.filter(photo => {
    if (filter === 'all') return true
    return photo.status === filter
  })

  // Status badge
  const getStatusBadge = (status: string) => {
    switch (status) {
      case 'validada':
        return <span className="px-2 py-1 text-xs rounded-full bg-emerald-100 text-emerald-800">✅ Validada</span>
      case 'catalogada':
        return <span className="px-2 py-1 text-xs rounded-full bg-blue-100 text-blue-800">📋 Catalogada</span>
      case 'bruta':
      default:
        return <span className="px-2 py-1 text-xs rounded-full bg-amber-100 text-amber-800">⏳ Em análise</span>
    }
  }

  if (authLoading || isLoading) {
    return (
      <main className="max-w-6xl mx-auto p-6">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded w-1/3 mb-8"></div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map(i => (
              <div key={i} className="h-64 bg-gray-200 rounded-xl"></div>
            ))}
          </div>
        </div>
      </main>
    )
  }

  return (
    <main className="max-w-6xl mx-auto p-6">
      {/* Cabeçalho */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <Link href="/dashboard" className="text-sm text-gray-500 hover:text-gray-700 mb-2 inline-block">
            ← Voltar ao painel
          </Link>
          <h1 className="text-3xl font-bold text-gray-900">Minhas Fotos</h1>
          <p className="text-gray-600 mt-1">
            {photos.length} {photos.length === 1 ? 'foto enviada' : 'fotos enviadas'}
          </p>
        </div>
        <Link 
          href="/contribuir"
          className="bg-emerald-600 text-white px-4 py-2 rounded-lg hover:bg-emerald-700 transition-colors"
        >
          + Enviar nova foto
        </Link>
      </div>

      {/* Filtros */}
      <div className="flex gap-2 mb-6">
        <button
          onClick={() => setFilter('all')}
          className={`px-4 py-2 rounded-lg text-sm transition-colors ${
            filter === 'all' 
              ? 'bg-gray-900 text-white' 
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          Todas ({photos.length})
        </button>
        <button
          onClick={() => setFilter('bruta')}
          className={`px-4 py-2 rounded-lg text-sm transition-colors ${
            filter === 'bruta' 
              ? 'bg-amber-600 text-white' 
              : 'bg-amber-50 text-amber-700 hover:bg-amber-100'
          }`}
        >
          Em análise ({photos.filter(p => p.status === 'bruta').length})
        </button>
        <button
          onClick={() => setFilter('catalogada')}
          className={`px-4 py-2 rounded-lg text-sm transition-colors ${
            filter === 'catalogada' 
              ? 'bg-blue-600 text-white' 
              : 'bg-blue-50 text-blue-700 hover:bg-blue-100'
          }`}
        >
          Catalogadas ({photos.filter(p => p.status === 'catalogada').length})
        </button>
        <button
          onClick={() => setFilter('validada')}
          className={`px-4 py-2 rounded-lg text-sm transition-colors ${
            filter === 'validada' 
              ? 'bg-emerald-600 text-white' 
              : 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100'
          }`}
        >
          Validadas ({photos.filter(p => p.status === 'validada').length})
        </button>
      </div>

      {/* Lista de Fotos */}
      {filteredPhotos.length === 0 ? (
        <div className="text-center py-16 bg-gray-50 rounded-xl">
          {photos.length === 0 ? (
            <>
              <p className="text-gray-500 text-lg mb-4">Você ainda não enviou nenhuma foto</p>
              <p className="text-gray-400 mb-6">
                Contribua com a memória de Bonito enviando suas fotografias históricas.
              </p>
              <Link 
                href="/contribuir"
                className="inline-block bg-emerald-600 text-white px-6 py-3 rounded-lg hover:bg-emerald-700 transition-colors"
              >
                Enviar minha primeira foto
              </Link>
            </>
          ) : (
            <p className="text-gray-500">Nenhuma foto encontrada com esse filtro</p>
          )}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredPhotos.map(photo => (
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
                <div className="flex items-center justify-between mb-2">
                  {getStatusBadge(photo.status)}
                  <span className="text-xs text-gray-400">
                    {new Date(photo.created_at).toLocaleDateString('pt-BR')}
                  </span>
                </div>
                {photo.description && (
                  <p className="text-sm text-gray-600 line-clamp-2">{photo.description}</p>
                )}
                {photo.status === 'validada' && (
                  <Link 
                    href={`/photos/${photo.id}`}
                    className="text-sm text-emerald-600 hover:text-emerald-700 mt-2 inline-block"
                  >
                    Ver no acervo →
                  </Link>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Legenda de Status */}
      <div className="mt-8 p-4 bg-gray-50 rounded-lg">
        <h3 className="font-medium text-gray-900 mb-3">Entenda os status:</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
          <div className="flex items-start gap-2">
            <span className="text-amber-600">⏳</span>
            <div>
              <p className="font-medium text-gray-700">Em análise</p>
              <p className="text-gray-500">Aguardando revisão da equipe de curadoria</p>
            </div>
          </div>
          <div className="flex items-start gap-2">
            <span className="text-blue-600">📋</span>
            <div>
              <p className="font-medium text-gray-700">Catalogada</p>
              <p className="text-gray-500">Informações básicas foram preenchidas</p>
            </div>
          </div>
          <div className="flex items-start gap-2">
            <span className="text-emerald-600">✅</span>
            <div>
              <p className="font-medium text-gray-700">Validada</p>
              <p className="text-gray-500">Disponível no acervo público</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
