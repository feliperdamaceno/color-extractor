import type { ColorScheme, RGBColor, HSLColor } from '../types'
import { ref } from 'vue'

const BASE_URL = 'http://127.0.0.1:8000/extract'

const loading = ref<boolean>(false)
const colors = ref<RGBColor | HSLColor[]>([])
const colorScheme = ref<ColorScheme>('rgb')

async function extractColors(files: FormData) {
  loading.value = true
  const response = await fetch(`${BASE_URL}/${colorScheme.value}`, {
    method: 'POST',
    body: files
  })
  colors.value = await response.json()
  loading.value = false
}

function changeColorScheme(scheme: ColorScheme) {
  colorScheme.value = scheme
}

export default function useColorExtractor() {
  return { extractColors, loading, colors, changeColorScheme, colorScheme }
}
