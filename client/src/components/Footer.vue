<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer
    class="w-full max-w-sm py-4 mx-auto text-sm font-medium text-center text-zinc-500"
  >
    <p>
      <span>Color Extractor © {{ currentYear }}</span>
      <a href="https://github.com/feliperdamaceno" target="_blank" rel="author">
        feliperdamaceno
      </a>
    </p>
  </footer>
</template>
