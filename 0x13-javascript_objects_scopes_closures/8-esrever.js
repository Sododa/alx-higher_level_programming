#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let a = list.length - 1; a >= 0; a--) {
    newlist.push(list[a]);
  }
  return newlist;
};
