from crewai.flow.flow import Flow, listen, start
import random
class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Assalam-O-alikum!")

    @listen(greeting)
    def select_city(self):
            cities = ["Karachi", "Islambad","Lahore"]
            select_city = random.choice(cities)
            print(select_city)

        
    
def kickoff():
    obj = RouteFlow()
    obj.kickoff()
def plot():
    obj = RouteFlow()
    obj.plot()
    # pip install crewai
    # uv run route_run
    # uv run route_plot
