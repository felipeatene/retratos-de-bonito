const API_BASE = process.env.NEXT_PUBLIC_API_URL || ''

export async function getTimeline() {
  const res = await fetch(`${API_BASE}/public/timeline`, { next: { revalidate: 3600 } })
  return res.json()
}

export async function searchPhotos(params: string) {
  const res = await fetch(`${API_BASE}/public/search?${params}`)
  return res.json()
}

export async function getPhotoDetail(id: string) {
  const res = await fetch(`${API_BASE}/public/photos/${id}`)
  return res.json()
}

export async function getPhotoStories(id: string) {
  const res = await fetch(`${API_BASE}/public/photos/${id}/stories`)
  return res.json()
}

export default { getTimeline, searchPhotos, getPhotoDetail, getPhotoStories }
