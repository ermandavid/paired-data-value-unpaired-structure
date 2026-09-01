# Data and provenance

## What is versioned here

This public course repository versions the project-generated compact artifacts needed to understand and audit the course paper: summary CSV/JSON tables, study seals/hashes, lightweight reproduction scripts, and the manuscript source.

## What is not duplicated in ordinary Git

Large third-party datasets, pretrained model checkpoints, and embedding caches are not copied into this repository merely for completeness. The paper uses public datasets/model releases and reports the source, revision where available, row counts, and frozen hashes needed to identify the inputs. Redistribution remains subject to the upstream licenses.

## Reader-facing study names

The paper intentionally avoids internal development labels such as `V257b` or `V259`. Those strings are reproducibility identifiers, not scientific concepts. `data/study_provenance.csv` maps each reader-facing name to its exact frozen record.

## Prospective-study boundary

The COCO theorem-certificate and Flickr30k selective studies were frozen separately before their respective outcome reveals. The later 12-condition selective-deployment audit combines their already-frozen outputs only after both studies were complete. It is therefore a descriptive synthesis, not a preregistered pooled trial and not an independence claim.

## Statistical boundary

The exact finite-sample confidence guarantee is proved under the stated independent Gaussian linear-pilot model. Neural experiments are prospectively frozen model-transfer tests of the theorem-derived statistic. Their agreement does not convert the Gaussian assumption into a theorem about arbitrary neural embeddings.
