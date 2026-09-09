#!/usr/bin/env node

interface DeindexingInput {
  brand: string;
  workflow: string;
  deindexScore: number;
  removalRate: number;
  reviewIssueScore: number;
  reputationScore: number;
  platformCoverage: number;
  workflowScore: number;
}

interface DeindexingOutput {
  brand: string;
  workflow: string;
  deindexScore: number;
  removalRateScore: number;
  reviewIssueScore: number;
  reputationScore: number;
  platformCoverageScore: number;
  workflowScore: number;
  overallAutomationIndex: number;
  priorityAction: string;
  platformCoverage: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatWorkflow(workflow: string): string {
  return workflow.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    deindex: "Deindex",
    removalRate: "Removal Rate",
    reviewIssue: "Review Issue",
    reputation: "Reputation",
    platformCoverage: "Platform Coverage",
    workflow: "Workflow",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getPlatformCoverage(deindex: number, removal: number, review: number, workflow: number): Record<string, number> {
  return {
    "Google Search": Math.min(100, Math.round(deindex * 1.0)),
    "Bing Search": Math.min(100, Math.round(removal * 1.0)),
    "Review Platforms": Math.min(100, Math.round(review * 1.0)),
    "Social Platforms": Math.min(100, Math.round(workflow * 1.0)),
  };
}

export function runDeindexingEngine(input: DeindexingInput): DeindexingOutput {
  const scores = {
    deindex: input.deindexScore,
    removalRate: input.removalRate,
    reviewIssue: input.reviewIssueScore,
    reputation: input.reputationScore,
    platformCoverage: input.platformCoverage,
    workflow: input.workflowScore,
  };
  const overallAutomationIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    workflow: formatWorkflow(input.workflow),
    deindexScore: input.deindexScore,
    removalRateScore: input.removalRate,
    reviewIssueScore: input.reviewIssueScore,
    reputationScore: input.reputationScore,
    platformCoverageScore: input.platformCoverage,
    workflowScore: input.workflowScore,
    overallAutomationIndex,
    priorityAction: getPriorityAction(scores),
    platformCoverage: getPlatformCoverage(input.deindexScore, input.removalRate, input.reviewIssueScore, input.workflowScore),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const workflow = args[1] || "search-deindex";
const deindexScore = parseInt(args[2]) || 88;
const removalRate = parseInt(args[3]) || 82;
const reviewIssueScore = parseInt(args[4]) || 85;
const reputationScore = parseInt(args[5]) || 78;
const platformCoverage = parseInt(args[6]) || 90;
const workflowScore = parseInt(args[7]) || 84;

const result = runDeindexingEngine({
  brand, workflow, deindexScore, removalRate,
  reviewIssueScore, reputationScore, platformCoverage, workflowScore,
});

console.log(`Brand: ${result.brand}`);
console.log(`Workflow: ${result.workflow}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Deindex Score:                 ${result.deindexScore}/100  [${getStatus(result.deindexScore)}]`);
console.log(`Removal Rate Score:            ${result.removalRateScore}/100  [${getStatus(result.removalRateScore)}]`);
console.log(`Review Issue Score:            ${result.reviewIssueScore}/100  [${getStatus(result.reviewIssueScore)}]`);
console.log(`Reputation Score:              ${result.reputationScore}/100  [${getStatus(result.reputationScore)}]`);
console.log(`Platform Coverage Score:       ${result.platformCoverageScore}/100  [${getStatus(result.platformCoverageScore)}]`);
console.log(`Workflow Score:                ${result.workflowScore}/100  [${getStatus(result.workflowScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Automation Index:      ${result.overallAutomationIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nPlatform Coverage:");
Object.entries(result.platformCoverage).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(22)} ${score}/100`);
});
