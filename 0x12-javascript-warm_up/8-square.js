#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      let line = '';
      for (let i = 0; i < num; i++) {
        line += 'X';
      }
      console.log(line);
    }
  } else {
    console.log('Missing size');
  }
}
