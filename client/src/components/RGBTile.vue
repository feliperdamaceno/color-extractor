<script setup lang="ts">
import type { RGBColor } from '../types'

defineProps<{
  color: RGBColor
}>()
</script>

<template>
  <div
    :style="{ backgroundColor: `rgb(${color.r}, ${color.g}, ${color.b})` }"
    class="w-20 border-2 rounded-sm aspect-square border-zinc-200"
  />
</template>
