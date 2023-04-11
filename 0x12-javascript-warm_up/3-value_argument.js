#!/usr/bin/node
import { argv } from 'node:process';

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
