from mesa import Agent
# from model import MoneyModel


class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    # RandomActivation which activates all the agents once per step in ramdom order.
    # Every agent is expected to have a step method.
    def step(self):
        # The agents step will go here.
        print ("Hi, I am agent" , str(self.unique_id), "and my wealth is", str(self.wealth))
