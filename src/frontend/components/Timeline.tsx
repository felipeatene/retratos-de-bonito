import PhotoCard from './PhotoCard'

export default function Timeline({ data }: any) {
  if (!data) return null

  return (
    <div className="space-y-10">
      {data.map((decade: any) => (
        <section key={decade.decade}>
          <h2 className="text-2xl font-semibold mb-4">Década de {decade.decade}</h2>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {decade.photos.map((photo: any) => (
              <PhotoCard key={photo.photo_id} photo={photo} />
            ))}
          </div>
        </section>
      ))}
    </div>
  )
}
