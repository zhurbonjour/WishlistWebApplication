document.addEventListener('DOMContentLoaded', () => {
  const themeToggler        = document.getElementById('themeToggler');

  /******************
   *** Dark theme ***
   ******************/
  if (window.matchMedia('(prefers-color-scheme: dark)').matches) document.body.classList.add('night-theme');
  themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('night-theme');
  })
})
