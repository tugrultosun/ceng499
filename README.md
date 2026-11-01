# CENG 499 — Introduction to machine learning

Homeworks 2–4 for **CENG 499 Introduction to Machine Learning** at METU, in **Python** with NumPy, Matplotlib
and scikit-learn. Homeworks 2 and 3 come with a LaTeX report (`report.tex` / `report.pdf`) and the plots it
uses.

## Homework 2 — kNN and clustering (`hw2/`)

| File | What it does |
|---|---|
| `hw2_data/knn.py` | **k-nearest neighbours**: picks k from 1–199 with 10-fold cross-validation, plots the accuracies, then tests the best k |
| `hw2_data/kmeans.py` | **k-means**: plots the average objective over 10 restarts for k = 1–10 (elbow method) and draws the chosen clustering |
| `hw2_data/hac.py` | **hierarchical agglomerative clustering** with single, complete, average and centroid linkage |

Plots are in `clustering_images/` and `hac_images/`; `README.txt` explains how to call each function.

## Homework 3 — Decision trees and SVMs (`hw3/`)

The work is in `hw3/hw3_files/hw3/`; `hw3_files.zip` is the same folder as submitted.

- **Decision trees** (`decisiontree.py`): ID3 with **information gain**, **gain ratio** and **average Gini
  index** as the split criterion, plus **chi-squared pre-pruning**. Each tree is drawn with Graphviz
  (`infogain.pdf`, `gainratio.pdf`, `avgginiindex.pdf`, `gainratiopreprun.pdf`) and scored on the test set.
- **SVMs** (`svmfirstpart.py` … `svmfourthpart.py`):
  1. a linear SVM on linearly separable data
  2. different kernels on non-linearly separable data
  3. a 5-fold grid search over the SVM hyperparameters (kernel, C, gamma) on the cat/dog images
  4. an RBF SVM on an imbalanced version of the cat/dog data

## Homework 4 — Naive Bayes and HMMs (`hw4_files/`)

| File | What it does |
|---|---|
| `nb.py` | **Naive Bayes** text classifier for news articles (sport, business, politics, entertainment, tech). **Unfinished:** only `vocabulary()` is implemented; `train()` and `test()` are still the given stubs |
| `hmm.py` | **hidden Markov model**: the **forward** algorithm (sequence probability) and **Viterbi** (most likely state sequence) |
| `nb_mini_test.py`, `hmm_mini_test.py` | small checks for both |

## Running

Each script runs on its own from its folder, for example:

```bash
cd hw2/hw2_data && python3 knn.py
cd hw4_files && python3 hmm_mini_test.py
```
