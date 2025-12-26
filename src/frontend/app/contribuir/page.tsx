import Link from 'next/link'

export default function ContribuirPage() {
  return (
    <main className="min-h-screen bg-[#F5F3EE]">
      {/* Header */}
      <header className="border-b border-[#d8d3c7] bg-[#F5F3EE]/95">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[#1F3D2B] text-[#F5F3EE] text-lg font-semibold">RB</div>
            <div className="leading-tight">
              <p className="font-serif text-xl text-[#1C1C1C]">Retratos de Bonito</p>
              <p className="text-sm text-[#6B6B6B]">Museu Digital Comunitário</p>
            </div>
          </div>
          <nav className="flex items-center gap-6 text-sm font-medium">
            <a href="/" className="text-[#1C1C1C] transition hover:text-[#1F3D2B]">Início</a>
            <a href="/search.html" className="text-[#1C1C1C] transition hover:text-[#1F3D2B]">Buscar</a>
            <a href="/expo" className="text-[#1C1C1C] transition hover:text-[#1F3D2B]">Modo Exposição</a>
          </nav>
        </div>
      </header>

      {/* Conteúdo */}
      <div className="mx-auto max-w-3xl px-6 py-16 space-y-12">
        {/* Intro */}
        <section className="space-y-6">
          <h1 className="font-serif text-5xl text-[#1C1C1C]">
            Compartilhe uma memória
          </h1>
          <p className="text-lg text-[#6B6B6B] leading-relaxed max-w-2xl">
            Você pode enviar uma fotografia antiga ou recente para compor o acervo cultural de Bonito. 
            Cada imagem é uma parte da história coletiva que queremos preservar.
          </p>
        </section>

        {/* O que acontece */}
        <section className="space-y-4">
          <h2 className="font-serif text-2xl text-[#1C1C1C]">Como funciona</h2>
          <div className="space-y-3">
            <div className="flex gap-4">
              <div className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-[#1F3D2B] text-white font-medium text-sm">1</div>
              <div>
                <p className="font-medium text-[#1C1C1C]">Você envia a fotografia</p>
                <p className="text-sm text-[#6B6B6B]">E conta um pouco sobre ela</p>
              </div>
            </div>
            <div className="flex gap-4">
              <div className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-[#1F3D2B] text-white font-medium text-sm">2</div>
              <div>
                <p className="font-medium text-[#1C1C1C]">Passamos por curadoria</p>
                <p className="text-sm text-[#6B6B6B]">Validamos e tratamos a imagem com cuidado</p>
              </div>
            </div>
            <div className="flex gap-4">
              <div className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-[#1F3D2B] text-white font-medium text-sm">3</div>
              <div>
                <p className="font-medium text-[#1C1C1C]">Publicamos no arquivo</p>
                <p className="text-sm text-[#6B6B6B]">E sua imagem faz parte da memória de Bonito</p>
              </div>
            </div>
          </div>
        </section>

        {/* Importância */}
        <section className="bg-white border border-[#e7e3d7] rounded-xl p-8 space-y-4">
          <h2 className="font-serif text-xl text-[#1C1C1C]">Por que isso importa</h2>
          <p className="text-[#6B6B6B] leading-relaxed">
            Fotografias antigas são janelas para o passado. Cada imagem que você compartilha ajuda escolas a ensinar história, 
            pesquisadores a entender transformações urbanas, e famílias a reconhecer seus próprios momentos.
          </p>
          <p className="text-[#6B6B6B] leading-relaxed">
            Sua contribuição não desaparece. Fica aqui, preservada, para gerações futuras.
          </p>
        </section>

        {/* CTA */}
        <section className="flex gap-4">
          <Link
            href="/contribuir/foto"
            className="inline-flex items-center gap-2 bg-[#1F3D2B] text-[#F5F3EE] px-8 py-4 rounded-lg font-medium transition hover:bg-[#2d5a3d] hover:-translate-y-0.5"
          >
            Enviar uma fotografia
          </Link>
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-[#1C1C1C] px-8 py-4 rounded-lg font-medium transition hover:text-[#1F3D2B]"
          >
            Voltar ao arquivo
          </Link>
        </section>
      </div>
    </main>
  )
}
