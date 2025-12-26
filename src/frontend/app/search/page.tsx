import React from 'react'
import { searchPhotos } from '@/lib/api'

export default async function SearchPage({ searchParams }: any) {
  const params = new URLSearchParams(searchParams).toString()
  const photos = await searchPhotos(params)

  return (
    <main className="max-w-6xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Resultados da busca</h1>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {photos.map((p: any) => (
          <div key={p.photo_id} className="border rounded-lg overflow-hidden">
            <img src={`${process.env.NEXT_PUBLIC_API_URL}/${p.file_name}`} className="w-full h-40 object-cover" />
            <div className="p-2 text-sm">{p.description}</div>
          </div>
        ))}
      </div>
    </main>
  )
}
