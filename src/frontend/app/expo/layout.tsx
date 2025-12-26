import { ReactNode } from 'react'

export const metadata = {
  title: 'Modo Exposição — Retratos de Bonito',
  description: 'Visualização imersiva do acervo histórico de Bonito em tela cheia'
}

export default function ExpoLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="pt-BR">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className="overflow-hidden">
        {children}
      </body>
    </html>
  )
}
