import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import YAML from 'yaml';

const root = process.cwd();
const required = ['myst.yml', 'index.md', '.github/workflows/ci.yml', '.github/workflows/deploy.yml'];
const missing = required.filter((file) => !fs.existsSync(path.join(root, file)));
if (missing.length) throw new Error(`Missing required files: ${missing.join(', ')}`);

const config = YAML.parse(fs.readFileSync(path.join(root, 'myst.yml'), 'utf8'));
const errors = [];
if (!config.project?.title) errors.push('project.title is required');
if (!config.project?.short_title) errors.push('project.short_title is required');
if (config.project?.open_access !== true) errors.push('project.open_access must be true');
if (!config.project?.github) errors.push('project.github is required');
if (!Array.isArray(config.project?.toc) || !config.project.toc.length) errors.push('project.toc must contain at least one page');

const experimentDir = path.join(root, 'experiments');
const experimentFiles = fs.readdirSync(experimentDir)
  .filter((file) => file.endsWith('.md'))
  .sort();

for (const file of experimentFiles) {
  const sourcePath = path.join(experimentDir, file);
  const source = fs.readFileSync(sourcePath, 'utf8');
  const figures = [...source.matchAll(/```\{figure\}\s+([^\n]+)\n([\s\S]*?)\n```/g)];

  if (figures.length !== 2) {
    errors.push(`${file} must contain exactly two figures (theory and apparatus); found ${figures.length}`);
  }

  for (const [, relativeImage, body] of figures) {
    const imagePath = path.resolve(experimentDir, relativeImage.trim());
    const displayPath = path.relative(root, imagePath);
    if (!fs.existsSync(imagePath)) {
      errors.push(`${file} references missing figure ${displayPath}`);
      continue;
    }
    if (!/:label:\s+\S/.test(body)) errors.push(`${file}: ${displayPath} needs a figure label`);
    if (!/:alt:\s+\S/.test(body)) errors.push(`${file}: ${displayPath} needs useful alt text`);

    const caption = body
      .split('\n')
      .filter((line) => !line.startsWith(':'))
      .join(' ')
      .trim();
    if (caption.length < 40) errors.push(`${file}: ${displayPath} needs an explanatory caption`);

    if (path.extname(imagePath).toLowerCase() === '.svg') {
      const svg = fs.readFileSync(imagePath, 'utf8');
      if (!/<svg\b/.test(svg) || !/\bviewBox=/.test(svg)) {
        errors.push(`${displayPath} is not a scalable, renderable SVG`);
      }
    }
  }
}

if (errors.length) throw new Error(errors.join('\n'));

console.log(`Book structure, MyST metadata, and ${experimentFiles.length * 2} experiment figures are valid.`);
