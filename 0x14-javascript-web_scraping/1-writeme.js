#!/usr/bin/node
// writes to a file
let fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) throw err;
});
