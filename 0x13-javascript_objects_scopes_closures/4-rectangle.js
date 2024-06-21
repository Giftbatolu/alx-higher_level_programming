#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (this.isvalid(w) && this.isvalid(h)) {
      this.width = w;
      this.height = h;
    }
  }

  isvalid (value) {
    return (Number.isInteger(value) && value > 0);
  }

  print () {
    let b, d, pattern;

    for (b = 0; b < this.height; b++) {
      pattern = '';
      for (d = 0; d < this.width; d++) {
        pattern += 'X';
      }
      console.log(pattern);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
