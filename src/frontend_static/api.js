const API = 'http://127.0.0.1:8000'

async function getTimeline() {
  const res = await fetch(API + '/public/timeline')
  if (!res.ok) throw new Error('Erro ' + res.status)
  return res.json()
}

async function searchPhotos(params) {
  const qs = new URLSearchParams(params).toString()
  const res = await fetch(API + '/public/search?' + qs)
  if (!res.ok) throw new Error('Erro ' + res.status)
  return res.json()
}

async function getPhotoDetail(id) {
  const res = await fetch(API + '/public/photos/' + id)
  if (!res.ok) throw new Error('Erro ' + res.status)
  return res.json()
}

async function getPhotoStories(id) {
  const res = await fetch(API + '/public/photos/' + id + '/stories')
  if (!res.ok) throw new Error('Erro ' + res.status)
  return res.json()
}
