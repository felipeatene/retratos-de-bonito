'use client'

import QRCode from 'qrcode.react'

interface ExpoThemeQRCodeProps {
  slug: string
  label?: string
}

export default function ExpoThemeQRCode({ slug, label = 'Explore esta exposição no seu celular' }: ExpoThemeQRCodeProps) {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://retratosdebonito.org'
  const expoUrl = `${baseUrl}/expo/${slug}`

  return (
    <div className="absolute bottom-6 right-6 bg-black/70 p-4 rounded-lg flex flex-col items-center border border-white/20 z-40">
      <QRCode
        value={expoUrl}
        size={130}
        bgColor="#000000"
        fgColor="#ffffff"
        level="M"
        includeMargin={true}
      />
      <span className="text-white text-xs mt-3 opacity-75 text-center font-light leading-snug max-w-[150px]">
        {label}
      </span>
    </div>
  )
}
