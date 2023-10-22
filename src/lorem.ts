document.querySelectorAll<HTMLElement>('.lorem').forEach((element) => {
	element.innerText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
});
document.querySelectorAll<HTMLElement>('.loremshort').forEach((element) => {
	element.innerText = 'Lorem ipsum';
});
