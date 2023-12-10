# Function to calculate option value
def one_step_binomial_tree(y, s, d, r, o):
  
  option_price = round((s-(s-d)*np.exp(-r*y))/2/d*o,3)
  
  print(f"Value of option today is {option_price}") 

one_step_binomial_tree(y = 0.25, s = 20, d = 2, r = 0.12, o = 1) # Test
