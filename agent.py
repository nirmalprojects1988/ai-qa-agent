import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import generate_test_scenarios

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI()

def run_agent(feature):

    # generate prompt from tool
    prompt = generate_test_scenarios(feature)

    # call LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior QA automation engineer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    feature = input("Describe feature: ")

    result = run_agent(feature)

    print("\nGenerated Test Scenarios:\n")
    print(result)