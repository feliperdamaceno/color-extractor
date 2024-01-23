<script setup lang="ts">
import { useColorExtractor } from '../composables'
import { ImageInput } from '../components'

const { extractColors, loading } = useColorExtractor()
</script>

<template>
  <ImageInput :handle-submit="extractColors" :loading="loading" />
</template>
