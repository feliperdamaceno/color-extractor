<script setup lang="ts">
import { ref } from 'vue'
import { useDropZone } from '@vueuse/core'

type RGBColor = {
  r: number
  g: number
  b: number
}

const initialColors = [...Array(5)].map(() => ({ r: 244, g: 244, b: 245 }))

const colors = ref<RGBColor[]>(initialColors)

const fileInputRef = ref<HTMLInputElement>()

const { isOverDropZone } = useDropZone(fileInputRef, {
  onDrop: handleDrop,
  dataTypes: ['image/jpg', 'image/jpeg', 'image/png']
})

async function uploadFileToServer(formData: FormData) {
  const response = await fetch('http://127.0.0.1:8000/extract/rgb', {
    method: 'POST',
    body: formData
  })
  colors.value = await response.json()
}

async function handleDrop(files: File[] | null) {
  if (!files) return

  const formData = new FormData()
  formData.append('image', files[0])

  await uploadFileToServer(formData)
}

async function handleChange(event: Event) {
  const { files } = event.target as HTMLInputElement
  if (!files?.length) return

  const formData = new FormData()
  formData.append('image', files[0])
  await uploadFileToServer(formData)
}
</script>

<template>
  <main
    class="grid min-h-screen gap-4 place-content-center justify-items-center"
  >
    <div
      class="relative grid h-56 gap-1 text-center transition-colors duration-150 ease-in-out border-2 border-dashed rounded-md place-content-center w-96 bg-zinc-100 border-zinc-200 text-zinc-500 hover:border-zinc-300"
    >
      <div class="w-8 h-8 mx-auto">
        <svg
          v-if="isOverDropZone"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          class="animate-spin"
        >
          <path
            fill-rule="evenodd"
            d="M4.755 10.059a7.5 7.5 0 0 1 12.548-3.364l1.903 1.903h-3.183a.75.75 0 1 0 0 1.5h4.992a.75.75 0 0 0 .75-.75V4.356a.75.75 0 0 0-1.5 0v3.18l-1.9-1.9A9 9 0 0 0 3.306 9.67a.75.75 0 1 0 1.45.388Zm15.408 3.352a.75.75 0 0 0-.919.53 7.5 7.5 0 0 1-12.548 3.364l-1.902-1.903h3.183a.75.75 0 0 0 0-1.5H2.984a.75.75 0 0 0-.75.75v4.992a.75.75 0 0 0 1.5 0v-3.18l1.9 1.9a9 9 0 0 0 15.059-4.035.75.75 0 0 0-.53-.918Z"
            clip-rule="evenodd"
          />
        </svg>
        <svg
          v-else="isOverDropZone"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M1.5 6a2.25 2.25 0 0 1 2.25-2.25h16.5A2.25 2.25 0 0 1 22.5 6v12a2.25 2.25 0 0 1-2.25 2.25H3.75A2.25 2.25 0 0 1 1.5 18V6ZM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0 0 21 18v-1.94l-2.69-2.689a1.5 1.5 0 0 0-2.12 0l-.88.879.97.97a.75.75 0 1 1-1.06 1.06l-5.16-5.159a1.5 1.5 0 0 0-2.12 0L3 16.061Zm10.125-7.81a1.125 1.125 0 1 1 2.25 0 1.125 1.125 0 0 1-2.25 0Z"
            clip-rule="evenodd"
          />
        </svg>
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

    <div class="grid grid-cols-5 gap-2">
      <div
        v-for="color in colors"
        :style="{ backgroundColor: `rgb(${color.r}, ${color.g}, ${color.b})` }"
        class="w-20 border-2 rounded-sm aspect-square border-zinc-200"
      ></div>
    </div>
  </main>
</template>
