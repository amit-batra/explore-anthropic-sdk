"""Anthropic SDK example: send a message and print the full response as indented JSON."""

import json
import os

from anthropic import Anthropic
from anthropic.types import Message
from dotenv import load_dotenv

def format_response(response: Message) -> str:
	"""Serialize a Message to an indented JSON string for human-readable inspection."""
	# to_dict() is an SDK-provided serialiser that converts the Message to a plain Python dict
	return json.dumps(response.to_dict(), indent=2)

def main() -> None:
	"""Send a hardcoded prompt to the model and print the full response object."""
	load_dotenv()  # populates ANTHROPIC_API_KEY (and optionally ANTHROPIC_BASE_URL) from .env
	client: Anthropic = Anthropic()

	response: Message = client.messages.create(
		model=os.environ["MODEL"],  # set MODEL in .env
		max_tokens=1024,
		messages=[{"role": "user", "content": "Hello, Gemma!"}]
	)
	print(format_response(response))

if __name__ == "__main__":
    main()