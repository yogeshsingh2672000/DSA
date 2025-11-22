// map polyfill
const arr = [1, 2, 3, 4, 5];

Array.prototype.mymap = function (callback) {
  if (callback && typeof callback !== "function")
    throw new TypeError(`${callback} is not a function`);
  const result = [];
  // this is the array on which mymap is called
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};

const newArr = arr.mymap((num) => num * 2);
console.log(newArr); // [2,4,6,8,10]

// filter polyfill
Array.prototype.myfilter = function (cb) {
  if (cb && typeof cb !== "function")
    throw new TypeError(`${cb} is not a function`);
  const result = [];
  // this is the array on which myfilter is called
  for (let i = 0; i < this.length; i++) {
    if (cb(this[i], i, this)) {
      result.push(this[i]);
    }
  }
  return result;
};

const filteredArr = arr.myfilter((num) => num % 2 === 0);
console.log(filteredArr); // [2,4]
