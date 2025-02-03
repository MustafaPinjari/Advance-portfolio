/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      fontFamily : {
        "ovo" : ["Ovo"],
        "outfit" : ["Outfit"]
      },
      colors:{
        lightHover : '#fcf4ff',
        darkHover : '#2a004a',
        darkTheme : '#11001F'
      },
      
      animation: {
        'spin-slow': 'spin 6s linear infinite',
      },
      boxShadow:{
        'black' : '4px 4px 0 #000',
        'white' : '4px 4px 0 #fff'
      }

      
    },
  },
  darkMode : 'selector'
}

