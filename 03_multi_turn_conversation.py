"""Anthropic SDK example: Simulate a multi-turn conversation with the LLM, and print the full response as indented JSON."""

import json
import os

from anthropic import Anthropic
from anthropic.types import Message
from dotenv import load_dotenv

def format_response(message: Message) -> str:
    """Serialize a Message to an indented JSON string for human-readable inspection."""
    # to_dict() is an SDK-provided serialiser that converts the Message to a plain Python dict
    return json.dumps(message.to_dict(), indent=2)

def main() -> None:
    """Send a simulated multi-turn conversation to the model and print the full response object."""
    load_dotenv()  # populates ANTHROPIC_API_KEY (and optionally ANTHROPIC_BASE_URL) from .env
    client: Anthropic = Anthropic()

    message: Message = client.messages.create(
        model=os.environ["MODEL_NAME"],  # set MODEL_NAME in .env
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Gemma!"},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Can you tell me a joke about football?"}
        ]
    )
    print("Full response:")
    print(format_response(message))
    print("\nModel's reply:")
    print(message.content[0].text)

if __name__ == "__main__":
    main()