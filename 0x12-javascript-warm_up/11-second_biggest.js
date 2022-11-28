#!/usr/bin/node

const nums = [];

for (let i = 0; i < process.argv.length; i++) {
  const n = parseInt(process.argv[i]);
  if (!isNaN(n)) {
    nums.push(n);
  }
}
if (nums.length === 0) {
  console.log('0');
} else if (nums.length === 1) {
  console.log('0');
} else {
  let max = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
  }
  while (max >= 0) {
    const n = max - 1;
    if (nums.includes(n)) {
      console.log(n);
    }
    max -= 1;
  }
}
