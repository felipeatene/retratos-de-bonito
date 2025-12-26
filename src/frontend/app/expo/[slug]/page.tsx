import { getExposicaoBySlug, exposicoes } from '@/config/exposicoes'

// Gerar routes estáticas
export async function generateStaticParams() {
  return Object.values(exposicoes).map(expo => ({
    slug: expo.slug
  }))
}

export async function generateMetadata({ params }: any) {
  const expo = getExposicaoBySlug(params.slug)

  if (!expo) {
    return {
      title: 'Exposição não encontrada',
      description: 'A exposição que você procura não existe.'
    }
  }

  return {
    title: `${expo.title} — Retratos de Bonito`,
    description: expo.description,
    openGraph: {
      title: expo.title,
      description: expo.description,
      type: 'website'
    }
  }
}

async function getExposicaoData(apiEndpoint: string) {
  try {
    const apiBase = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
    const res = await fetch(`${apiBase}${apiEndpoint}`, { 
      next: { revalidate: 3600 } 
    })
    return res.json()
  } catch (error) {
    console.error('Erro ao carregar dados da exposição:', error)
    return null
  }
}

export default async function ExpoThemePage({ params }: any) {
  const expo = getExposicaoBySlug(params.slug)

  if (!expo) {
    return (
      <div className="max-w-6xl mx-auto px-6 py-12 text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">Exposição não encontrada</h1>
        <p className="text-gray-600 mb-8">A exposição que você procura não existe ou foi removida.</p>
        <a href="/" className="text-blue-600 hover:underline">← Voltar à página inicial</a>
      </div>
    )
  }

  const data = await getExposicaoData(expo.apiEndpoint)

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
      <div className="mx-auto max-w-6xl px-6 py-16">
        {/* Intro da exposição */}
        <section className="mb-16 space-y-4">
          <p className="text-sm uppercase tracking-[0.18em] text-[#6B6B6B]">Exposição temática</p>
          <h1 className="font-serif text-5xl text-[#1C1C1C]">{expo.title}</h1>
          <p className="max-w-3xl text-lg text-[#6B6B6B]">{expo.description}</p>
        </section>

        {/* Dados carregados (placeholder para desenvolvimento) */}
        {data ? (
          <section>
            {/* Timeline format (default) */}
            {Array.isArray(data) && data.length > 0 && data[0].decade !== undefined && (
              <div className="space-y-12">
                {data.map((period: any) => (
                  <div key={period.decade} className="space-y-6">
                    <div className="space-y-2 border-b border-[#e7e3d7] pb-4">
                      <p className="text-xs uppercase tracking-[0.2em] text-[#6B6B6B]">Período</p>
                      <h2 className="font-serif text-3xl text-[#1C1C1C]">Década de {period.decade}</h2>
                    </div>

                    <div className="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-4">
                      {period.photos.map((photo: any) => (
                        <a
                          key={photo.photo_id}
                          href={`/photos/${photo.photo_id}`}
                          className="group block"
                        >
                          <div className="relative aspect-[3/4] overflow-hidden rounded-lg border border-[#e7e3d7] bg-white shadow-sm transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                            <img
                              src={`${process.env.NEXT_PUBLIC_API_URL}/${encodeURIComponent(photo.file_name)}`}
                              alt={photo.description || 'Foto'}
                              className="h-full w-full object-cover transition duration-300 group-hover:scale-105"
                            />
                          </div>
                          <p className="mt-2 text-sm text-[#6B6B6B] line-clamp-2">
                            {photo.description || 'Sem descrição'}
                          </p>
                          {photo.original_date && (
                            <p className="mt-1 text-xs text-[#6B6B6B]">{photo.original_date}</p>
                          )}
                        </a>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Grid format (search results) */}
            {Array.isArray(data) && data.length > 0 && !data[0].decade && (
              <div className="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-4">
                {data.map((photo: any) => (
                  <a
                    key={photo.photo_id}
                    href={`/photos/${photo.photo_id}`}
                    className="group block"
                  >
                    <div className="relative aspect-[3/4] overflow-hidden rounded-lg border border-[#e7e3d7] bg-white shadow-sm transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                      <img
                        src={`${process.env.NEXT_PUBLIC_API_URL}/${encodeURIComponent(photo.file_name)}`}
                        alt={photo.description || 'Foto'}
                        className="h-full w-full object-cover transition duration-300 group-hover:scale-105"
                      />
                    </div>
                    <p className="mt-2 text-sm text-[#6B6B6B] line-clamp-2">
                      {photo.description || 'Sem descrição'}
                    </p>
                  </a>
                ))}
              </div>
            )}

            {(!Array.isArray(data) || data.length === 0) && (
              <div className="text-center py-12">
                <p className="text-[#6B6B6B]">Nenhuma foto encontrada para esta exposição.</p>
              </div>
            )}
          </section>
        ) : (
          <div className="text-center py-12">
            <p className="text-[#6B6B6B]">Erro ao carregar dados da exposição.</p>
          </div>
        )}
      </div>
    </main>
  )
}
