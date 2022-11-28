#!/usr/bin/node

function factorial (num) {
  const n = parseInt(num);
  if (!isNaN(n)) {
    if (n < 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  } else {
    return 1;
  }
}

console.log(factorial(process.argv[2]));
