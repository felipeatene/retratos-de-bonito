export const exposicoes = {
  decadas: {
    slug: 'decadas-de-bonito',
    title: 'Décadas de Bonito',
    description:
      'Uma viagem visual pelas transformações da cidade ao longo do tempo. De década em década, veja como Bonito cresceu, mudou e manteve sua identidade.',
    apiEndpoint: '/public/timeline'
  },

  praca: {
    slug: 'praca-central',
    title: 'Praça Central',
    description:
      'Registros históricos da Praça Central como espaço de encontro, celebração e memória coletiva da comunidade bonitesenese.',
    apiEndpoint: '/public/search?location=Praça'
  },

  trabalho: {
    slug: 'memoria-do-trabalho',
    title: 'Memória do Trabalho',
    description:
      'Fotografias que documentam o trabalho, a produção e a vida econômica de Bonito ao longo dos anos.',
    apiEndpoint: '/public/search?collection=trabalho'
  },

  festas: {
    slug: 'festas-celebracoes',
    title: 'Festas e Celebrações',
    description:
      'Momentos de alegria compartilhada. Festas, eventos culturais e celebrações que marcaram a história de Bonito.',
    apiEndpoint: '/public/search?collection=festas'
  }
}

export type ExposicaoConfig = typeof exposicoes[keyof typeof exposicoes]

export function getExposicaoBySlug(slug: string): ExposicaoConfig | null {
  const expo = Object.values(exposicoes).find(e => e.slug === slug)
  return expo || null
}
