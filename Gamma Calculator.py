import numpy as np # Library

def gamma_calculator(S, K, v, y, r):
    d1 = (np.log(S / K) + (r + v ** 2 / 2) * y) / (v * y ** 0.5)  # Delta 1
    d2 = d1 - v * y ** 0.5  # Delta 2

    d_d1 = np.exp(-d1 ** 2 / 2) / (2 * np.pi) ** 0.5  # Derived Delta 1

    gamma_parameter = d_d1 / S / v / y ** 0.5  # Gamma value

    return {"Call & Put": gamma_parameter}  # Display value

gamma_calculator(49, 50, 0.2, 0.3846, 0.05) # Example usage:
