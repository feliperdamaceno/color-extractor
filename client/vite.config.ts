import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'
import svgLoader from 'vite-svg-loader'

svgLoader({
  defaultImport: 'component'
})

export default defineConfig({
  plugins: [vue(), svgLoader()],
  server: {
    port: 3000
  },
  build: {
    outDir: '../static',
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name].[ext]'
      }
    }
  }
})
