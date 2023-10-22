import './css/main.css';
import './css/nav.css';
import './css/page.css';
import './css/footer.css';

document.querySelectorAll<HTMLElement>('.lorem').forEach((element) => {
	element.innerText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
});

document.querySelectorAll<HTMLAnchorElement>('a').forEach((element) => {
	element.addEventListener('click', () => {
		const page = element.href.split('#')[1];
		console.log(page);
	});
});
