'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth'

interface ProtectedRouteProps {
  children: React.ReactNode
  requiredRoles?: string[]
}

/**
 * Componente para proteger rotas que requerem autenticação.
 * 
 * Uso básico (qualquer usuário logado):
 * <ProtectedRoute>
 *   <MinhaPageProtegida />
 * </ProtectedRoute>
 * 
 * Com papéis específicos:
 * <ProtectedRoute requiredRoles={['curator', 'admin']}>
 *   <PaginaDeCuradoria />
 * </ProtectedRoute>
 */
export default function ProtectedRoute({ children, requiredRoles }: ProtectedRouteProps) {
  const { user, isAuthenticated, isLoading } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (!isLoading) {
      if (!isAuthenticated) {
        router.push('/login')
        return
      }

      if (requiredRoles && requiredRoles.length > 0) {
        const hasRequiredRole = user && requiredRoles.includes(user.role_name)
        if (!hasRequiredRole) {
          router.push('/dashboard?error=acesso_negado')
        }
      }
    }
  }, [isLoading, isAuthenticated, user, requiredRoles, router])

  // Loading
  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-emerald-600"></div>
      </div>
    )
  }

  // Não autenticado
  if (!isAuthenticated) {
    return null
  }

  // Verificar papel se necessário
  if (requiredRoles && requiredRoles.length > 0) {
    const hasRequiredRole = user && requiredRoles.includes(user.role_name)
    if (!hasRequiredRole) {
      return (
        <div className="min-h-screen flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-2xl font-bold text-gray-900 mb-2">Acesso Restrito</h1>
            <p className="text-gray-600">Você não tem permissão para acessar esta página.</p>
          </div>
        </div>
      )
    }
  }

  return <>{children}</>
}
