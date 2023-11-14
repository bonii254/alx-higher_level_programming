#!/usr/bin/node
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    const result = num * factorial(num - 1);
    return result;
  }
}

const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
