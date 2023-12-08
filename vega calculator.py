def vega_calculator(S, K, v, y, r):
  
  d1 = (np.log(S / K) + (r + v ** 2/2) * y) / v / y ** 0.5 # Delta 1
  
  d2 = d1 - v * y ** 0.5 # Delta 2
  
  d_d1 = np.exp(-d1 ** 2 / 2) / (2 * np.pi) ** .5 # Derived Delta 1
  
  vega_parameter = round(S * y ** 0.5 * d_d1, 2) # Vega value
  
  return(vega_parameter) # Display value

vega_calculator(49, 50, .2, .3846, .05) # Test
