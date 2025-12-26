import { getPhotoDetail, getPhotoStories } from '@/lib/api'
import StoryCard from '@/components/StoryCard'

export default async function PhotoPage({ params }: any) {
  const photo = await getPhotoDetail(params.id)
  const stories = await getPhotoStories(params.id)

  return (
    <main className="max-w-4xl mx-auto p-6 space-y-6">
      <img
        src={`${process.env.NEXT_PUBLIC_API_URL}/${photo.file_name}`}
        alt={photo.description}
        className="w-full rounded-lg"
      />

      <div>
        <h1 className="text-2xl font-bold">{photo.description}</h1>
        <p className="text-sm text-gray-500">{photo.location} · {photo.decade}s</p>
      </div>

      <section>
        <h2 className="text-xl font-semibold mb-2">Pessoas na foto</h2>
        <ul className="flex flex-wrap gap-2">
          {photo.people.map((p: any) => (
            <li key={p.full_name} className="bg-gray-100 px-3 py-1 rounded">{p.full_name} ({p.role})</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold mb-2">Histórias</h2>
        {stories.map((story: any) => (
          <StoryCard key={story.id} story={story} />
        ))}
      </section>
    </main>
  )
}
