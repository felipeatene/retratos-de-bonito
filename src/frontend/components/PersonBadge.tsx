export default function PersonBadge({ person }: any) {
  return (
    <span className="bg-gray-100 px-3 py-1 rounded text-sm">{person.full_name}</span>
  )
}
