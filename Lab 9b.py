"""
Simple implementation of the Schelling model of segregation in Python
(https://www.uzh.ch/cmsssl/suz/dam/jcr:00000000-68cb-72db-ffff-ffffff8071db/04.02%7B_%7Dschelling%7B_%7D71.pdf)
For use in classes at the Harris School of Public Policy
"""

#Genevieve Madigan  

import random
import numpy as np

class Agent:
    def __init__(self, world, agent_id):
        self.world = world
        self.agent_id = agent_id
        self.location = None

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.world.size) for j in range(self.world.size) if self.world.grid[i][j] is None]
        if empty_patches:
            return random.choice(empty_patches)
        return None

    def move_to_patch(self, x, y):
        if self.location:
            self.world.grid[self.location[0]][self.location[1]] = None
        self.location = (x, y)
        self.world.grid[x][y] = self

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = np.full((size, size), None)
        self.agents = self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        agents = []
        for agent_id in range(num_agents):
            agent = Agent(self, agent_id)
            loc = agent.find_empty_patch()
            agent.move_to_patch(*loc)
            agents.append(agent)
        return agents

    def simulate(self, num_steps):
        for step in range(num_steps):
            for agent in self.agents:
                new_patch = agent.find_empty_patch()
                if new_patch:
                    agent.move_to_patch(*new_patch)
            self.display_world()

    def display_world(self):
        for row in self.grid:
            print(' '.join(['.' if cell is None else 'A' for cell in row]))
        print()


if __name__ == "__main__":
    world_size = 5
    num_agents = 3
    num_steps = 5

    world = World(world_size, num_agents)
    world.simulate(num_steps)
