import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

script = """
Meet the Mostly AI Assistant — your smart companion for exploring data with natural language, no code required.
Let’s start by uploading the synthetic dataset we created in the previous tutorial.
As soon as the data is loaded, the assistant gives you high-level insights — instantly.
From there, you can ask plain-English questions — and the assistant will write and run SQL queries for you.
It can handle joins, aggregations, filters — all the complexity, without you writing a single line of SQL.
You can even generate charts and visualizations with just a simple request.
Run advanced analysis, without code — and give your business teams the power to explore data on their own.
Ask the kind of questions that used to be reserved for data analysts — and get clear, actionable answers.
The Mostly AI Assistant is fast, powerful, and honestly... kind of amazing.
"""

response = openai.audio.speech.create(
    model="tts-1-hd",
    voice="nova",  # Other options: alloy, shimmer, echo
    input=script
)

# Save to file
with open("mostly_ai_assistant_narration.mp3", "wb") as f:
    f.write(response.content)
