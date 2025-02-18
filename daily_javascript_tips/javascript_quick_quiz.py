// Let's compare some values using == and === operator
console.log(1 == '1');   // true - because == compares values with type coercion
console.log(1 === '1');  // false - because === compares both value and type
console.log(0 == false); // true - because == converts false to 0
console.log(0 === false);// false - because === keeps types intact
console.log(null == undefined); // true - special case for ==
console.log(null === undefined); // false - different types!