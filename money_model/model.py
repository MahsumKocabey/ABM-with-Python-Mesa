from mesa import Model
from agent import MoneyAgent
from mesa.time import RandomActivation


class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    """
    Time in most agent-based models moves in steps, sometimes also called ticks.

    The scheduler is a special model component which controls the order in which agents are activated.
    For example, all the agents may activate in the same order every step; their order might be shuffled;
    we may try to simulate all the agents acting at the same time; and more.

    important; scheduling patterns can have an impact on your results.
    """

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
