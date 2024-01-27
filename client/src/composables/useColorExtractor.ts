import { ref } from 'vue'
import type { RGBColor } from '../types'

const BASE_URL = 'http://127.0.0.1:8000/extract'
const COLOR_SCHEME = 'rgb'

const loading = ref<boolean>(false)
const colors = ref<RGBColor[]>([])

async function extractColors(files: FormData) {
  loading.value = true
  const response = await fetch(`${BASE_URL}/${COLOR_SCHEME}`, {
    method: 'POST',
    body: files
  })
  colors.value = await response.json()
  loading.value = false
}

export default function useColorExtractor() {
  return { colors, loading, extractColors }
}
