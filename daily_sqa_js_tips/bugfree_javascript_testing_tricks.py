// Define a function and test it using assertions
function add(a, b) {
    return a + b;
}

// Simple assertion to check if the function works correctly
console.assert(add(2, 3) === 5, 'Test for add(2, 3) failed!');
console.assert(add(-1, 1) === 0, 'Test for add(-1, 1) failed!');
console.assert(add(0, 0) === 0, 'Test for add(0, 0) failed!');