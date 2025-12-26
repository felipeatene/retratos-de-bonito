"use client";

import { useEffect, useMemo, useState } from "react";

type ExpoPhoto = {
  photo_id: number;
  file_name: string;
  description?: string | null;
  decade?: number | null;
  location?: string | null;
};

const INTERVAL_MS = 12000; // 12s por foto

export default function ExpoPage() {
  const [photos, setPhotos] = useState<ExpoPhoto[]>([]);
  const [index, setIndex] = useState(0);
  const [loaded, setLoaded] = useState(false);
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  useEffect(() => {
    let cancelled = false;
    const url = `${apiUrl}/public/expo?mode=timeline`;

    fetch(url)
      .then((res) => res.json())
      .then((data: ExpoPhoto[]) => {
        if (!cancelled && Array.isArray(data)) {
          setPhotos(data);
          setIndex(0);
        }
      })
      .catch(() => {
        // Falha: mantém tela limpa com crédito
        setPhotos([]);
      });

    return () => {
      cancelled = true;
    };
  }, [apiUrl]);

  useEffect(() => {
    if (!photos.length) return;

    const timer = setInterval(() => {
      setLoaded(false);
      setIndex((i) => (i + 1) % photos.length);
    }, INTERVAL_MS);

    return () => clearInterval(timer);
  }, [photos]);

  useEffect(() => {
    // Reset animação de fade/zoom ao trocar a foto
    setLoaded(false);
    const t = setTimeout(() => setLoaded(true), 50);
    return () => clearTimeout(t);
  }, [index]);

  const photo = useMemo(() => photos[index], [photos, index]);

  return (
    <main className="w-screen h-screen bg-black text-white flex flex-col justify-center items-center overflow-hidden">
      {/* Imagem ou fallback */}
      {photo ? (
        <div className="relative w-full flex justify-center items-center" style={{ height: "80vh" }}>
          <img
            src={`${apiUrl}/${photo.file_name}`}
            className={`max-h-[80vh] object-contain transition-opacity duration-1000 ease-in-out ${
              loaded ? "opacity-100" : "opacity-0"
            }`}
            style={{
              animation: loaded ? `slow-zoom ${INTERVAL_MS}ms linear forwards` : "none",
            }}
            onLoad={() => setLoaded(true)}
            alt={photo.description ?? "Retratos de Bonito"}
          />
        </div>
      ) : (
        <div className="flex h-[80vh] w-full items-center justify-center">
          <div className="text-center opacity-80">
            <p className="text-xl">Retratos de Bonito – Acervo Cultural</p>
          </div>
        </div>
      )}

      {/* Legenda mínima */}
      <div className="mt-6 text-center text-xl sm:text-lg opacity-80 px-4">
        {photo && (
          <>
            {photo.description && <p className="text-2xl sm:text-xl">{photo.description}</p>}
            <p className="text-base sm:text-sm mt-2">
              {photo.location ?? ""}
              {photo.location && photo.decade ? " · " : ""}
              {photo.decade ? `${photo.decade}s` : ""}
            </p>
          </>
        )}
        <p className="text-xs mt-3 opacity-60">Retratos de Bonito – Acervo Cultural</p>
      </div>

      {/* Estilo para zoom lento */}
      <style jsx>{`
        @keyframes slow-zoom {
          from { transform: scale(1.0); }
          to { transform: scale(1.05); }
        }
      `}</style>
    </main>
  );
}