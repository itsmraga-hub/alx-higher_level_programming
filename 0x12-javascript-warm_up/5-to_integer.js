#!/usr/bin/node

if (process.argv.length < 3) {
	console.log("Not a number");
} else {
	const num = parseInt(process.argv[2]);
	if (num >= 0) {
		console.log("My number: ", num);
	} else {
		console.log("Not a number");
	}
}
