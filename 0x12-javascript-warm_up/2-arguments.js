#!/usr/bin/node
const arguement = process.argv;
if (arguement.length === 2) {
  console.log('No argument');
} else if (arguement.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
