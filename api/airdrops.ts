// backend/api/airdrops.ts

import { readFileSync } from "fs";
import path from "path";

export async function GET() {
  const filePath = path.resolve("backend/data/airdrops.json");
  const data = JSON.parse(readFileSync(filePath, "utf-8"));
  return new Response(JSON.stringify(data), {
    headers: { "Content-Type": "application/json" },
  });
}
