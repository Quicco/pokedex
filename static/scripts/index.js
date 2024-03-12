const cards = document.querySelectorAll('.card-pokedex');

// Add an eventListener to every row
for (const card of cards) {
  card.addEventListener('click', () => {
    const form = card.querySelector('.pkmn-data');
    form.submit();
  });
}
// Add an eventListener to every row
// for (let i = 0; i < rows.length; i++) {
//   rows[i].addEventListener('click', () => {
//     const form = rows[i].querySelector('.pkmn-data');
//     form.submit();
//   })
// }

// Add 'Go Back' functionality to a button
const goBackBtn = document.querySelector('.go-back');

if (goBackBtn) {
  goBackBtn.addEventListener('click', () => {
    window.history.back();
  });
}
