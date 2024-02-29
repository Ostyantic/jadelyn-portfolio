/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
        colors: {
            'Nyanza': '#E1f4CB',
        }
    },
  },
  plugins: [
      require('flowbite/plugin'),
  ],
}

