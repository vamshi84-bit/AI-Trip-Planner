from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_plan(source, destination, days, budget):

    prompt = f"""
    Create a {days}-day travel plan from {source} to {destination}.
    Budget: ₹{budget}

    Rules:
    - Simple day-wise plan (no extra formatting)
    - Budget friendly
    - Mention if budget is insufficient
    """

    try:
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        reply = chat.choices[0].message.content

        cleaned = []
        for line in reply.split("\n"):
            line = line.strip()
            if line:
                line = line.replace("*", "").replace("-", "")
                cleaned.append(line)

        return cleaned

    except Exception as e:
        print("AI Error:", e)
        return ["Basic plan: Travel, explore, return within budget."]