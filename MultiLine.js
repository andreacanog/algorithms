// // Sample multi-line string with comma-separated data
// const multiLineString = `
//     A,1,X
//     A,2,Y
//     B,3,Z
//     A,1,Z
//     B,4,W
// `;

// // Initialize an empty root node
// const root = {};

// // Helper function to build the tree
// function buildTree(node, path, value) {
//     // Split the path into individual segments
//     const segments = path.split(',');
//     console.log("segments: ", segments)

//     // Traverse the tree based on the path
//     for (const segment of segments) {
//         node[segment] = node[segment] || {};
//         node = node[segment];
//     }

//     // Assign the value to the final node
//     node.value = value;
// }

// // Split the multi-line string into lines
// const lines = multiLineString.trim().split('\n');
// console.log("lines: ", lines)

// // Parse and build the tree
// lines.forEach((line) => {
//     const [path, value] = line.trim().split(',');
//     console.log("path: ", path, "value: ", value)
//     buildTree(root, path, value);
// });

// // The 'root' object now represents the tree structure
// console.log(JSON.stringify(root, null, 2));


// Sample multi-line string with comma-separated data

const multiLineString = `
    IT,John
    Engineering,Robert
    IT,Emily
    Engineering,Alice
    HR,Michael
    IT,David
    HR,Susan
`;

// // Initialize the root node
export const root = { name: 'Root', children: [] };

// Helper function to find or create a department node
function findOrCreateDepartmentNode(parentNode, departmentName) {
    const existingDepartment = parentNode.children.find(node => node.name === departmentName);

    if (existingDepartment) {
        return existingDepartment;
    } else {
        const newDepartment = { name: departmentName, children: [] };
        parentNode.children.push(newDepartment);
        return newDepartment;
    }
}


// Split the multi-line string into lines
const generateRoot = () => {
    const lines = multiLineString.trim().split('\n');
    
    // Parse and build the tree
    lines.forEach((line) => {
        const [department, employee] = line.trim().split(',');
        const departmentNode = findOrCreateDepartmentNode(root, department);
        departmentNode.children.push({ name: employee });
    });

    return root;
    
    // The 'root' object now represents the hierarchical tree structure
    // console.log(JSON.stringify(root, null, 2));
}

export default generateRoot;
// export default findOrCreateDepartmentNode;


