import os
from dotenv import load_dotenv
from agent import ToDoAgent

load_dotenv()

AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_API_KEY = os.getenv("AOAI_API_KEY")
AOAI_API_VERSION = os.getenv("AOAI_API_VERSION")
AOAI_DEPLOYMENT = os.getenv("AOAI_DEPLOYMENT")

if __name__ == "__main__":
  agent = ToDoAgent(
    aoai_endpoint=AOAI_ENDPOINT,
    aoai_key=AOAI_API_KEY,
    aoai_api_version=AOAI_API_VERSION,
    aoai_deployment=AOAI_DEPLOYMENT
  )

  while True:
    user_prompt = input("You >>> ")

    if user_prompt == "exit":
      break

    response = agent.execute_agent(user_prompt)

    print("Bot >>>", response)
