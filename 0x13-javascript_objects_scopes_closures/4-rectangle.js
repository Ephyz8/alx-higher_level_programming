#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let t = '';
        for (let j = 0; j < this.width; j++) {
          t += 'X';
        }
        console.log(t);
      }
    }
  
    rotate () {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  
    double () {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
  module.exports = Rectangle;