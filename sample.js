// Given input string
function parse(StrRates) {
    // Split the input string into rows using ':' as the delimiter
    var rows = StrRates.split(';');
    // rows.split(';')
    console.log('rows:', rows)
    // Initialize an empty two-dimensional matrix
    var matrix = [];

    // Iterate over each row
    for (var i = 0; i < rows.length; i++) {
    // Split the row into values using ',' as the delimiter
    var values = rows[i].split(',');

    // Add the values to the matrix
    matrix.push(values);
    }

    // Determine the number of rows and columns
    var numRows = matrix.length;
    var numCols = matrix[0].length;

    
 return matrix;
}
var StrRates = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;";

console.log(parse(StrRates))


// var StrRates = "5.0, 100, 5.5, 101, 6.0, 102:L10, 5.0, 99, 5.5, 100, 6.0, 101:L20";
// var re = /[L]\d+/g;

// var locks = StrRates.match(re)[0].split("L");
// var rates = Array.from(new Set(StrRates.match(/\d+\.\d+/g).map(parseFloat))).sort((a, b) => a - b);

// var strTrimmed = StrRates.replace(":", ",").split(",");

// var prices = [];

// for (var x = 0; x < strTrimmed.length; x++) {
//   if (!isNaN(strTrimmed[x])) {
//     prices.push(strTrimmed[x]);
//   }
// }

// var matrix = [locks];

// for (var i = 0; i < locks.length; i++) {
//   var row = Array(locks.length).fill("");
//   row[0] = rates[i];
//   matrix.push(row);
// }

// for (var i = 1; i < matrix.length; i++) {
//   var idx = i - 1;
//   for (var j = 1; j < matrix[i].length; j++) {
//     matrix[i][j] = prices[idx];
//     idx += rates.length;
//   }
// }

// for (var x = 0; x < matrix.length; x++) {
//   console.log(matrix[x]);
// }
