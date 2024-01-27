<script setup lang="ts">
import { ImageInput } from '../components'
import { useColorExtractor } from '../composables'

const { extractColors, loading } = useColorExtractor()
</script>

<template>
  <ImageInput :handle-submit="extractColors" :loading="loading" />
</template>
