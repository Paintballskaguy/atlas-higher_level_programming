#!/usr/bin/node

exports.nb0ccurences = function (list, searchElement) {
  return list.reduce((count, element) => {
    return element === searchElement ? count + 1 : count;
  }, 0);
};
