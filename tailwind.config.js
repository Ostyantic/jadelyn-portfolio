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
            'Sage': '#BACBA9',
            'Dimgray': '#717568',
            'Blackolive': '#3F4739',
        }
    },
  },
  plugins: [
      require('flowbite/plugin'),
  ],
}

