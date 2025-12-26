'use client'

import { useRouter, useSearchParams } from 'next/navigation'
import { exposicoes, ExposicaoConfig } from '@/config/exposicoes'
import { useEffect, useState } from 'react'

export default function ExpoThemeSelector() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const [currentTheme, setCurrentTheme] = useState<ExposicaoConfig | null>(null)

  useEffect(() => {
    const themeParam = searchParams.get('tema')
    const selectedExpo =
      Object.values(exposicoes).find(e => e.slug === themeParam) ||
      exposicoes.decadas

    setCurrentTheme(selectedExpo)
  }, [searchParams])

  const handleThemeChange = (slug: string) => {
    router.push(`/expo?tema=${slug}`)
  }

  if (!currentTheme) return null

  return (
    <div className="absolute top-6 left-6 z-50 bg-black/70 p-4 rounded-lg border border-white/20">
      <p className="text-white text-xs opacity-60 mb-3 uppercase tracking-wide">Tema</p>
      <div className="space-y-2">
        {Object.values(exposicoes).map(expo => (
          <button
            key={expo.slug}
            onClick={() => handleThemeChange(expo.slug)}
            className={`block text-left text-sm transition ${
              currentTheme.slug === expo.slug
                ? 'text-white font-semibold'
                : 'text-white/60 hover:text-white'
            }`}
          >
            {expo.title}
          </button>
        ))}
      </div>
    </div>
  )
}
