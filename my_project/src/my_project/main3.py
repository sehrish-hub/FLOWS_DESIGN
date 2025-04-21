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
        city = result['choices'][0]['message']['content']
        print(city)
        return city
    
    @listen(generate_random_city)
    def generate_fun_fact(self, city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=GEMINI_API_KEY,
            messages=[{"content":f"write some fun fact about {city_name} city.",
                       "role":"user"}]

        )
        fun_fact = result['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact'] = fun_fact
        # return fun_fact

    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_fact.md","w") as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']

def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)
    # uv add litellm
    # pip install python-dotenv
    # uv run chain_prompt2
