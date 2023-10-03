import generateRoot from './MultiLine.js';
import csvParser from './CSVparser.js';
import parseCSV from './CSVparser.js';

// const csvData = `
// 1,Name,Age,Email
// 2,John,30,john@example.com
// 3,Alice,25,alice@example.com
// 4,Bob,35,bob@example.com
// `;


// const parse = parseCSV(csvData);
// console.log("parse: ", parse)

const multiLineString = `
    IT,John
    Engineering,Robert
    IT,Emily
    Engineering,Alice
    HR,Michael
    IT,David
    HR,Susan
`;

// export const root = { name: 'Root', children: [] };

// const newRoot = generateRoot()
// console.log("newRoot: ", newRoot)
// console.log(JSON.stringify(newRoot, null, 2));
// console.log(JSON.stringify(newRoot, null, 1));


// csvParser('data.csv', (err, data) => {
//     if (err) {
//       // Handle the error
//       console.error('Error:', err);
//     } else {
//       // Use the parsed data
//       // console.log(data);
//       return data
//     }
//   });




// let data; 
async function readCSV() {
  try {
    const csv = await csvParser('Leetcode1.csv');

    return csv;
  } catch (err) {
    // Handle errors here
    console.error('Error:', err);
  }
}

// const data = await readCSV();
console.log("await csv: ", await readCSV());
// console.log("stringify data: ", JSON.stringify(data, null, 1));


// const data = csvParser('Leetcode1.csv')
// console.log("data: ",  data)