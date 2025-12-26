'use client'

import { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'

export default function UploadPhotoPage() {
  const router = useRouter()
  const [step, setStep] = useState<'foto' | 'contexto' | 'consentimento'>('foto')
  const [file, setFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [description, setDescription] = useState('')
  const [source, setSource] = useState('')
  const [accepted, setAccepted] = useState(false)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const apiBase = process.env.NEXT_PUBLIC_API_URL || ''

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0]
    if (!selectedFile) return

    // Validar tipo
    if (!selectedFile.type.startsWith('image/')) {
      setError('Por favor, selecione uma imagem válida')
      return
    }

    // Validar tamanho (máx 10MB)
    if (selectedFile.size > 10 * 1024 * 1024) {
      setError('A imagem deve ter menos de 10MB')
      return
    }

    setFile(selectedFile)
    setError(null)

    // Preview
    const reader = new FileReader()
    reader.onload = e => {
      setPreview(e.target?.result as string)
    }
    reader.readAsDataURL(selectedFile)
  }

  const handleNextStep = () => {
    if (step === 'foto' && file) {
      setStep('contexto')
    } else if (step === 'contexto' && description.trim()) {
      setStep('consentimento')
    }
  }

  const handleSubmit = async () => {
    if (!file || !accepted) return

    setIsSubmitting(true)
    setError(null)

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('description', description)
      formData.append('source', source)

      const response = await fetch(`${apiBase}/photos/upload`, {
        method: 'POST',
        body: formData
      })

      if (!response.ok) {
        throw new Error('Erro ao enviar fotografia')
      }

      router.push('/contribuir/obrigado')
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'Erro ao enviar. Tente novamente.'
      )
      setIsSubmitting(false)
    }
  }

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
      <div className="mx-auto max-w-2xl px-6 py-16">
        {/* Indicador de progresso */}
        <div className="mb-12 space-y-2">
          <div className="flex gap-2">
            <div className={`h-1 flex-1 rounded ${step === 'foto' || step === 'contexto' || step === 'consentimento' ? 'bg-[#1F3D2B]' : 'bg-[#d8d3c7]'}`} />
            <div className={`h-1 flex-1 rounded ${step === 'contexto' || step === 'consentimento' ? 'bg-[#1F3D2B]' : 'bg-[#d8d3c7]'}`} />
            <div className={`h-1 flex-1 rounded ${step === 'consentimento' ? 'bg-[#1F3D2B]' : 'bg-[#d8d3c7]'}`} />
          </div>
          <p className="text-xs uppercase tracking-widest text-[#6B6B6B]">
            {step === 'foto' && 'Etapa 1 de 3 — A fotografia'}
            {step === 'contexto' && 'Etapa 2 de 3 — Contexto'}
            {step === 'consentimento' && 'Etapa 3 de 3 — Confirmação'}
          </p>
        </div>

        {/* ETAPA 1: Foto */}
        {step === 'foto' && (
          <div className="space-y-8">
            <div className="space-y-4">
              <h1 className="font-serif text-4xl text-[#1C1C1C]">Escolha a fotografia</h1>
              <p className="text-[#6B6B6B]">
                Essa fotografia fará parte do acervo histórico de Bonito.
              </p>
            </div>

            {!preview && (
              <div className="border-2 border-dashed border-[#c9c1b0] rounded-xl p-12 text-center space-y-4 bg-white/50">
                <div className="text-4xl">📸</div>
                <div className="space-y-2">
                  <p className="font-medium text-[#1C1C1C]">Selecione uma imagem</p>
                  <p className="text-sm text-[#6B6B6B]">JPG, PNG ou WebP (máximo 10MB)</p>
                </div>
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleFileChange}
                  className="w-full"
                />
              </div>
            )}

            {preview && (
              <div className="space-y-4">
                <div className="relative aspect-[3/4] overflow-hidden rounded-xl border border-[#e7e3d7] bg-white">
                  <img src={preview} alt="Preview" className="w-full h-full object-contain" />
                </div>
                <button
                  onClick={() => {
                    setFile(null)
                    setPreview(null)
                    setError(null)
                  }}
                  className="text-sm text-[#6B6B6B] hover:text-[#1C1C1C] transition"
                >
                  ← Escolher outra imagem
                </button>
              </div>
            )}

            {error && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 text-sm">
                {error}
              </div>
            )}

            <div className="flex gap-3">
              <button
                onClick={handleNextStep}
                disabled={!file}
                className="flex-1 bg-[#1F3D2B] text-[#F5F3EE] px-6 py-4 rounded-lg font-medium transition hover:bg-[#2d5a3d] disabled:opacity-50 disabled:cursor-not-allowed hover:disabled:bg-[#1F3D2B]"
              >
                Continuar
              </button>
              <Link
                href="/contribuir"
                className="inline-flex items-center justify-center text-[#1C1C1C] px-6 py-4 rounded-lg font-medium transition hover:text-[#1F3D2B]"
              >
                Voltar
              </Link>
            </div>
          </div>
        )}

        {/* ETAPA 2: Contexto */}
        {step === 'contexto' && (
          <div className="space-y-8">
            <div className="space-y-4">
              <h1 className="font-serif text-4xl text-[#1C1C1C]">Conte sobre a foto</h1>
              <p className="text-[#6B6B6B]">
                Informações simples ajudam a preservar a história com cuidado.
              </p>
            </div>

            <div className="space-y-6">
              {/* Descrição */}
              <div className="space-y-2">
                <label className="block font-medium text-[#1C1C1C]">
                  O que mostra esta fotografia?
                </label>
                <textarea
                  value={description}
                  onChange={e => setDescription(e.target.value)}
                  placeholder="Ex: Praça central nos anos 90, festa de Nossa Senhora, grupo de trabalhadoras rurais..."
                  className="w-full border border-[#d8d3c7] rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-[#1F3D2B] font-sans text-[#1C1C1C]"
                  rows={4}
                />
                <p className="text-xs text-[#6B6B6B]">Obrigatório</p>
              </div>

              {/* Origem */}
              <div className="space-y-2">
                <label className="block font-medium text-[#1C1C1C]">
                  De onde vem esta foto?
                </label>
                <input
                  type="text"
                  value={source}
                  onChange={e => setSource(e.target.value)}
                  placeholder="Ex: arquivo pessoal, acervo da família, jornal local..."
                  className="w-full border border-[#d8d3c7] rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-[#1F3D2B] font-sans text-[#1C1C1C]"
                />
                <p className="text-xs text-[#6B6B6B]">Opcional</p>
              </div>
            </div>

            {error && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 text-sm">
                {error}
              </div>
            )}

            <div className="flex gap-3">
              <button
                onClick={handleNextStep}
                disabled={!description.trim()}
                className="flex-1 bg-[#1F3D2B] text-[#F5F3EE] px-6 py-4 rounded-lg font-medium transition hover:bg-[#2d5a3d] disabled:opacity-50 disabled:cursor-not-allowed hover:disabled:bg-[#1F3D2B]"
              >
                Continuar
              </button>
              <button
                onClick={() => setStep('foto')}
                className="inline-flex items-center justify-center text-[#1C1C1C] px-6 py-4 rounded-lg font-medium transition hover:text-[#1F3D2B]"
              >
                Voltar
              </button>
            </div>
          </div>
        )}

        {/* ETAPA 3: Consentimento */}
        {step === 'consentimento' && (
          <div className="space-y-8">
            <div className="space-y-4">
              <h1 className="font-serif text-4xl text-[#1C1C1C]">Conferir tudo</h1>
              <p className="text-[#6B6B6B]">
                Uma última confirmação antes de enviar sua memória.
              </p>
            </div>

            {/* Resumo */}
            <div className="bg-white border border-[#e7e3d7] rounded-xl p-6 space-y-6">
              <div>
                <p className="text-xs uppercase tracking-widest text-[#6B6B6B] mb-2">Fotografia</p>
                {preview && (
                  <div className="relative aspect-[3/4] overflow-hidden rounded-lg border border-[#e7e3d7]">
                    <img src={preview} alt="Preview" className="w-full h-full object-contain" />
                  </div>
                )}
              </div>

              <div>
                <p className="text-xs uppercase tracking-widest text-[#6B6B6B] mb-2">Descrição</p>
                <p className="text-[#1C1C1C]">{description}</p>
              </div>

              {source && (
                <div>
                  <p className="text-xs uppercase tracking-widest text-[#6B6B6B] mb-2">Origem</p>
                  <p className="text-[#1C1C1C]">{source}</p>
                </div>
              )}
            </div>

            {/* Consentimento */}
            <div className="space-y-4">
              <div className="bg-[#F5F3EE] border border-[#d8d3c7] rounded-lg p-6 space-y-4">
                <h3 className="font-medium text-[#1C1C1C]">Autorização</h3>
                <label className="flex gap-3 items-start cursor-pointer">
                  <input
                    type="checkbox"
                    checked={accepted}
                    onChange={e => setAccepted(e.target.checked)}
                    className="mt-1 w-5 h-5 accent-[#1F3D2B] cursor-pointer"
                  />
                  <span className="text-sm text-[#6B6B6B] leading-relaxed">
                    Confirmo que posso compartilhar esta imagem para fins culturais e históricos. 
                    Entendo que ela será curadora e poderá ser publicada no acervo de Retratos de Bonito.
                  </span>
                </label>
              </div>

              <p className="text-xs text-[#6B6B6B] leading-relaxed">
                Sua privacidade importa. A imagem será armazenada com segurança e respeitará todas as políticas de proteção de dados.
              </p>
            </div>

            {error && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 text-sm">
                {error}
              </div>
            )}

            <div className="flex gap-3">
              <button
                onClick={handleSubmit}
                disabled={!accepted || isSubmitting}
                className="flex-1 bg-[#1F3D2B] text-[#F5F3EE] px-6 py-4 rounded-lg font-medium transition hover:bg-[#2d5a3d] disabled:opacity-50 disabled:cursor-not-allowed hover:disabled:bg-[#1F3D2B]"
              >
                {isSubmitting ? 'Enviando...' : 'Enviar fotografia'}
              </button>
              <button
                onClick={() => setStep('contexto')}
                disabled={isSubmitting}
                className="inline-flex items-center justify-center text-[#1C1C1C] px-6 py-4 rounded-lg font-medium transition hover:text-[#1F3D2B] disabled:opacity-50"
              >
                Voltar
              </button>
            </div>
          </div>
        )}
      </div>
    </main>
  )
}
