import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  build: {
    minify: false,
    sourcemap: true,
    lib: {
      entry: path.resolve(__dirname, 'src/index.ts'),
      name: 'torch',
      fileName: (format) => `torch.browser.${format}.js`,
      formats: ['es'] // umd -> see cdn build
    },
    outDir: 'build/browser',
    rollupOptions: {
      treeshake: true,
    },
  },
  esbuild: {
    keepNames: true,
  }
});
