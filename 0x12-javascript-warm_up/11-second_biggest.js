#!/usr/bin/node

const arr = process.argv

let nums = [];

for (let i = 0; i < process.argv.length; i++) {
	let n = parseInt(process.argv[i]);
	if (!isNaN(n)) {
		nums.push(n);
	}
}
if (nums.length === 0) {
	console.log("0");
	return;
} else if (nums.length === 1) {
	console.log("0");
	return;
} else {
	let max = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] > max) {
			max = nums[i]
		}
	}
	while (max >= 0) {
		const n = max - 1;
		if(nums.includes(n)) {
			console.log(n);
			return;
		}
		max -= 1;
	}
}
