import Link from 'next/link'

export default function PhotoCard({ photo }: any) {
  return (
    <Link href={`/photos/${photo.photo_id}`}>
      <div className="border rounded-lg overflow-hidden hover:shadow-lg transition">
        <img
          src={`${process.env.NEXT_PUBLIC_API_URL}/${photo.file_name}`}
          alt={photo.description}
          className="w-full h-40 object-cover"
        />
        <div className="p-2 text-sm">{photo.description}</div>
      </div>
    </Link>
  )
}
