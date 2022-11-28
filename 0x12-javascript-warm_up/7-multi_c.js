#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
