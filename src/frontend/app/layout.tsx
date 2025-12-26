import './globals.css'
import Header from '@/components/Header'

export const metadata = {
  title: 'Retratos de Bonito',
  description: 'Arquivo comunitário de fotografias de Bonito-MS'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>
        <Header />
        <div className="container mx-auto px-4 py-6">{children}</div>
      </body>
    </html>
  )
}
