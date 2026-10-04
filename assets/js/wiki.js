const input = document.querySelector('[data-wiki-search]');
const cards = [...document.querySelectorAll('[data-wiki-card]')];
const filters = [...document.querySelectorAll('[data-filter]')];
const empty = document.querySelector('[data-wiki-empty]');
let category = 'all';

function update() {
  const query = (input?.value || '').trim().toLowerCase();
  let shown = 0;
  cards.forEach(card => {
    const matchesText = !query || card.dataset.search.includes(query);
    const matchesCategory = category === 'all' || card.dataset.category === category;
    const visible = matchesText && matchesCategory;
    card.hidden = !visible;
    if (visible) shown++;
  });
  if (empty) empty.hidden = shown !== 0;
}

input?.addEventListener('input', update);
filters.forEach(button => button.addEventListener('click', () => {
  category = button.dataset.filter;
  filters.forEach(x => x.classList.toggle('is-active', x === button));
  update();
}));

document.addEventListener('keydown', event => {
  if (event.key === '/' && document.activeElement?.tagName !== 'INPUT') {
    event.preventDefault();
    input?.focus();
  }
});
