from crewai.flow.flow import Flow, listen, start, router#, or_
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam-O-alikum!")

        cities = ["karachi", "islambad","lahore"]

        select_city = random.choice(cities)
        self.state['city'] = select_city

    @router(greeting)
    def select_city(self):
        
        
        if self.state['city']=='karachi':
            return 'karachi'
        elif self.state['city']=='islambad':
            return 'islambad'
        else:
            return 'lahore'
        
        
        
    
       
        
    
    @listen('karachi')
    def f1(self):
        print(f"Write some fun fact about {self.state['city']} city.")
        return f"Write some fun fact about {self.state['city']} city."
    
    @listen('islambad')
    def Islamabad(self, city):
        print(f"Write some fun fact about {self.state['city']} city.")
        return f"Write some fun fact about {self.state['city']} city."
    
    @listen('lahore')
    def Lahore(self, city):
        print(f"Write some fun fact about {self.state['city']} city.")
        return f"Write some fun fact about {self.state['city']} city."
    
    


def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot4():
    obj = RouteFlow()
    obj.plot()
     # pip install crewai
    # uv run route_run4
    # uv run route_plot4




