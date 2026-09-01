# When Does Unpaired Structure Save Paired Supervision?

Public reproducibility repository for the course/preprint project on the value of paired supervision after pair-free structure has been extracted.

## Question

When unpaired observations reveal geometry within each modality, how much paired supervision is still needed for the task we actually care about, and when is it safe to trust structural advice?

The project separates three questions that are often conflated:

1. **Exact pair value under residual symmetry.** Which task-relevant directions remain ambiguous, and exactly how much does one additional correspondence remove?
2. **Imperfect structure.** How much paired variance is removed by structural regularization, and how much bias does misspecification introduce?
3. **Selective trust.** Can a small independent paired pilot certify HELP, HARM, practical NEUTRALITY, or insufficient evidence before we deploy the structural estimator?

## Course methods

The analysis uses PCA/SVD, Mahalanobis whitening, spectral/moment operators, CCA/Procrustes, RKHS/MMD, random subspaces/projections, and permutation/sign-flip inference. Each method is used for a specific data question rather than included for coverage alone.

## Main empirical message

The repository intentionally preserves positive, harmful, null, crossover, and failed-prospective evidence. Two separately sealed theorem-certificate studies are particularly important:

- **Sealed COCO theorem-certificate study:** six formal HELP calls, followed by six HELP outcomes on the theorem-aligned primary endpoint; all 120 repetition-level structural-minus-paired differences are negative.
- **Prospectively frozen Flickr30k selective challenge:** four formal HELP calls are followed by four HELP outcomes; two other conditions are formally UNCERTAIN and later reveal HARM.

A post-hoc decision audit applies the simple rule **deploy structure only after a HELP certificate; otherwise use paired-only**. Across the 12 conditions from those two separately sealed studies, the rule selects structure in 10 cases and paired-only in two; all 12 actions match the hindsight better estimator on the primary quadratic-risk endpoint. This is descriptive synthesis, not a preregistered pooled 12-condition trial, and it does not imply retrieval/R@10 safety.

## Repository layout

- `paper/` - the professional manuscript location; use `Paired_Data_Value_and_Unpaired_Structure.pdf` and `.tex` when uploading the final course paper.
- `code/` - compact verification and figure/audit scripts.
- `data/` - project-generated compact results and frozen study provenance summaries.
- `docs/` - method/data provenance and claim boundaries.

Reader-facing files and prose use descriptive scientific names rather than internal release numbers. Exact immutable protocol identifiers are kept only where auditability requires them; `data/study_provenance.csv` maps descriptive study names to the frozen records.

## Data policy

Project-generated compact CSV/JSON outputs, seeds, hashes, protocol records, and scripts belong in this repository. Large third-party datasets, pretrained checkpoints, and embedding caches are **not** copied into ordinary Git merely for completeness. Instead, the repository records public sources, immutable model revisions where available, hashes, and materialization instructions. Redistribution should follow the upstream licenses.

## Anonymity

This repository is author-identifying and is appropriate for the course/preprint. It should **not** be linked from a double-blind ICLR submission during review; an anonymous code snapshot should be used there.
