from crewai.flow.flow import Flow, listen, start, router#, or_
import random
class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Assalam-O-alikum!")

    @router(greeting)
    def select_city(self):
            cities = ["karachi", "islambad","lahore"]

            select_city = random.choice(cities)
            self.state['city'] = select_city

            if select_city == 'karachi':
                return 'karachi'
            if select_city == 'islambad':
                return 'islambad'
            if select_city == 'lahore':
                return 'lahore'
    
    
    @listen('karachi')
    def karachi(self):
        print(f"Write some fun fact about {self.state['city']} city.")
        return f"Write some fun fact about {self.state['city']} city."

    @listen('islambad')
    def islambad(self, city):
        print(f"Write some fun fact about {self.state['city']} city.")
        return f"Write some fun fact about {self.state['city']} city."

    @listen('lahore')
    def lahore(self, city):
        print(f"Write some fun fact about {self.state['city']} city.") 
        return f"Write some fun fact about {self.state['city']} city."

def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot3():
    obj = RouteFlow()
    obj.plot()
     # pip install crewai
    # uv run route_run3
    # uv run route_plot3
