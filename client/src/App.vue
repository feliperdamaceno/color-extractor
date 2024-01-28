<script setup lang="ts">
import { ImageExtrator, ColorGrid, Footer } from './components'
import { useColorExtractor } from './composables'

const { colors } = useColorExtractor()
</script>

<template>
  <main class="grid flex-1 gap-4 place-content-center justify-items-center">
    <ImageExtrator />
    <ColorGrid :colors="colors" />
  </main>
  <Footer class="mt-auto" />
</template>
