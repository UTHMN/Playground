/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["tailwind.css"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
}