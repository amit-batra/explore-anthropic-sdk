"""Minimal Anthropic SDK example: send a single message and print the text reply."""

import os
from urllib import response

from anthropic import Anthropic
from anthropic.types import Message
from dotenv import load_dotenv

def main() -> None:
    """Send a hardcoded prompt to the model and print the response text."""
    load_dotenv()  # populates ANTHROPIC_API_KEY (and optionally ANTHROPIC_BASE_URL) from .env
    client: Anthropic = Anthropic()  # key is read from the environment automatically

    message: Message = client.messages.create(
        model=os.environ["MODEL_NAME"],  # set MODEL_NAME in .env
        max_tokens=4096,  # upper bound on output; the model stops earlier if it finishes naturally
        messages=[
            {"role": "user", "content": "Short overview of uv utility for Python developers"}
        ],
    )

    print(message.content[0].text)  # content is a list of blocks; [0] assumes a single text reply

if __name__ == "__main__":
    main()