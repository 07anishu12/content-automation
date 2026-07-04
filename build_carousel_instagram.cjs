const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

(async () => {
    console.log("Generating HTML slides first...");
    execSync('python3 generate_carousel_instagram.py', { cwd: __dirname });

    const d = new Date().toISOString().slice(0, 10);
    const outDir = path.resolve(__dirname, `./carousel-routine/output/${d}/carousel-instagram`);
    fs.mkdirSync(outDir, { recursive: true });

    const config = require('./core/config/config.cjs');
    console.log("Launching Chrome using Puppeteer in headless mode with Keychain bypass...");
    const browser = await puppeteer.launch({
        executablePath: config.CHROME_PATH,
        headless: true,
        args: config.KEYCHAIN_ARGS
    });
    
    const page = await browser.newPage();
    // Instagram Portrait Viewport (1080 width x 1350 height)
    await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });

    // Process all 7 slides
    for (let i = 1; i <= 7; i++) {
        const slideHtml = path.resolve(__dirname, `./carousel-routine/temp/carousel-branded/slide${i}.html`);
        if (!fs.existsSync(slideHtml)) {
            console.log(`Warning: Slide HTML not found at ${slideHtml}`);
            continue;
        }
        
        console.log(`Capturing Slide ${i} (1080x1350 Portrait)...`);
        await page.goto(`file://${slideHtml}`, { waitUntil: 'networkidle0' });
        await page.screenshot({ path: `${outDir}/slide${i}.png` });
    }

    await browser.close();
    console.log(`Successfully compiled Instagram slides PNG assets to ${outDir}`);
})();
