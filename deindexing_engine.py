#!/usr/bin/env python3
"""
Deindexing Automation Engine
Automation engine for managing search deindexing, content removal requests,
review issues, and online reputation workflows across major platforms.

https://deindexing.services
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_workflow(workflow: str) -> str:
    return " ".join(w.capitalize() for w in workflow.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "deindex": "Deindex",
        "removal_rate": "Removal Rate",
        "review_issue": "Review Issue",
        "reputation": "Reputation",
        "platform_coverage": "Platform Coverage",
        "workflow": "Workflow",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_platform_coverage(deindex: int, removal: int, review: int, workflow: int) -> dict:
    return {
        "Google Search": min(100, round(deindex * 1.0)),
        "Bing Search": min(100, round(removal * 1.0)),
        "Review Platforms": min(100, round(review * 1.0)),
        "Social Platforms": min(100, round(workflow * 1.0)),
    }


def run_deindexing_engine(
    brand: str,
    workflow: str = "search-deindex",
    deindex_score: int = 88,
    removal_rate: int = 82,
    review_issue_score: int = 85,
    reputation_score: int = 78,
    platform_coverage: int = 90,
    workflow_score: int = 84,
) -> dict:
    """
    Run the Deindexing Automation Engine across all workflow signals.

    Args:
        brand: Brand name or identifier
        workflow: Type of deindexing workflow to run
        deindex_score: Deindexing request strength score (0-100)
        removal_rate: Content removal approval and success rate (0-100)
        review_issue_score: Review dispute strength score (0-100)
        reputation_score: Online reputation health score (0-100)
        platform_coverage: Platform removal channel coverage (0-100)
        workflow_score: Automation workflow efficiency score (0-100)

    Returns:
        dict with individual workflow scores, overall automation index,
        and platform coverage breakdown
    """
    scores = {
        "deindex": deindex_score,
        "removal_rate": removal_rate,
        "review_issue": review_issue_score,
        "reputation": reputation_score,
        "platform_coverage": platform_coverage,
        "workflow": workflow_score,
    }
    overall_automation_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "workflow": format_workflow(workflow),
        "deindex_score": deindex_score,
        "removal_rate_score": removal_rate,
        "review_issue_score": review_issue_score,
        "reputation_score": reputation_score,
        "platform_coverage_score": platform_coverage,
        "workflow_score": workflow_score,
        "overall_automation_index": overall_automation_index,
        "priority_action": get_priority_action(scores),
        "platform_coverage": get_platform_coverage(deindex_score, removal_rate, review_issue_score, workflow_score),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    workflow = args[1] if len(args) > 1 else "search-deindex"
    deindex_score = int(args[2]) if len(args) > 2 else 88
    removal_rate = int(args[3]) if len(args) > 3 else 82
    review_issue_score = int(args[4]) if len(args) > 4 else 85
    reputation_score = int(args[5]) if len(args) > 5 else 78
    platform_coverage = int(args[6]) if len(args) > 6 else 90
    workflow_score = int(args[7]) if len(args) > 7 else 84

    result = run_deindexing_engine(
        brand, workflow, deindex_score, removal_rate,
        review_issue_score, reputation_score, platform_coverage, workflow_score
    )

    print(f"Brand: {result['brand']}")
    print(f"Workflow: {result['workflow']}")
    print("=" * 45)
    print(f"Deindex Score:                 {result['deindex_score']}/100  [{get_status(result['deindex_score'])}]")
    print(f"Removal Rate Score:            {result['removal_rate_score']}/100  [{get_status(result['removal_rate_score'])}]")
    print(f"Review Issue Score:            {result['review_issue_score']}/100  [{get_status(result['review_issue_score'])}]")
    print(f"Reputation Score:              {result['reputation_score']}/100  [{get_status(result['reputation_score'])}]")
    print(f"Platform Coverage Score:       {result['platform_coverage_score']}/100  [{get_status(result['platform_coverage_score'])}]")
    print(f"Workflow Score:                {result['workflow_score']}/100  [{get_status(result['workflow_score'])}]")
    print("=" * 45)
    print(f"Overall Automation Index:      {result['overall_automation_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nPlatform Coverage:")
    for platform, score in result['platform_coverage'].items():
        print(f"  {platform:<24} {score}/100")


if __name__ == "__main__":
    main()
