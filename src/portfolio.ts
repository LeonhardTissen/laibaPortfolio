document.querySelectorAll<HTMLButtonElement>('#filters .filter').forEach((tag) => {
	tag.addEventListener('click', () => {
		const category = tag.dataset.category;
		if (category !== undefined) {
			filterBy(category);
		}

		if (tag.classList.contains('selected')) {
			removeFilter();
			tag.classList.remove('selected');
			return;
		}

		document.querySelectorAll<HTMLButtonElement>('#filters .filter.selected').forEach((selected_tag) => {
			selected_tag.classList.remove('selected');
		});

		tag.classList.add('selected');
	});
});

const no_results = document.getElementById('noresults') as HTMLElement;

function filterBy(tag: string): void {
	let results: number = 0;

	document.querySelectorAll<HTMLElement>('#works .work').forEach((work) => {
		const categories_str = work.dataset.categories;

		if (categories_str === undefined) return;

		const categories = categories_str.split(' ').filter((s) => s !== '');

		if (categories.includes(tag)) {
			work.style.display = 'block';
			results ++;
		} else {
			work.style.display = 'none';
		}
	});

	no_results.style.display = results === 0 ? 'block' : 'none';
}

function removeFilter(): void {
	no_results.style.display = 'none';

	document.querySelectorAll<HTMLElement>('#works .work').forEach((work) => {
		work.style.display = 'block';
	});
}
