from crewai.flow.flow import Flow, start, listen
import time


class SimpleFlow(Flow):
    @start()
    def function1(self):
        print("step1...")
        time.sleep(3)

    @listen(function1)
    def function2(self): 
        print("step2...")
        time.sleep(3)

    @listen(function2)
    def function3(self): 
        print("step3...")
        time.sleep(3)



def kickoff():
    obj = SimpleFlow()
    obj.kickoff()
# uv run piaic1
# uv add crewai
