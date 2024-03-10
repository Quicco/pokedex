const rows = document.querySelectorAll('.data');
// Add an eventListener to every row
for (let i = 0; i < rows.length; i++) {
  rows[i].addEventListener('click', () => {
    const form = rows[i].querySelector('.pkmn-data');
    form.submit();
  })
}