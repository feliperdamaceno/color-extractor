<script setup lang="ts">
import { RGBColor, HSLColor } from '../types'
import { RGBTile, HSLTile } from '../components'

import { useColorExtractor } from '../composables'
const { colorScheme } = useColorExtractor()

defineProps<{
  colors: RGBColor | HSLColor[]
}>()
</script>

<template>
  <div class="grid grid-cols-5 gap-2">
    <RGBTile
      v-if="colorScheme == 'rgb'"
      v-for="color in colors"
      :color="color"
    />
    <HSLTile v-else v-for="color in colors" :color="color" />
  </div>
</template>
