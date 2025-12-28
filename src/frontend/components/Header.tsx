'use client'

import Link from 'next/link'
import UserMenu from './UserMenu'

export default function Header() {
  return (
    <header className="bg-white border-b">
      <div className="container mx-auto px-4 py-4 flex items-center justify-between">
        <Link href="/" className="text-xl font-bold">Retratos de Bonito</Link>
        <nav className="flex items-center space-x-4">
          <Link href="/search" className="text-sm text-gray-600 hover:text-gray-900">Buscar</Link>
          <Link href="/expo" className="text-sm text-gray-600 hover:text-gray-900">Modo Exposição</Link>
          <Link href="/contribuir" className="text-sm text-gray-600 hover:text-gray-900">Contribuir</Link>
          <div className="border-l pl-4 ml-2">
            <UserMenu />
          </div>
        </nav>
      </div>
    </header>
  )
}
