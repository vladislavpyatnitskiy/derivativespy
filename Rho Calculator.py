def rho_calculator(S, K, v, y, r): # Function for Rho of Option
  
  d1 = (np.log(S / K) + (r + v ** 2/2) * y) / v / y ** .5 # Delta 1
  
  d2 = d1 - v * y ** .5 # Delta 2
  
  rho_df = pd.DataFrame({'Call':[K*y*np.exp(-r*y) * norm.cdf(d2)],
  'Put':[-K*y*np.exp(-r*y) * norm.cdf(-d2)]})
  
  return(rho_df) # Display value

rho_calculator(49, 50, .2, .3846, .05) # Test
