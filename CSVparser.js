// // const fs = require('fs');
import fs from 'fs'

// Example usage:

function csvParser(file_path) {
  return new Promise((resolve, reject) => {
    // Read the CSV file
    fs.readFile(file_path, 'utf-8', (err, data) => {
      if (err) {
        console.error('Error reading the CSV file:', err);
        reject(err);
        return;
      }

      // Split the CSV data into rows
      const rows = data.split('\n');

      // Extract column headers from the first row
      const headers = rows[0].trim().split(',');

      // Initialize an array to store the objects
      const csvData = [];

      // Process each row starting from the second row (index 1)
      for (let i = 1; i < rows.length; i++) {
        const values = rows[i].split(',');
        const rowObject = {};

        // Populate the object with values
        for (let j = 0; j < headers.length; j++) {
          rowObject[headers[j].toString()] = values[j].trim();
        }

        csvData.push(rowObject);
      }

      // Resolve the Promise with the parsed data
      resolve(csvData);
    });
  });
}

// Example usage with async/await


export default csvParser;
csvParser('Leetcode1.csv')
//--------------------------------------------------------------------

// Sample CSV data as a string
// const csvData = `
// 1,Name,Age,Email
// 2,John,30,john@example.com
// 3,Alice,25,alice@example.com
// 4,Bob,35,bob@example.com
// `;

// // Function to parse CSV data and convert it into an array of objects
// function parseCSV(csv) {
//   const lines = csv.trim().split('\n');
//   const headers = lines[0].split(',').slice(1);

//   const data = [];


//   for (let i = 1; i < lines.length; i++) {
//     const values = lines[i].split(',').slice(1);
//     const row = {};

//     for (let j = 0; j < headers.length; j++) {
//       row[headers[j]] = values[j].trim();
//     }

//     data.push(row);
//   }
//   // console.log("data: ",data)
//   return data;
// }

// // Parse the CSV data
// const csvObjects = parseCSV(csvData);

// // Display the data on the UI (for example, in the console)
// csvObjects.forEach((row) => {
//   console.log(row);
// });

// export default parseCSV;


//----------------------------------------------------------------------------------------------------------------------------------------


function csvParser(file_path) {
  var data = fs.readFileSync(file_path, 'utf-8')
  
    // Split the CSV data into rows
    const rows = data.split('\n');
  
    // Extract column headers from the first row
    const headers = rows[0].trim().split(',');
  
    // Initialize an array to store the objects
    const csvData = [];
  
    // Process each row starting from the second row (index 1)
    for (let i = 1; i < rows.length; i++) {
      const values = rows[i].split(',');
      const rowObject = {};
  
      // Populate the object with values
      for (let j = 0; j < headers.length; j++) {
        rowObject[headers[j].toString()] = values[j].trim();
      }
  
      csvData.push(rowObject);
    }
    data = csvData

  return data;
}

// export default csvParser;