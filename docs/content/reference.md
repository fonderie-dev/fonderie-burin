---
title: "Référence"
description: "Reference for Burin: Python API, inventory and comparison reports, edit specification and change log. Outline; coming soon."
summary: "Every public function, report format and record, field by field."
lede: "The exact interfaces of Burin: functions, report formats and the change log."
outlineTitle: "Planned sections"
outline:
  - id: python-api
    title: "Python API"
    text: "Public modules, functions and classes of `fonderie_burin`, generated from their docstrings once the interfaces settle."
  - id: inventory-report
    title: "Inventory report"
    text: "The fields reported for each tensor: name, shape, dtype and summary statistics."
  - id: comparison-report
    title: "Comparison report"
    text: "The per-layer differences reported for two checkpoints of the same architecture."
  - id: edit-specification
    title: "Edit specification"
    text: "How an edit is described: target tensors, operation and parameters."
  - id: change-log
    title: "Change-log schema"
    text: "The record written with every edited checkpoint, including input and output checksums."
---

## Available now

The package currently exposes its version, `fonderie_burin.__version__`, and
nothing else.
