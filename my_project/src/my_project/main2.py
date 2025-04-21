from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# GEMINI_API_KEY = "AIzaSyD0ne8oTpsi7XYbp7GsdbrVWehSl5_aN7U"
# import time
class CityFunFact(Flow):
    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=GEMINI_API_KEY,
            messages=[{"content":"Return any random city name from pakistan.",
                       "role":"user"}]

        )
        print(result['choices'][0]['message']['content'])
def kickoff():
    obj = CityFunFact()
    obj.kickoff()
    # uv add litellm
    # pip install python-dotenv
    # uv run chain_prompt1
