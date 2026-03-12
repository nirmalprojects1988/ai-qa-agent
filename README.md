# AI QA Agent

A simple AI-powered QA assistant that generates structured test scenarios from feature descriptions using LLMs.

---

## Problem

QA engineers often manually write test cases based on feature requirements.  
This project explores how an AI agent can assist in generating structured test scenarios automatically.

---

## Features

- Generate test scenarios from feature descriptions
- Covers:
  - Positive test cases
  - Negative test cases
  - Edge cases
  - Security scenarios
  - Boundary conditions

---

## Architecture

Feature description  
→ Python Agent  
→ Tool layer  
→ OpenAI LLM  
→ Structured test scenarios

---

## Tech Stack

- Python
- OpenAI API
- python-dotenv
- Modular agent architecture

---

## Project Structure
ai-qa-agent
│
├ agent.py # Agent orchestration logic
├ tools.py # Reusable tools used by the agent
├ requirements.txt # Project dependencies
├ .env # API key configuration (not committed)
├ .gitignore
└ README.md


---

## Demo

Run the agent:

```bash
python agent.py

Describe feature:
User login functionality with email and password

Generated Test Scenarios:

1. Verify login with valid email and password
2. Verify login with incorrect password
3. Verify login with non-registered email
4. Verify login with empty email field
5. Verify login with empty password field
6. Verify login with SQL injection attempts
7. Verify login with boundary password length
8. Verify account lock after multiple failed login attempts


Setup

Clone the repository:

git clone https://github.com/nirmalprojects1988/ai-qa-agent.git
cd ai-qa-agent


Install dependencies:

pip install -r requirements.txt

Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here


Run the agent:

python agent.py
