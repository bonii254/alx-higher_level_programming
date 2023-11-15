#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occour = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occour += 1;
    }
  }
  return occour;
};
