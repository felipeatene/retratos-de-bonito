export default function StoryCard({ story }: any) {
  return (
    <article className="border-l-4 border-green-600 pl-4 mb-4">
      <h3 className="font-semibold">{story.title}</h3>
      <p className="text-sm mt-1">{story.content}</p>
      {story.author_name && (
        <p className="text-xs text-gray-500 mt-1">{story.author_name} – {story.author_relation}</p>
      )}
    </article>
  )
}
