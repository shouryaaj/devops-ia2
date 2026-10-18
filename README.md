# DevOps IA-2: Continuous Integration Demo

A minimal Python project used to demonstrate a Continuous Integration (CI) pipeline with GitHub Actions.

## What the pipeline does

Every push or pull request to `main` triggers the **CI Pipeline** workflow (`.github/workflows/ci.yml`), which runs two jobs in sequence:

1. **lint** — checks out the code, installs `flake8`, and runs it against the codebase to catch style issues (line length, unused imports, syntax problems, etc.) before anything else happens.
2. **test** — only runs if `lint` passes. It checks out the code again, installs all dependencies from `requirements.txt`, and runs the test suite with `pytest -v`.

If either job fails, the workflow is marked as failed on the commit/PR, so broken or badly styled code never silently merges.

## Running tests locally

```bash
# install dependencies
pip install -r requirements.txt

# run the test suite
pytest -v

# run the linter
flake8 .
```

## Workflow jobs explained

- **`on.push` / `on.pull_request` (branches: main)** — the workflow fires whenever someone pushes to `main` or opens/updates a pull request targeting `main`.
- **`lint` job** — runs on a fresh `ubuntu-latest` virtual machine, sets up Python 3.11, installs `flake8`, and runs `flake8 .` to check code style across the whole repo.
- **`test` job** — declares `needs: lint`, so it only starts after `lint` succeeds. It sets up its own fresh `ubuntu-latest` + Python 3.11 environment, installs everything in `requirements.txt`, and runs `pytest -v` to execute all 5 unit tests with verbose output.
