#!/usr/bin/node

if (process.argv.length < 3) {
	console.log("Missing size");
} else {
	const num = parseInt(process.argv[2]);
	if (!isNaN(num)) {
		for (let i = 0; i < num; i++) {
			let line = '';
			for (let i = 0; i < num; i++) {
				line += 'x'
			}
			console.log(line);
		}
	} else {
		console.log("Missing size");
	}
}
