// Sample XML content
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

/// code for the browser
const parser = new DOMParser();
const xmlDoc = parser.parseFromString(xmlString, 'text/xml');

const items = xmlDoc.getElementsByTagName('item');
const extractedData = [];

console.log('items:', items)

for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const name = item.querySelector('name').textContent;
    const price = parseFloat(item.querySelector('price').textContent);
    extractedData.push({ name, price });
}

console.log("extractedData:", extractedData)