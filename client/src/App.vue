<script setup lang="ts">
import { ImageExtrator, ColorGrid } from './components'
import { useColorExtractor } from './composables'
const { colors } = useColorExtractor()
</script>

<template>
  <main
    class="grid min-h-screen gap-4 place-content-center justify-items-center"
  >
    <ImageExtrator />
    <ColorGrid :colors="colors" />
  </main>
</template>
