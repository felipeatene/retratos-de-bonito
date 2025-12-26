'use client'

import { useEffect, useState, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import ExpoThemeQRCode from '@/components/ExpoThemeQRCode'
import { exposicoes } from '@/config/exposicoes'

type IntroSlide = {
  type: 'intro'
  decade: number
}

type PhotoSlide = {
  type: 'photo'
  photo: {
    photo_id: number
    file_name: string
    description?: string
    decade?: number
    location?: string
  }
}

type Slide = IntroSlide | PhotoSlide

function buildSlides(timeline: any[]): Slide[] {
  const slides: Slide[] = []

  timeline.forEach((block: any) => {
    slides.push({ type: 'intro', decade: block.decade })

    block.photos.forEach((photo: any) => {
      slides.push({
        type: 'photo',
        photo: {
          photo_id: photo.photo_id,
          file_name: photo.file_name,
          description: photo.description,
          decade: block.decade,
          location: photo.location
        }
      })
    })
  })

  return slides
}

export default function ExpoPage() {
  const [slides, setSlides] = useState<Slide[]>([])
  const [index, setIndex] = useState(0)
  const [isPlaying, setIsPlaying] = useState(true)
  const timerRef = useRef<NodeJS.Timeout | null>(null)
  const apiBase = process.env.NEXT_PUBLIC_API_URL || ''

  // Usar tema padrão (decadas)
  const tema = exposicoes.decadas

  // Carrega timeline da API
  useEffect(() => {
    fetch(`${apiBase}/public/timeline`)
      .then(res => res.json())
      .then(data => {
        const builtSlides = buildSlides(data)
        setSlides(builtSlides)
      })
      .catch(err => console.error('Erro ao carregar timeline:', err))
  }, [apiBase])

  // Controla transição automática de slides
  useEffect(() => {
    if (!slides.length || !isPlaying) {
      if (timerRef.current) clearTimeout(timerRef.current)
      return
    }

    const current = slides[index]
    // Intro: 7s, Foto: 12s
    const duration = current.type === 'intro' ? 7000 : 12000

    timerRef.current = setTimeout(() => {
      setIndex(i => (i + 1) % slides.length)
    }, duration)

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [index, slides, isPlaying])

  // Mantém execução ao perder foco
  useEffect(() => {
    const handleVisibilityChange = () => {
      // Continua rodando mesmo se aba ficar invisível
      // (comentado para respeitar padrões de performance)
      // setIsPlaying(!document.hidden)
    }

    document.addEventListener('visibilitychange', handleVisibilityChange)
    return () => document.removeEventListener('visibilitychange', handleVisibilityChange)
  }, [])

  if (!slides.length) {
    return (
      <div className="w-screen h-screen bg-black flex items-center justify-center text-white">
        <p className="text-2xl">Carregando acervo...</p>
      </div>
    )
  }

  const slide = slides[index]

  return (
    <main className="w-screen h-screen bg-black overflow-hidden relative">
      <AnimatePresence mode="wait">
        {slide.type === 'intro' && (
          <motion.div
            key={`intro-${slide.decade}`}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1.5, ease: 'easeInOut' }}
            className="absolute inset-0 flex flex-col items-center justify-center text-white text-center px-8"
          >
            <h1 className="text-7xl md:text-8xl font-serif font-light tracking-tight mb-6">
              Década de {slide.decade}
            </h1>
            <p className="text-xl md:text-2xl text-white/70 max-w-2xl font-light">
              Memórias visuais de Bonito neste período
            </p>
          </motion.div>
        )}

        {slide.type === 'photo' && (
          <motion.div
            key={`photo-${slide.photo.photo_id}`}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1.2, ease: 'easeInOut' }}
            className="absolute inset-0 flex flex-col items-center justify-center"
          >
            {/* Imagem com Ken Burns effect suave */}
            <motion.div
              initial={{ scale: 1 }}
              animate={{ scale: 1.05 }}
              transition={{ duration: 12, ease: 'easeInOut' }}
              className="absolute inset-0 flex items-center justify-center overflow-hidden"
            >
              <img
                src={`${apiBase}/${encodeURIComponent(slide.photo.file_name)}`}
                alt={slide.photo.description || 'Foto do acervo'}
                className="w-full h-full object-contain"
              />
            </motion.div>

            {/* Overlay escuro no topo (fade to transparent) */}
            <div className="absolute inset-0 bg-gradient-to-b from-black/50 via-transparent to-transparent pointer-events-none" />

            {/* Faixa de informação na base */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, duration: 0.8 }}
              className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent px-8 py-10 text-white"
            >
              <p className="text-2xl md:text-3xl font-light mb-2 leading-tight line-clamp-2">
                {slide.photo.description}
              </p>
              <div className="flex items-center gap-4 text-sm text-white/70 font-light">
                {slide.photo.location && (
                  <span>{slide.photo.location}</span>
                )}
                {slide.photo.decade && (
                  <span>Década de {slide.photo.decade}</span>
                )}
              </div>
              <p className="text-xs text-white/50 mt-3 uppercase tracking-wider">
                Retratos de Bonito — Acervo Histórico
              </p>
            </motion.div>

            {/* QR Code Temático */}
            <ExpoThemeQRCode slug={tema.slug} label="Explore esta exposição no seu celular" />
          </motion.div>
        )}
      </AnimatePresence>

      {/* Controles mínimos (canto inferior) */}
      <div className="absolute bottom-6 left-6 z-50 flex items-center gap-3 text-white/60 text-xs">
        <button
          onClick={() => setIsPlaying(!isPlaying)}
          className="w-8 h-8 rounded-full border border-white/30 flex items-center justify-center hover:border-white/60 transition"
          aria-label={isPlaying ? 'Pausar' : 'Reproduzir'}
        >
          {isPlaying ? '⏸' : '▶'}
        </button>
        <span className="font-light">
          {index + 1} / {slides.length}
        </span>
      </div>

      {/* Indicador de progresso (barra fina no topo) */}
      <motion.div
        className="absolute top-0 left-0 h-0.5 bg-white/60"
        initial={{ width: '0%' }}
        animate={{ width: '100%' }}
        transition={{ duration: slide.type === 'intro' ? 7 : 12, ease: 'linear' }}
      />
    </main>
  )
}
