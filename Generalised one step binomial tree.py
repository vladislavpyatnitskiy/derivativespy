import numpy as np

def gen_one_step_bin_tree(y, s, d, r): # option value via generalisation
  
  bins = (np.exp(r * y) - (s - d) / s) / (2 * d / s) # Calculate probability
  
  option = round(np.exp(-r*y) * (bins + 0*(1 - bins)),3)
  
  print(f"Option Value today is {option}")

gen_one_step_bin_tree(y = .25, s = 20, d = 2, r = .12) # Test
