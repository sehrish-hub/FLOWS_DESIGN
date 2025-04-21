from crewai.flow.flow import Flow, listen, start, router
import random
from pydantic import BaseModel

class Routerflow(Flow):

    @start()
    def greeting(self):
        print("Cool Day!")

        # cities = ["karachi", "islambad","lahore"]

        # select_city = random.choice(cities)
        # self.state['city'] = select_city

    @router(greeting)
    def select_city(self):
        cities = ["Karachi", "Islambad","Lahore", "Peshawar"]
        

        # select_city = random.choice(cities)
        self.city = random.choice(cities)
        print("City Selected: ", self.city)

        if self.city == "Karachi":
            return 'Karachi'
        if self.city == "Islambad":
            return 'Islambad'
        if self.city == "Lahore":
            return 'Lahore'
        if self.city == "Peshawar":
            return 'Peshawar'     
        # if self.state['city']=='karachi':
        #     return 'karachi'
        # elif self.state['city']=='islambad':
        #     return 'islambad'
        # else:
        #     return 'lahore'
    @listen('Karachi')
    def karachi(self):
        print("Karachi is the largest city of Pakistan.")
        #print(f"Write some fun fact about {self.state['city']} city.")
        #return f"Write some fun fact about {self.state['city']} city."
    
    @listen('Islambad')
    #def islamabad(self, city):
    def islamabad(self):
        print("Islamabad is the capital of Pakistan.")
        #print(f"Write some fun fact about {self.state['city']} city.")
        #return f"Write some fun fact about {self.state['city']} city."
    
    @listen('Lahore')
    #def lahore(self, city):
    def lahore(self):
        print("Lahore is the city of gardens.")
        #print(f"Write some fun fact about {self.state['city']} city.")
        #return f"Write some fun fact about {self.state['city']} city."
    @listen('Peshawar')
    #def peshawar(self, city):
    def peshawar(self):
        print("Peshawar is the city of flowers.")
        #print(f"Write some fun fact about {self.state['city']} city.")
        #return f"Write some fun fact about {self.state['city']} city."
    
    


def kickoff():
    obj = Routerflow()
    obj.kickoff()

def plot6():
    obj = Routerflow()
    obj.plot()
     # pip install crewai
    # uv run route_run6
    # uv run route_plot6
