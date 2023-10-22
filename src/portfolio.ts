document.querySelectorAll<HTMLButtonElement>('#filters .filter').forEach((tag) => {
	tag.addEventListener('click', () => {
		const category = tag.dataset.category;
		if (category !== undefined) {
			filterBy(category);
		}

		document.querySelectorAll<HTMLButtonElement>('#filters .filter.selected').forEach((selected_tag) => {
			selected_tag.classList.remove('selected');
		});

		tag.classList.add('selected');
	});
});

function filterBy(tag: string): void {
	console.log(tag);
}
