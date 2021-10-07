import numpy as np

def dist_lognormal():
  np.random.seed(0)
  return np.random.lognormal(size=1000)
