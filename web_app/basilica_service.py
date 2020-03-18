# web_app/basilica_service.py
import basilica

import os
from dotenv import load_dotenv

load_dotenv() # Will look inside a .env file for our environment variable.

API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)


if __name__ == "__main__":   # This makes it so that this code is only called on when this script is run in the command line directly.
    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]
    embeddings = connection.embed_sentences(sentences)
    print(type(embeddings))

    for embedding in embeddings:
        print(len(embedding))   #> 768
        print(list(embedding))  # [0.0238289,....
        print("-----------")
