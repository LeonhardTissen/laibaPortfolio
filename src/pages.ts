// Register a function on each anchor tag
document.querySelectorAll<HTMLAnchorElement>('a').forEach((element) => {
	element.addEventListener('click', (ev) => {
		const page = element.href.split('#')[1];

		if (page === undefined) return;

		ev.preventDefault();

		setPage(page);
	});
});

// If user loaded page with a hash, automatically navigate to that article
const hash = window.location.hash;
if (hash) {
	setPage(hash.replace('#',''));
}

function capitalizeFirst(input: string): string {
	return input.charAt(0).toUpperCase() + input.slice(1);
}

function setPage(page: string): void {
	window.location.hash = page;

	document.title = `Laiba Tariq - ${capitalizeFirst(page)}`;

	// Hide all anchor tags that were previously selected
	const non_selected_links = document.querySelectorAll<HTMLAnchorElement>('.link.selected');

	non_selected_links.forEach((link) => {
		link.classList.remove('selected');
	});

	// Apply a selected class to all anchor tags that are now selected
	const selected_links = document.querySelectorAll<HTMLAnchorElement>(`.link${page}`);

	selected_links.forEach((link) => {
		link.classList.add('selected');
	});

	// Hide all pages that were previously selected
	const non_selected_pages = document.querySelectorAll<HTMLElement>('.page.selected');

	non_selected_pages.forEach((page_element) => {
		page_element.classList.remove('selected');
	});

	// Apply a selected class to all anchor tags that are now selected
	const selected_pages = document.querySelectorAll<HTMLElement>(`#${page}`);

	selected_pages.forEach((page_element) => {
		page_element.classList.add('selected');
	});

	scrollToTop();
}

function scrollToTop(): void {
	window.scrollTo({ top: 0 });
}
