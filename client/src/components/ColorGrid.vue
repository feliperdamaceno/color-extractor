<script setup lang="ts">
import type { RGBColor } from '../types'
import { RGBTile } from '../components'

defineProps<{
  colors: RGBColor[]
}>()
</script>

<template>
  <div class="grid grid-cols-5 gap-2">
    <RGBTile v-for="color in colors" :color="color" />
  </div>
</template>
