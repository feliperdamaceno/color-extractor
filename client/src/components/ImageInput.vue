<script setup lang="ts">
import { LoadingIcon, PictureIcon } from '../assets'

import { useDropZone } from '@vueuse/core'
import { ref } from 'vue'

const { handleSubmit } = defineProps<{
  handleSubmit: (files: FormData) => Promise<void>
  loading: boolean
}>()

const fileInputRef = ref<HTMLInputElement>()

function createImageFormData(file: File): FormData {
  const formData = new FormData()
  formData.append('image', file)
  return formData
}

async function handleChange(event: Event) {
  const { files } = event.target as HTMLInputElement
  const file = files?.length ? files[0] : new FileList()[0]
  handleSubmit(createImageFormData(file))
}

async function handleDrop(files: File[] | null) {
  const file = files?.length ? files[0] : new FileList()[0]
  handleSubmit(createImageFormData(file))
}

useDropZone(fileInputRef, {
  onDrop: handleDrop,
  dataTypes: ['image/jpg', 'image/jpeg', 'image/png']
})
</script>

<template>
  <div
    class="relative grid h-56 gap-1 text-center transition-colors duration-150 ease-in-out border-2 border-dashed rounded-md place-content-center w-96 bg-zinc-100 border-zinc-200 text-zinc-500 hover:border-zinc-300"
  >
    <div class="w-8 h-8 mx-auto">
      <LoadingIcon v-if="loading" class="animate-spin" />
      <PictureIcon v-else="loading" />
    </div>

    <p><span class="font-semibold">Click to upload</span> or drag and drop</p>
    <p class="text-sm">JPG, JPEG or PNG</p>

    <input
      ref="fileInputRef"
      class="w-full h-full file:hidden text-[0] text-transparent cursor-pointer absolute"
      type="file"
      accept="image/jpg, image/jpeg, image/png"
      @change="handleChange"
    />
  </div>
</template>
