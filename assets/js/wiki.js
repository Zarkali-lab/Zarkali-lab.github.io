const input = document.querySelector('[data-wiki-search]');
const cards = [...document.querySelectorAll('[data-wiki-card]')];
const empty = document.querySelector('[data-wiki-empty]');

function update() {
  const query = (input?.value || '').trim().toLowerCase();
  let shown = 0;

  cards.forEach(card => {
    const visible = !query || card.dataset.search.includes(query);
    card.hidden = !visible;
    if (visible) shown++;
  });

  if (empty) empty.hidden = shown !== 0;
}

input?.addEventListener('input', update);

document.addEventListener('keydown', event => {
  if (event.key === '/' && document.activeElement?.tagName !== 'INPUT') {
    event.preventDefault();
    input?.focus();
  }
});
