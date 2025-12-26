'use client'

import QRCode from 'qrcode.react'

interface ExpoQRCodeProps {
  photoId: number
}

export default function ExpoQRCode({ photoId }: ExpoQRCodeProps) {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://retratosdebonito.org'
  const qrUrl = `${baseUrl}/photos/${photoId}`

  return (
    <div className="absolute bottom-28 right-6 flex flex-col items-center gap-2 bg-black/70 p-4 rounded-lg border border-white/20 z-40">
      <QRCode
        value={qrUrl}
        size={120}
        bgColor="#000000"
        fgColor="#ffffff"
        level="M"
        includeMargin={true}
      />
      <p className="text-white text-xs font-light text-center opacity-75">
        Acesse a história<br/>desta foto
      </p>
    </div>
  )
}
