"""Anthropic SDK example: Send an image (as base64-encoded data) to the model and print the full response as indented JSON."""

import base64
import httpx
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
    image_url: str = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
    image_media_type: str = "image/jpeg"
    image_data: str = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

    load_dotenv()  # populates ANTHROPIC_API_KEY (and optionally ANTHROPIC_BASE_URL) from .env
    client: Anthropic = Anthropic()

    message: Message = client.messages.create(
        model=os.environ["MODEL_NAME"],  # set MODEL_NAME in .env
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in the attached image?"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image_media_type,
                            "data": image_data,
                        },
                    },
                ],
            },
        ],
    )

    print("Full response:")
    print(format_response(message))
    print("\nModel's reply:")
    print(message.content[0].text)

if __name__ == "__main__":
    main()