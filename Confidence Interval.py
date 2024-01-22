import numpy as np
from scipy.stats import norm

# Function to calculate confidence intervals for stock volatility
def confidence_interval(p, r, v, y, rg=95):
  
    mean_ci = np.log(p) + (r - v**2 / 2) * y  # Mean
    sd_ci = (v**2 * y)**0.5  # Standard Deviation

    l = np.exp(mean_ci + norm.ppf((100-rg)/200)*sd_ci)  # Lower Bound
    u = np.exp(mean_ci + norm.ppf(rg*.01+(100-rg)/200) * sd_ci)  # Upper Bound

    return f"{rg}% probability stock price will be between {l:.2f} and {u:.2f}."

print(confidence_interval(p=40, r=0.16, v=0.2, y=0.5, rg=99)) # Test
