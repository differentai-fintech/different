import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const TARGET = path.resolve(__dirname, "..", "different._AIplatform_V4.0.html");

const raw = fs.readFileSync(TARGET, "utf8");
const m = raw.match(/const ALLOCATION_EMBEDDED_HTML_B64 = '([^']+)'/);
if (!m) throw new Error("B64 not found");
let h = Buffer.from(m[1], "base64").toString("utf8");
if (!h.includes("CRM onboarding wealth goals v1")) {
  console.log("Skip: onboarding marker missing");
  process.exit(0);
}

const pairs = [
  [
    "step2Subtitle:'Select the profile that best matches the client's investor DNA.'",
    "step2Subtitle:'Pick a risk persona and asset-type preferences (Cash, Equity, Fixed Income, Real Estate).' ",
  ],
  [
    "step2Subtitle:'选择最符合客户投资风格的风险画像。'",
    "step2Subtitle:'选择风险画像，并勾选资产类型偏好（现金、股票、固定收益、房地产）。'",
  ],
  [
    "step2Subtitle:'選擇最符合客戶投資風格的風險畫像。'",
    "step2Subtitle:'選擇風險畫像，並勾選資產類型偏好（現金、股票、固定收益、房地產）。'",
  ],
  [
    "step2Subtitle:'クライアントの投資DNAに最も合うプロファイルを選びます。'",
    "step2Subtitle:'リスクプロファイルと資産クラス嗜好（Cash / Equity / FI / RE）を選びます。'",
  ],
];

let n = 0;
for (const [a, b] of pairs) {
  if (h.includes(a)) {
    h = h.replace(a, b);
    n++;
  }
}
if (!n) {
  console.log("No subtitle replacements applied");
  process.exit(0);
}
const b64 = Buffer.from(h, "utf8").toString("base64");
const out = raw.replace(/const ALLOCATION_EMBEDDED_HTML_B64 = '[^']+'/, `const ALLOCATION_EMBEDDED_HTML_B64 = '${b64}'`);
fs.writeFileSync(TARGET, out, "utf8");
console.log("Updated step2Subtitle in", n, "locales");
