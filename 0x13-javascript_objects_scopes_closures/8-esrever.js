#!/usr/bin/node

exports.esrever = function (list) {
  let ret = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    ret.push(list[i]);
  }
  return ret;
};
