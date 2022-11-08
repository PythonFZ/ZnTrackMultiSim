from zntrack import Node, zn


class Simulator(Node):
    parameter1: float = zn.params()
    parameter2: float = zn.params()
    metric: float = zn.metrics()

    def run(self):
        """Run the Simulation here"""
        self.metric = self.parameter1 + self.parameter2
