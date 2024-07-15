/** @type {import('tailwindcss').Config} */
module.exports = {
	mode: 'jit',
	darkMode: 'class', //false, class, media
	content: [
		'./core/templates/**/*.html', // Adjust content path to include all templates
		'./static/**/*.css',
		'./static/**/*.js',
	],
	theme: {
		extend: {},
	},
	plugins: [],
};
