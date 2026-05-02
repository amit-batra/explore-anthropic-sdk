"""Minimal Anthropic SDK example: send a single message and print the text reply."""

import os

from anthropic import Anthropic
from anthropic.types import Message
from dotenv import load_dotenv

def main() -> None:
	"""Send a hardcoded prompt to the model and print the response text."""
	load_dotenv()  # populates ANTHROPIC_API_KEY (and optionally ANTHROPIC_BASE_URL) from .env
	client: Anthropic = Anthropic()  # key is read from the environment automatically

	response: Message = client.messages.create(
    	model=os.environ["MODEL"],  # set MODEL in .env
    	max_tokens=4096,  # upper bound on output; the model stops earlier if it finishes naturally
    	messages=[
        	{"role": "user", "content": "Short overview of uv utility for Python developers"}
    	],
	)

	print(response.content[0].text)  # content is a list of blocks; [0] assumes a single text reply

if __name__ == "__main__":
    main()