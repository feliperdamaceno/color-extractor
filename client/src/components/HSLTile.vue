<script setup lang="ts">
import { HSLColor } from '../types'

defineProps<{
  color: HSLColor
}>()
</script>

<template>
  <div
    :style="{ backgroundColor: `rgb(${color.h}, ${color.s}, ${color.l})` }"
    class="w-20 border-2 rounded-sm aspect-square border-zinc-200"
  ></div>
</template>
