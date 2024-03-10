import numpy as np # Library
import pandas as pd # Library

def theta_calculator(S, K, v, y, r):
    d1 = (np.log(S / K) + (r + v ** 2 / 2) * y) / (v * y ** 0.5)  # Delta 1
    d2 = d1 - v * y ** 0.5  # Delta 2

    d_d1 = np.exp(-d1 ** 2 / 2) / (2 * np.pi) ** 0.5  # Derived Delta 1

    theta_call = -((S * d_d1 * v) / (2 * y ** 0.5)) - ((r * K) * np.exp(-r * y) * norm.cdf(d2))  # Call
    theta_put = -((S * d_d1 * v) / (2 * y ** 0.5)) + ((r * K) * np.exp(-r * y) * norm.cdf(-d2))  # Put

    theta_df = pd.DataFrame({'Call': [theta_call], 'Put': [theta_put]})  # Make DataFrame

    return theta_df  # Display

theta_calculator(49, 50, 0.2, 0.3846, 0.05) # Example usage:
