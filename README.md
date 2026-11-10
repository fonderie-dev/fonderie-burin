# Burin

Inspecting and editing the weights of open models. Part of
[Fonderie](https://github.com/fonderie-dev).

A *burin* is the engraver's chisel, used to cut fine lines into finished
metal.

> **Status: scaffold (○○○).** The package installs and its smoke test passes.
> None of the scope below is implemented yet.

## Intended scope

- Read `safetensors` checkpoints lazily and report per-tensor shape, dtype and
  summary statistics without loading the whole model into memory.
- Compare two checkpoints of the same architecture, for example a base model
  and its fine-tune from
  [Affinage](https://github.com/fonderie-dev/fonderie-affinage), layer by
  layer.
- Targeted edits (rescaling, zeroing, replacing or merging tensors) written to
  a new checkpoint, with a record of every change and the checksums of input
  and output.
- Confirm that an edited checkpoint still loads with the expected shapes.

Not in scope: training (Affinage); judging whether an edit helps
([Essai](https://github.com/fonderie-dev/fonderie-essai)). Pickle-based
checkpoints are not read; see the organisation's
[security notes](https://github.com/fonderie-dev/.github/blob/main/SECURITY.md#model-files-and-remote-code).

## First milestones

1. Tensor inventory and statistics for a `safetensors` file.
2. Checkpoint comparison report.
3. Recorded edits with a change log that allows the edit to be reversed.

## Development

```sh
python -m pip install -e ".[dev]"
ruff check . && ruff format --check .
python -m pytest
```

```
src/fonderie_burin/   package
tests/                pytest suite: synthetic tensors, no downloads, no GPU
```

CI runs the shared
[Fonderie workflow](https://github.com/fonderie-dev/.github/blob/main/.github/workflows/python-check.yaml)
on Python 3.11–3.14.

## Licence

Apache-2.0; see [LICENSE](LICENSE) and [NOTICE](NOTICE). Models inspected or
edited with this package keep their own licences. © 2026 R. Heller.
