#!/usr/bin/node
const dict = require('./101-data').dict;

const tlist = Object.entries(dict);
const val = Object.values(dict);
const valUni = [...new Set(val)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in tlist) {
    if (tlist[k][1] === valsUniq[j]) {
      list.unshift(tlist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);