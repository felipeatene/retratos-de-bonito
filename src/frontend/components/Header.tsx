import Link from 'next/link'

export default function Header() {
  return (
    <header className="bg-white border-b">
      <div className="container mx-auto px-4 py-4 flex items-center justify-between">
        <Link href="/" className="text-xl font-bold">Retratos de Bonito</Link>
        <nav className="space-x-4">
          <Link href="/search" className="text-sm text-gray-600">Buscar</Link>
        </nav>
      </div>
    </header>
  )
}
