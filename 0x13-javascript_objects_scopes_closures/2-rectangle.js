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
};
