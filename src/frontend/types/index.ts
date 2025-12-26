export type TimelinePhoto = {
  photo_id: number
  file_name: string
  description?: string
  original_date?: string
}

export type TimelineDecade = {
  decade: number
  photos: TimelinePhoto[]
}

export type Story = {
  id: number
  title: string
  content: string
  author_name?: string
  author_relation?: string
  visibility: string
}

export type PublicPhotoDetail = {
  photo_id: number
  file_name: string
  description?: string
  original_date?: string
  decade?: number | null
  location?: string | null
  people: any[]
}
