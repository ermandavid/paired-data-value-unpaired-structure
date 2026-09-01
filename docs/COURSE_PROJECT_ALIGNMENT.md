# Course project alignment

The course project asks for an individual 12-15 page data-analysis project using methods learned in class, with additional methods allowed when useful. It is graded on understanding of the data, appropriate mathematical/statistical method choice, and interesting non-trivial conclusions.

The submitted paper is designed around that rubric rather than treating the empirical section as an appendix to a theory paper.

## Data and goal

The project analyzes complementary controlled and natural representation data: two-view handwritten digits; public Flickr30k, MS COCO, and TextVQA representation panels; and prospectively frozen multi-encoder COCO/Flickr30k studies. The goal is to quantify how much paired supervision remains after pair-free structure is extracted and when that structure is safe to use.

Controlled data isolate mechanisms. Natural panels expose model mismatch, crossovers, null effects, harmful regimes, and data-quality failures. The paper therefore does not report only favorable examples.

## Course methods and why they are used

- **PCA/SVD:** dimension reduction, task spectra, and best low-rank residual structure.
- **Mahalanobis whitening:** covariance-aware normalization and reduction to an orthogonal residual ambiguity under the declared linear model.
- **Spectral/moment operators and diffusion-style geometry:** pair-free structure within each modality.
- **CCA and orthogonal Procrustes:** paired linear coupling and the natural paired-only residual-map baseline.
- **RKHS/MMD:** whether marginal distributions contain information about an unresolved alignment.
- **Random subspaces/projections:** how task utility changes when exposed directions are task-agnostic rather than task-aware.
- **Bootstrap, permutation, and sign-flip inference:** finite-sample uncertainty and repeated paired comparisons.

Additional Gaussian quadratic-risk calculations and Le Cam arguments are used only for the trust/certification question.

## Non-trivial conclusions

The project distinguishes map recovery from downstream utility, proves exact task-weighted pair value in the residual-symmetry model, quantifies the bias-variance value of imperfect structure, shows that pair-free data cannot universally determine whether structural advice helps or harms, and derives a pilot-based selective deployment rule. Empirically, the evidence includes gains, harmful regimes, null transfer, budget crossovers, a failed prospective heuristic, successful prospectively frozen HELP certificates, and consequential abstentions.

## Length and reproducibility

The course manuscript is exactly 15 pages including references. It contains the visible public-repository link:

https://github.com/ermandavid/paired-data-value-unpaired-structure

Scientific claims cite published papers, datasets, and model releases rather than course lecture notes or homework. The lecture material motivates the method choices; the bibliography supplies the scientific sources.