import './css/main.css';
import './css/nav.css';
import './css/page.css';
import './css/footer.css';

document.querySelectorAll<HTMLElement>('.lorem').forEach((element) => {
	element.innerText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
});

document.querySelectorAll<HTMLAnchorElement>('a').forEach((element) => {
	element.addEventListener('click', (ev) => {
		ev.preventDefault();

		const page = element.href.split('#')[1];

		setPage(page);
	});
});

const hash = window.location.hash;
if (hash) {
	setPage(hash.replace('#',''));
}

function setPage(page: string): void {
	window.location.hash = page;

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
