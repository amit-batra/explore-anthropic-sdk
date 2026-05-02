# Exploring the Anthropic Python SDK

A collection of small scripts for learning the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) — fast Python package and project manager
- An Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

## Setup

```bash
# Install dependencies and create the virtual environment
uv sync

# Copy the example env file and add your API key
cp .env.example .env
```

`.env` should contain:

```
ANTHROPIC_API_KEY=sk-ant-...
```

## Running the scripts

```bash
uv run 01_hello_anthropic.py
uv run 02_basic_request_response.py
```

## Scripts

| File | Description |
|------|-------------|
| `01_hello_anthropic.py` | Minimal example — creates a client, sends a single message, and prints the text reply. |
| `02_basic_request_response.py` | Same request/response flow, but prints the full `Message` object as indented JSON so you can inspect every field (content blocks, stop reason, token usage, etc.). |

## Project structure

```
.
├── pyproject.toml          # project metadata and dependencies (managed by uv)
├── uv.lock                 # pinned dependency versions — commit this for reproducibility
├── .python-version         # Python version pin used by uv
├── .env                    # your API key — never committed (see .gitignore)
├── 01_hello_anthropic.py
└── 02_basic_request_response.py
```
