#!/usr/bin/node

function add (a, b) {
  const aNum = parseInt(a);
  const bNum = parseInt(b);
  return aNum + bNum;
}

console.log(add(process.argv[2], process.argv[3]));
