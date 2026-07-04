const fs = require('fs');
const path = require('path');

function loadEnv(envPath = path.resolve(__dirname, '../../.env')) {
    const envVars = {};
    if (fs.existsSync(envPath)) {
        const content = fs.readFileSync(envPath, 'utf8');
        content.split('\n').forEach(line => {
            const trimmed = line.strip ? line.strip() : line.trim();
            if (trimmed.indexOf('=') !== -1 && !trimmed.startsWith('#')) {
                const parts = trimmed.split('=');
                const key = parts[0].trim();
                const val = parts.slice(1).join('=').trim();
                envVars[key] = val;
            }
        });
    }
    return envVars;
}

const env = loadEnv();

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const DEFAULT_VIEWPORT = { width: 1080, height: 1080, deviceScaleFactor: 2 };
const KEYCHAIN_ARGS = [
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-gpu',
    '--disable-dev-shm-usage',
    '--use-mock-keychain',
    '--password-store=basic',
    '--disable-extensions',
    '--disable-component-update',
    '--no-default-browser-check'
];

module.exports = {
    SLACK_BOT_TOKEN: env.SLACK_BOT_TOKEN || process.env.SLACK_BOT_TOKEN,
    APIFY_API_KEY: env.APIFY_API_KEY || process.env.APIFY_API_KEY,
    OPENROUTER_API_KEY: env.OPENROUTER_API_KEY || process.env.OPENROUTER_API_KEY,
    SLACK_CHANNEL: "C0AVBBTD529",
    CHROME_PATH,
    DEFAULT_VIEWPORT,
    KEYCHAIN_ARGS
};
