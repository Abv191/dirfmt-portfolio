#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

function generateReadme(dir) {
  dir = path.resolve(dir);
  const pkgPath = path.join(dir, "package.json");
  let pkg = {};

  try {
    pkg = JSON.parse(fs.readFileSync(pkgPath, "utf-8"));
  } catch (_) {
    pkg = { name: path.basename(dir), version: "0.0.0" };
  }

  const readmePath = path.join(dir, "README.md");
  if (fs.existsSync(readmePath)) {
    const existing = fs.readFileSync(readmePath, "utf-8");
    if (existing.includes("<!-- readmegen -->")) {
      console.log("README.md already contains readmegen marker. Use --overwrite to replace.");
      process.exit(1);
    }
  }

  const lines = [];
  lines.push(`# ${pkg.name || path.basename(dir)}`);
  lines.push("");
  if (pkg.description) {
    lines.push(pkg.description);
    lines.push("");
  }

  if (pkg.version) {
    lines.push(`![Version](https://img.shields.io/badge/version-${pkg.version}-blue)`);
    lines.push("");
  }

  const badgeParts = [];
  if (pkg.license) badgeParts.push(`![License](https://img.shields.io/badge/license-${pkg.license}-green)`);
  if (pkg.dependencies && Object.keys(pkg.dependencies).length > 0) {
    badgeParts.push(`![Dependencies](https://img.shields.io/badge/dependencies-${Object.keys(pkg.dependencies).length}-orange)`);
  }
  if (badgeParts.length > 0) {
    lines.push(...badgeParts);
    lines.push("");
  }

  lines.push("<!-- readmegen -->");
  lines.push("");

  lines.push("## Installation");
  lines.push("");
  lines.push(`\`\`\`bash`);
  lines.push(`npm install ${pkg.name}`);
  lines.push(`\`\`\``);
  lines.push("");

  const readmeContent = lines.join("\n");

  if (fs.existsSync(readmePath)) {
    const existing = fs.readFileSync(readmePath, "utf-8");
    const updated = existing + "\n\n" + readmeContent;
    fs.writeFileSync(readmePath, updated);
    console.log(`Updated README.md in ${dir}`);
  } else {
    fs.writeFileSync(readmePath, readmeContent);
    console.log(`Created README.md in ${dir}`);
  }
}

const args = process.argv.slice(2);
const flags = new Set();
const positional = [];

for (const arg of args) {
  if (arg.startsWith("--")) {
    flags.add(arg.replace(/^--/, ""));
  } else {
    positional.push(arg);
  }
}

const targetDir = positional[0] || ".";
generateReadme(targetDir);

module.exports = { generateReadme };