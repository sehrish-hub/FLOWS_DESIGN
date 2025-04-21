from crewai.flow.flow import Flow, listen, start, router
import random
class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Assalam-O-alikum!")

    @router(greeting)
    def select_city(self):
            cities = ["karachi", "islambad","lahore"]
            select_city = random.choice(cities)
            print(select_city)
            return select_city
    @listen(select_city)
    def karachi(self, city):
        print(f"Write some fun fact about {city} city.")
    @listen(select_city)
    def islambad(self, city):
        print(f"Write some fun fact about {city} city.")
    @listen(select_city)
    def lahore(self, city):
        print(f"Write some fun fact about {city} city.") 
def kickoff():
    obj = RouteFlow()
    obj.kickoff()
def plot1():
    obj = RouteFlow()
    obj.plot()
    # pip install crewai
    # uv run route_run1
    # uv run route_plot1














