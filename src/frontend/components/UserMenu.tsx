'use client'

import Link from 'next/link'
import { useAuth } from '@/lib/auth'

export default function UserMenu() {
  const { user, isAuthenticated, isLoading, logout } = useAuth()

  if (isLoading) {
    return (
      <div className="text-sm text-gray-400">
        Carregando...
      </div>
    )
  }

  if (!isAuthenticated) {
    return (
      <div className="flex items-center space-x-3">
        <Link 
          href="/login" 
          className="text-sm text-gray-600 hover:text-gray-900"
        >
          Entrar
        </Link>
        <Link 
          href="/register" 
          className="text-sm bg-emerald-600 text-white px-4 py-2 rounded-lg hover:bg-emerald-700 transition-colors"
        >
          Criar Conta
        </Link>
      </div>
    )
  }

  return (
    <div className="flex items-center space-x-4">
      <Link 
        href="/dashboard" 
        className="text-sm text-gray-600 hover:text-gray-900"
      >
        {user?.name}
      </Link>
      {(user?.role_name === 'curator' || user?.role_name === 'admin') && (
        <Link 
          href="/curadoria" 
          className="text-sm text-amber-600 hover:text-amber-800"
        >
          Curadoria
        </Link>
      )}
      <button
        onClick={logout}
        className="text-sm text-gray-500 hover:text-gray-700"
      >
        Sair
      </button>
    </div>
  )
}
