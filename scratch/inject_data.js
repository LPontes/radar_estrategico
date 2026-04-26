const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'dashboard_data.json');

const htmlFiles = [
    path.join(__dirname, '..', 'presentation', 'ra-03-funnel.html')
];

const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

htmlFiles.forEach(htmlPath => {
    if (!fs.existsSync(htmlPath)) {
        console.warn(`File ${htmlPath} not found, skipping.`);
        return;
    }
    let html = fs.readFileSync(htmlPath, 'utf8');
    const rawDataString = `const rawData = ${JSON.stringify(data, null, 2)};`;
    const regex = /const rawData = \{[\s\S]*?\};/;
    if (regex.test(html)) {
        html = html.replace(regex, rawDataString);
        fs.writeFileSync(htmlPath, html, 'utf8');
        console.log(`Successfully injected data into ${path.basename(htmlPath)}`);
    } else {
        console.error(`Could not find rawData block in ${path.basename(htmlPath)}`);
    }
});
