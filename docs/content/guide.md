---
title: "Guide"
description: "How to use Burin: installation, tensor inventory, checkpoint comparison, recorded edits and verification. Outline; coming soon."
summary: "Looking inside a checkpoint, comparing two, and editing one with a record of every cut."
lede: "How to look inside a checkpoint, compare it with another, and edit it with a record of every change."
outlineTitle: "Planned chapters"
outline:
  - id: installation
    title: "Installation"
    text: "Installing a released version, and the optional extras that bring in tensor libraries only when they are needed."
  - id: first-inspection
    title: "A first inspection"
    text: "An inventory of a small synthetic `safetensors` file: its tensors, shapes, dtypes and statistics."
  - id: inventory
    title: "Tensor inventory"
    text: "Reading a checkpoint lazily and reporting per-tensor shape, dtype and summary statistics without loading the whole model into memory."
  - id: comparison
    title: "Comparing checkpoints"
    text: "Layer-by-layer comparison of two checkpoints of the same architecture, such as a base model and its fine-tune from [Affinage](https://fonderie-dev.github.io/fonderie-affinage/)."
  - id: edits
    title: "Targeted edits"
    text: "Rescaling, zeroing, replacing or merging tensors, always written to a new checkpoint and never in place."
  - id: change-log
    title: "The change log"
    text: "The record of every edit with the checksums of input and output, and how to reverse an edit from it."
  - id: verification
    title: "Verifying an edited checkpoint"
    text: "Confirming that the result still loads with the expected shapes before it goes to [Essai](https://fonderie-dev.github.io/fonderie-essai/) for measurement."
  - id: safe-loading
    title: "Safe loading"
    text: "Why Burin reads `safetensors` only and does not open pickle-based checkpoints. See [safe loading](https://fonderie-dev.github.io/website/methode/#safe-loading)."
---

## Available now: install from source

There is no release yet. The scaffold installs from a clone of the repository:

```sh
git clone https://github.com/fonderie-dev/fonderie-burin.git
cd fonderie-burin
python -m pip install -e ".[dev]"
python -m pytest
```

The tests use small synthetic tensors; they need neither a GPU nor downloads.
