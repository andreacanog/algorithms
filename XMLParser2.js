const xml2js = require('xml2js');

const xmlString = `<root>
    <item>
        <name>Item 1</name>
        <price>10.99</price>
    </item>
    <item>
        <name>Item 2</name>
        <price>20.49</price>
    </item>
</root>`;

// Parse the XML string using xml2js
xml2js.parseString(xmlString, (err, result) => {
    if (err) {
        console.error('Error parsing XML:', err);
        return;
    }
    // console.log("result:", result)
    const items = result.root.item;
    // console.log("items:", items)

    const extractedData = items.map((item) => ({
        name: item.name[0],
        price: parseFloat(item.price[0])
    }));

    return extractedData

    console.log('Extracted Data:', extractedData);
});


//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

const xml2js = require('xml2js');
const fs = require('fs'); // Only for Node.js environment

// Read the XML file (for Node.js environment)
const xmlData = fs.readFileSync('yourfile.xml', 'utf-8');

// Parse the XML using xml2js
xml2js.parseString(xmlData, (err, result) => {
  if (err) {
    console.error('Error parsing XML:', err);
    return;
  }

 // Use the extracted information as needed

    const items = result.root.item;
    console.log("items:", items)

    const extractedData = items.map((item) => ({
        name: item.name[0],
        price: parseFloat(item.price[0])
    }));

    console.log('Extracted Data:', extractedData);
});
