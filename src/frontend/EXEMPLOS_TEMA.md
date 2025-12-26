// Exemplos de como usar o Modo Exposição com diferentes temas

// ============================================================
// 1. USANDO TEMA PADRÃO (Décadas)
// ============================================================
// Em app/expo/page.tsx:
// const tema = exposicoes.decadas
// <ExpoThemeQRCode slug={tema.slug} />

// ============================================================
// 2. MÚLTIPLOS TEMAS (com parametrização)
// ============================================================
// Em app/expo/page.tsx (versão com suporte a tema via URL):

/*
'use client'

import { useSearchParams } from 'next/navigation'
import { exposicoes, getExposicaoBySlug } from '@/config/exposicoes'

export default function ExpoPage() {
  const searchParams = useSearchParams()
  const temaParam = searchParams.get('tema')
  
  // Usar tema da URL ou padrão
  const tema = getExposicaoBySlug(temaParam || 'decadas-de-bonito') || exposicoes.decadas

  // ... resto do código
  
  // No JSX:
  <ExpoThemeQRCode slug={tema.slug} />
}
*/

// ============================================================
// 3. CRIAR NOVO TEMA
// ============================================================
// Em config/exposicoes.ts:

/*
export const exposicoes = {
  // ... temas existentes ...

  minascultura: {
    slug: "minas-da-cultura",
    title: "Minas da Cultura",
    description:
      "A história da mineração em Bonito e seu impacto na vida cultural.",
    apiEndpoint: "/public/search?collection=mineracao"
  }
}
*/

// ============================================================
// 4. PÁGINA DE SELEÇÃO DE TEMAS (opcional)
// ============================================================
// Em app/expo/select/page.tsx:

/*
import { exposicoes } from '@/config/exposicoes'
import Link from 'next/link'

export default function ExpoSelectPage() {
  return (
    <main className="min-h-screen bg-[#F5F3EE] px-6 py-12">
      <h1 className="font-serif text-4xl text-[#1C1C1C] mb-8 max-w-6xl mx-auto">
        Escolha uma Exposição
      </h1>

      <div className="max-w-6xl mx-auto grid grid-cols-2 gap-6 md:grid-cols-4">
        {Object.values(exposicoes).map(expo => (
          <Link
            key={expo.slug}
            href={`/expo?tema=${expo.slug}`}
            className="group"
          >
            <div className="aspect-square rounded-lg bg-white border border-[#e7e3d7] p-6 flex flex-col justify-center items-center text-center hover:shadow-md transition">
              <h3 className="font-serif text-xl text-[#1C1C1C] mb-2">
                {expo.title}
              </h3>
              <p className="text-sm text-[#6B6B6B] line-clamp-3">
                {expo.description}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </main>
  )
}
*/

// ============================================================
// 5. THEME SELECTOR NO TELÃO (avançado)
// ============================================================
// Se quiser seletor de tema durante a exposição:
// Usar o componente ExpoThemeSelector (já implementado)

// import ExpoThemeSelector from '@/components/ExpoThemeSelector'
// <ExpoThemeSelector />  // aparece no canto superior esquerdo

// ============================================================
// 6. DADOS ESTRUTURA DA API ESPERADA
// ============================================================

// Timeline (/public/timeline):
/*
[
  {
    "decade": 1990,
    "photos": [
      {
        "photo_id": 1,
        "file_name": "2025/bonito-1995.jpg",
        "description": "Praça central",
        "location": "Centro",
        "original_date": "1995"
      }
    ]
  },
  {
    "decade": 2000,
    "photos": [ ... ]
  }
]
*/

// Search Results (/public/search?location=Praça):
/*
[
  {
    "photo_id": 1,
    "file_name": "2025/praca-1990.jpg",
    "description": "Praça central",
    "location": "Centro",
    "original_date": "1990"
  },
  {
    "photo_id": 2,
    "file_name": "2025/praca-2000.jpg",
    "description": "Praça reformada",
    "location": "Centro",
    "original_date": "2000"
  }
]
*/

// ============================================================
// 7. AMBIENTE (ENV VARS)
// ============================================================

/*
# .env.local

NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SITE_URL=http://localhost:3000

# Produção (Vercel):
# NEXT_PUBLIC_API_URL=https://api.retratosdebonito.org
# NEXT_PUBLIC_SITE_URL=https://retratosdebonito.org
*/

// ============================================================
// 8. LINKS ÚTEIS
// ============================================================

/*
Acesso direto a temas:

http://localhost:3000/expo                       → Padrão (Décadas)
http://localhost:3000/expo?tema=praca-central    → Praça Central
http://localhost:3000/expo?tema=memoria-do-trabalho → Memória do Trabalho
http://localhost:3000/expo?tema=festas-celebracoes  → Festas

Páginas temáticas públicas (destino do QR):

http://localhost:3000/expo/decadas-de-bonito
http://localhost:3000/expo/praca-central
http://localhost:3000/expo/memoria-do-trabalho
http://localhost:3000/expo/festas-celebracoes

Seletor de temas (opcional):

http://localhost:3000/expo/select
*/
