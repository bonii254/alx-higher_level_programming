#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}
