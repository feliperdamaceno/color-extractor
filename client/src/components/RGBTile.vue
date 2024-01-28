<script setup lang="ts">
import type { RGBColor } from '../types'
import colorConverter from 'color-convert'

const { color } = defineProps<{
  color: RGBColor
}>()
</script>

<template>
  <div class="w-20 h-20 border-2 border-zinc-200">
    <input
      class="w-full h-full"
      type="color"
      :value="`#${colorConverter.rgb.hex(color.r, color.g, color.b)}`"
    />
  </div>
</template>

<style lang="postcss">
input[type='color'],
input[type='color']::-webkit-color-swatch,
input[type='color']::-webkit-color-swatch-wrapper {
  -webkit-appearance: none;
  @apply border-none p-0 cursor-pointer;
}
</style>
