export default function DownloadModal({ photo }: any) {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/50">
      <div className="bg-white rounded p-4 max-w-lg w-full">
        <h3 className="font-semibold">Termo de uso</h3>
        <p className="text-sm mt-2">Ao baixar, você aceita creditar e não usar para fins comerciais sem autorização.</p>
        <div className="mt-4 flex justify-end">
          <button className="px-4 py-2 bg-green-600 text-white rounded">Concordo e baixar</button>
        </div>
      </div>
    </div>
  )
}
