#!/usr/bin/env python3
"""Reproduce the compact 12-condition selective-deployment audit.

This script uses only project-generated summary data. It does not rerun the underlying
COCO/Flickr embedding experiments. The two studies were sealed separately; their
combined decision audit is descriptive rather than a preregistered pooled trial.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "selective_deployment_audit.csv"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)


def main() -> None:
    df = pd.read_csv(DATA)

    # epsilon = 0 policy used in the descriptive audit.
    expected_action = df["upper"].map(lambda u: "STRUCTURE" if u < 0 else "PAIRED_ONLY")
    assert (expected_action == df["policy_action"]).all()

    oracle = df["heldout"].map(lambda d: "STRUCTURE" if d < 0 else "PAIRED_ONLY")
    assert (oracle == df["oracle_action"]).all()

    regret = df.apply(
        lambda r: 0.0 if r.policy_action == r.oracle_action else abs(float(r.heldout)),
        axis=1,
    )
    assert (regret == df["observed_decision_regret"]).all()

    # Coverage-event opportunity-cost bound at epsilon=0.
    assert (df["observed_decision_regret"] <= df["interval_width"] + 1e-12).all()

    print(f"conditions={len(df)}")
    print(f"deploy_structure={(df.policy_action == 'STRUCTURE').sum()}")
    print(f"fallback_to_paired={(df.policy_action == 'PAIRED_ONLY').sum()}")
    print(f"observed_zero_regret={(df.observed_decision_regret == 0).sum()}/{len(df)}")

    fig, ax = plt.subplots(figsize=(7.3, 4.8))
    for _, r in df.iterrows():
        marker = "o" if r.policy_action == "STRUCTURE" else "x"
        ax.scatter(r.upper, r.heldout, marker=marker, s=46)
        ax.annotate(r.condition, (r.upper, r.heldout), xytext=(4, 4),
                    textcoords="offset points", fontsize=7)
    ax.axvline(0, linewidth=1)
    ax.axhline(0, linewidth=1)
    ax.set_xlabel("Frozen certificate upper endpoint")
    ax.set_ylabel("Later structural - paired primary risk")
    ax.set_title("Selective deployment across two separately sealed studies")
    fig.tight_layout()
    fig.savefig(OUT / "selective_deployment_audit.pdf", bbox_inches="tight")
    fig.savefig(OUT / "selective_deployment_audit.png", dpi=180, bbox_inches="tight")
    print(f"wrote {OUT / 'selective_deployment_audit.pdf'}")


if __name__ == "__main__":
    main()
