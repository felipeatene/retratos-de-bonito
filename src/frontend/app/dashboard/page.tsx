'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { useAuth } from '@/lib/auth'

export default function DashboardPage() {
  const { user, isAuthenticated, isLoading } = useAuth()
  const router = useRouter()

  // Redirecionar se não estiver logado
  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      router.push('/login')
    }
  }, [isLoading, isAuthenticated, router])

  if (isLoading) {
    return (
      <main className="max-w-6xl mx-auto p-6">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded w-1/3 mb-4"></div>
          <div className="h-4 bg-gray-200 rounded w-1/2 mb-8"></div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="h-32 bg-gray-200 rounded-xl"></div>
            <div className="h-32 bg-gray-200 rounded-xl"></div>
            <div className="h-32 bg-gray-200 rounded-xl"></div>
          </div>
        </div>
      </main>
    )
  }

  if (!user) {
    return null
  }

  // Determinar saudação baseada na hora
  const hour = new Date().getHours()
  let greeting = 'Bom dia'
  if (hour >= 12 && hour < 18) greeting = 'Boa tarde'
  else if (hour >= 18) greeting = 'Boa noite'

  return (
    <main className="max-w-6xl mx-auto p-6">
      {/* Cabeçalho */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          {greeting}, {user.name.split(' ')[0]}!
        </h1>
        <p className="text-gray-600">
          Obrigado por contribuir com a memória de Bonito.
        </p>
      </div>

      {/* Cards de Estatísticas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white rounded-xl shadow-sm border p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500 mb-1">Total de fotos</p>
              <p className="text-3xl font-bold text-gray-900">{user.total_photos}</p>
            </div>
            <div className="text-4xl">📷</div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500 mb-1">Fotos validadas</p>
              <p className="text-3xl font-bold text-emerald-600">{user.photos_validated}</p>
            </div>
            <div className="text-4xl">✅</div>
          </div>
          <p className="text-xs text-gray-400 mt-2">Já estão no acervo público</p>
        </div>

        <div className="bg-white rounded-xl shadow-sm border p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500 mb-1">Em análise</p>
              <p className="text-3xl font-bold text-amber-600">{user.photos_pending}</p>
            </div>
            <div className="text-4xl">⏳</div>
          </div>
          <p className="text-xs text-gray-400 mt-2">Aguardando curadoria</p>
        </div>
      </div>

      {/* Ações Rápidas */}
      <div className="bg-white rounded-xl shadow-sm border p-6 mb-8">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">O que você gostaria de fazer?</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <Link 
            href="/contribuir"
            className="flex items-center gap-3 p-4 rounded-lg border-2 border-dashed border-gray-200 hover:border-emerald-500 hover:bg-emerald-50 transition-colors"
          >
            <span className="text-2xl">📤</span>
            <div>
              <p className="font-medium text-gray-900">Enviar fotos</p>
              <p className="text-xs text-gray-500">Contribuir com novas imagens</p>
            </div>
          </Link>

          <Link 
            href="/dashboard/minhas-fotos"
            className="flex items-center gap-3 p-4 rounded-lg border-2 border-dashed border-gray-200 hover:border-emerald-500 hover:bg-emerald-50 transition-colors"
          >
            <span className="text-2xl">🖼️</span>
            <div>
              <p className="font-medium text-gray-900">Minhas fotos</p>
              <p className="text-xs text-gray-500">Ver suas contribuições</p>
            </div>
          </Link>

          <Link 
            href="/search"
            className="flex items-center gap-3 p-4 rounded-lg border-2 border-dashed border-gray-200 hover:border-emerald-500 hover:bg-emerald-50 transition-colors"
          >
            <span className="text-2xl">🔍</span>
            <div>
              <p className="font-medium text-gray-900">Explorar acervo</p>
              <p className="text-xs text-gray-500">Descobrir memórias</p>
            </div>
          </Link>

          <Link 
            href="/expo"
            className="flex items-center gap-3 p-4 rounded-lg border-2 border-dashed border-gray-200 hover:border-emerald-500 hover:bg-emerald-50 transition-colors"
          >
            <span className="text-2xl">🎬</span>
            <div>
              <p className="font-medium text-gray-900">Modo exposição</p>
              <p className="text-xs text-gray-500">Apresentação em tela cheia</p>
            </div>
          </Link>
        </div>
      </div>

      {/* Informações do Perfil */}
      <div className="bg-white rounded-xl shadow-sm border p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Seu perfil</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <p className="text-sm text-gray-500">Nome</p>
            <p className="text-gray-900">{user.name}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Email</p>
            <p className="text-gray-900">{user.email}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Tipo de conta</p>
            <p className="text-gray-900">
              {user.role_name === 'admin' && '👑 Administrador'}
              {user.role_name === 'curator' && '🎨 Curador'}
              {user.role_name === 'user' && '🙋 Contribuidor'}
            </p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Membro desde</p>
            <p className="text-gray-900">
              {new Date(user.created_at).toLocaleDateString('pt-BR', {
                day: '2-digit',
                month: 'long',
                year: 'numeric'
              })}
            </p>
          </div>
        </div>
      </div>

      {/* Área de Curadoria (apenas para curadores e admins) */}
      {(user.role_name === 'curator' || user.role_name === 'admin') && (
        <div className="mt-8 bg-amber-50 rounded-xl border border-amber-200 p-6">
          <h2 className="text-lg font-semibold text-amber-900 mb-4">
            🎨 Área de Curadoria
          </h2>
          <p className="text-amber-800 mb-4">
            Você tem permissões especiais para ajudar na organização do acervo.
          </p>
          <div className="flex gap-4">
            <Link 
              href="/curadoria"
              className="bg-amber-600 text-white px-4 py-2 rounded-lg hover:bg-amber-700 transition-colors"
            >
              Acessar Curadoria
            </Link>
          </div>
        </div>
      )}
    </main>
  )
}
