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

# Optional: override the default API base URL (e.g. for a proxy or local model server)
ANTHROPIC_BASE_URL=

# Optional: model passed to client.messages.create (e.g. claude-opus-4-7)
MODEL_NAME=
```

## Running the scripts

```bash
uv run 01_hello_anthropic.py
uv run 02_basic_request_response.py
uv run 03_multi_turn_conversation.py
uv run 04_partial_response_completion.py
uv run 05_image_recognition_base64.py
uv run 06_image_recognition_url.py
```

## Scripts

| File | Description |
|------|-------------|
| `01_hello_anthropic.py` | Minimal example — creates a client, sends a single message, and prints the text reply. |
| `02_basic_request_response.py` | Same request/response flow, but prints the full `Message` object as indented JSON so you can inspect every field (content blocks, stop reason, token usage, etc.). |
| `03_multi_turn_conversation.py` | Simulates a multi-turn conversation by sending a sequence of user/assistant messages and prints the full response as indented JSON. |
| `04_partial_response_completion.py` | Forces the model to complete a partial response by pre-filling the assistant turn. |
| `05_image_recognition_base64.py` | Downloads an image, encodes it as base64, and asks the model to describe it. |
| `06_image_recognition_url.py` | Sends an image to the model via URL reference and asks the model to describe it. |

## Project structure

```
.
├── pyproject.toml          # project metadata and dependencies (managed by uv)
├── uv.lock                 # pinned dependency versions — commit this for reproducibility
├── .python-version         # Python version pin used by uv
├── .env                    # your API key — never committed (see .gitignore)
├── 01_hello_anthropic.py
├── 02_basic_request_response.py
├── 03_multi_turn_conversation.py
├── 04_partial_response_completion.py
├── 05_image_recognition_base64.py
└── 06_image_recognition_url.py
```
