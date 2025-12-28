/**
 * Contexto de autenticação para gerenciar sessão do usuário.
 */

'use client'

import { createContext, useContext, useState, useEffect, ReactNode } from 'react'

const API_BASE = process.env.NEXT_PUBLIC_API_URL || ''

// Tipos
export interface User {
  id: number
  name: string
  email: string
  role_name: string
  is_active: boolean
  created_at: string
  total_photos: number
  photos_validated: number
  photos_pending: number
}

interface AuthContextType {
  user: User | null
  token: string | null
  isLoading: boolean
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>
  register: (name: string, email: string, password: string) => Promise<{ success: boolean; error?: string }>
  logout: () => void
  refreshUser: () => Promise<void>
}

// Contexto
const AuthContext = createContext<AuthContextType | undefined>(undefined)

// Chaves de storage
const TOKEN_KEY = 'retratos_token'

// Provider
export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [token, setToken] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  // Carregar token do localStorage na inicialização
  useEffect(() => {
    const savedToken = localStorage.getItem(TOKEN_KEY)
    if (savedToken) {
      setToken(savedToken)
      fetchUser(savedToken)
    } else {
      setIsLoading(false)
    }
  }, [])

  // Buscar dados do usuário
  const fetchUser = async (accessToken: string) => {
    try {
      const res = await fetch(`${API_BASE}/auth/me`, {
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      })
      
      if (res.ok) {
        const userData = await res.json()
        setUser(userData)
        setToken(accessToken)
      } else {
        // Token inválido, limpar
        localStorage.removeItem(TOKEN_KEY)
        setToken(null)
        setUser(null)
      }
    } catch (error) {
      console.error('Erro ao buscar usuário:', error)
      localStorage.removeItem(TOKEN_KEY)
      setToken(null)
      setUser(null)
    } finally {
      setIsLoading(false)
    }
  }

  // Login
  const login = async (email: string, password: string) => {
    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      })

      if (res.ok) {
        const data = await res.json()
        localStorage.setItem(TOKEN_KEY, data.access_token)
        setToken(data.access_token)
        await fetchUser(data.access_token)
        return { success: true }
      } else {
        const error = await res.json()
        return { success: false, error: error.detail || 'Erro ao fazer login' }
      }
    } catch (error) {
      return { success: false, error: 'Erro de conexão. Tente novamente.' }
    }
  }

  // Registro
  const register = async (name: string, email: string, password: string) => {
    try {
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, password })
      })

      if (res.ok) {
        // Após registro, fazer login automaticamente
        return await login(email, password)
      } else {
        const error = await res.json()
        return { success: false, error: error.detail || 'Erro ao criar conta' }
      }
    } catch (error) {
      return { success: false, error: 'Erro de conexão. Tente novamente.' }
    }
  }

  // Logout
  const logout = () => {
    localStorage.removeItem(TOKEN_KEY)
    setToken(null)
    setUser(null)
  }

  // Atualizar dados do usuário
  const refreshUser = async () => {
    if (token) {
      await fetchUser(token)
    }
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isLoading,
        isAuthenticated: !!user,
        login,
        register,
        logout,
        refreshUser
      }}
    >
      {children}
    </AuthContext.Provider>
  )
}

// Hook
export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth deve ser usado dentro de um AuthProvider')
  }
  return context
}

// Função auxiliar para fazer requisições autenticadas
export function useAuthenticatedFetch() {
  const { token } = useAuth()

  return async (url: string, options: RequestInit = {}) => {
    const headers = {
      ...options.headers,
      ...(token ? { 'Authorization': `Bearer ${token}` } : {})
    }

    return fetch(`${API_BASE}${url}`, {
      ...options,
      headers
    })
  }
}
