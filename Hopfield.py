import numpy as np
class HopfieldNetwork:
  def __init__(self, nodes, states):
    self.nNodes = nodes
    self.nStats = states

    self.T = np.zeros((nodes, nodes))

    self.
