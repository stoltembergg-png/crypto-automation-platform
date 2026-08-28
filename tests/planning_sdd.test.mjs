import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const read = (p) => fs.readFileSync(path.join(root, p), 'utf8');
const exists = (p) => fs.existsSync(path.join(root, p));
const report = JSON.parse(read('.planning/master/PLANNING_INTEGRITY_REPORT.json'));

test('@spec:AC-001 @principle:P-001 canonical planning inventory exists', () => {
  assert.equal(report.status, 'PASS');
  assert.equal(report.missing.length, 0);
  assert.ok(report.required_files >= 82);
});

test('@spec:AC-002 fifteen ADR decisions are present', () => {
  const files = fs.readdirSync(path.join(root, 'docs/adrs')).filter((x) => x.endsWith('.md'));
  assert.equal(files.length, 15);
  assert.match(read('docs/adrs/ADR-003-modular-monolith-vs-microservices.md'), /modular monolith/i);
  assert.ok(read('docs/adrs/ADR-005-internal-ledger.md').includes('double-entry'));
});

test('@spec:AC-003 architecture diagrams and contracts are complete', () => {
  const diagrams = fs.readdirSync(path.join(root, 'docs/architecture/diagrams')).filter((x) => x.endsWith('.mmd'));
  const contracts = fs.readdirSync(path.join(root, '.planning/contracts')).filter((x) => x.endsWith('.md'));
  assert.ok(diagrams.length >= 11);
  assert.ok(contracts.length >= 10);
});

test('@spec:AC-004 implementation cards contain every required field', () => {
  const cards = JSON.parse(read('.planning/queue/queue.json'));
  const md = read('.planning/queue/PR_CARDS.md');
  assert.equal(cards.length, 141);
  for (const label of ['Objective:', 'Scope:', 'Files:', 'Dependencies:', 'Implementation:', 'Tests:', 'Acceptance criteria:', 'Security implications:', 'Observability:', 'Rollback:', 'Definition of done:']) assert.equal((md.match(new RegExp(label, 'g')) || []).length, 141, label);
});

test('@spec:AC-005 @principle:P-005 queue DAG is acyclic', () => {
  assert.equal(report.dag_acyclic, true);
  assert.ok(read('.planning/queue/QUEUE_INDEX.md').includes('Critical path'));
});

test('@spec:AC-006 traceability covers every normalized mandate group', () => {
  assert.equal(report.traceability_rows, 68);
  const rows = read('.planning/master/TRACEABILITY_MATRIX.md').split('\n').filter((x) => x.startsWith('| USR-'));
  assert.equal(rows.length, 68);
});

test('@spec:AC-007 @principle:P-002 mainnet is explicitly blocked', () => {
  assert.equal(report.mainnet, 'BLOCKED');
  assert.ok(read('.planning/master/MAINNET_READINESS_MATRIX.md').includes('MAINNET = BLOCKED'));
});

test('@spec:AC-008 @principle:P-003 no financial runtime roots exist in planning baseline', () => {
  for (const forbidden of ['src', 'apps', 'crates', 'infra']) assert.equal(exists(forbidden), false, forbidden);
});

test('@spec:AC-009 integrity report limits its own claim', () => {
  assert.match(report.note, /documented topology/i);
  assert.equal(report.status, 'PASS');
  assert.notEqual(report.mainnet, 'PASS');
});

test('@spec:AC-010 @principle:P-004 planning artifacts contain no token-shaped secret', () => {
  const walk = (dir) => fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => entry.isDirectory() ? walk(path.join(dir, entry.name)) : [path.join(dir, entry.name)]);
  const files = ['docs', '.planning', '.spec', 'tests'].flatMap((p) => walk(path.join(root, p))).filter((p) => /\.(md|mmd|json|js|mjs|py|ya?ml)$/i.test(p));
  const secretPattern = /(gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AIza[A-Za-z0-9_-]{20,}|0x[a-fA-F0-9]{64})/;
  for (const file of files) assert.equal(secretPattern.test(fs.readFileSync(file, 'utf8')), false, file);
});

test('@spec:AC-011 develop page is status-only and does not imply a financial runtime', () => {
  const page = read('develop/index.html');
  const config = read('vercel.json');
  for (const marker of ['PLANNING BASELINE', '141', '68', 'MAINNET BLOCKED']) assert.ok(page.includes(marker), marker);
  assert.equal(/<form|<script\b|https?:\/\//i.test(page), false);
  assert.ok(config.includes('"/develop"'));
});
