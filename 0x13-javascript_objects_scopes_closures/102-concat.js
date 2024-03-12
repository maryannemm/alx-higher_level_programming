#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
    console.error('Usage: ./102-concat.js <file1> <file2> <output_file>');
    process.exit(1);
}

const file1 = args[0];
const file2 = args[1];
const outputFile = args[2];

try {
    // Read content from file1
    const content1 = fs.readFileSync(file1, 'utf8');

    // Read content from file2
    const content2 = fs.readFileSync(file2, 'utf8');

    // Concatenate content from both files
    const concatenatedContent = content1 + '\n' + content2;

    // Write concatenated content to output_file
    fs.writeFileSync(outputFile, concatenatedContent);

    console.log(`Files ${file1} and ${file2} are successfully concatenated to ${outputFile}`);
} catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
}

