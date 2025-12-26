import Link from 'next/link'

export default function ObrigadoPage() {
  return (
    <main className="min-h-screen bg-[#F5F3EE]">
      {/* Header */}
      <header className="border-b border-[#d8d3c7] bg-[#F5F3EE]/95">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
          <Link href="/" className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[#1F3D2B] text-[#F5F3EE] text-lg font-semibold">RB</div>
            <div className="leading-tight">
              <p className="font-serif text-xl text-[#1C1C1C]">Retratos de Bonito</p>
              <p className="text-sm text-[#6B6B6B]">Museu Digital Comunitário</p>
            </div>
          </Link>
        </div>
      </header>

      {/* Conteúdo */}
      <div className="mx-auto max-w-2xl px-6 py-20 text-center space-y-8">
        <div className="space-y-4">
          <div className="text-6xl">✨</div>
          <h1 className="font-serif text-5xl text-[#1C1C1C]">
            Obrigado por contribuir
          </h1>
        </div>

        <div className="space-y-4 max-w-xl mx-auto">
          <p className="text-lg text-[#6B6B6B] leading-relaxed">
            Sua fotografia foi recebida com cuidado.
          </p>
          <p className="text-[#6B6B6B] leading-relaxed">
            Ela passará por curadoria e validação. Em breve, poderá fazer parte do acervo público de Retratos de Bonito, 
            ajudando gerações futuras a entender e se conectar com a história da cidade.
          </p>
        </div>

        <div className="bg-white border border-[#e7e3d7] rounded-xl p-8 space-y-4 text-left">
          <h2 className="font-serif text-xl text-[#1C1C1C]">O que acontece agora?</h2>
          <ul className="space-y-3 text-sm text-[#6B6B6B]">
            <li className="flex gap-3">
              <span className="flex-shrink-0 text-[#1F3D2B] font-semibold">✓</span>
              <span>Sua imagem é armazenada com segurança em nossos servidores</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-shrink-0 text-[#1F3D2B] font-semibold">✓</span>
              <span>Um curador revisa a foto e suas informações</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-shrink-0 text-[#1F3D2B] font-semibold">✓</span>
              <span>A imagem é tratada (tamanho, qualidade, metadados)</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-shrink-0 text-[#1F3D2B] font-semibold">✓</span>
              <span>Ela entra no acervo público do arquivo</span>
            </li>
          </ul>
        </div>

        <div className="space-y-4">
          <p className="text-sm text-[#6B6B6B]">
            Quer saber mais sobre como o arquivo funciona?
          </p>
          <div className="flex gap-3 justify-center">
            <Link
              href="/"
              className="inline-flex items-center gap-2 bg-[#1F3D2B] text-[#F5F3EE] px-8 py-4 rounded-lg font-medium transition hover:bg-[#2d5a3d] hover:-translate-y-0.5"
            >
              Explorar o acervo
            </Link>
            <Link
              href="/contribuir"
              className="inline-flex items-center gap-2 text-[#1C1C1C] px-8 py-4 rounded-lg font-medium transition hover:text-[#1F3D2B]"
            >
              Enviar outra foto
            </Link>
          </div>
        </div>

        <div className="border-t border-[#d8d3c7] pt-8">
          <p className="text-xs text-[#6B6B6B]">
            Dúvidas? Entre em contato conosco pelo email ou redes sociais.
          </p>
        </div>
      </div>
    </main>
  )
}
