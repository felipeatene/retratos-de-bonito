import Timeline from '@/components/Timeline'
import { getTimeline } from '@/lib/api'

export default async function HomePage() {
  const timeline = await getTimeline()

  return (
    <main className="max-w-6xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Retratos de Bonito</h1>
      <Timeline data={timeline} />
    </main>
  )
}
