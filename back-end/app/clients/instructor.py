import os
from dotenv import load_dotenv
import instructor
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

open_ai_key = os.getenv('OPEN_AI_KEY')

# Define the Open AI Client
openAiClient = OpenAI(
    api_key=open_ai_key #Open AI Key
)

# Patch the client with Instructor
instructorClient = instructor.patch(openAiClient)