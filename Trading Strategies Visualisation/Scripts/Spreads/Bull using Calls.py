import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def spread_bull_call(k1, k2, c1, c2):
    """
    Bull Spread using Calls
    k1: Strike price of Long Call
    k2: Strike price of Short Call
    c1: Premium paid for Long Call
    c2: Premium received for Short Call
    """
    if k1 >= k2:
        print("Long Call cannot be higher than Short Call")
        return None
    
    # Long Call payoff
    L1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k1 + 1),
        "Profit from Long Call": -c2  # Premium paid (constant)
    })
    L2 = pd.DataFrame({
        "Stock Price": np.arange(k2 - 4, k2 + 6),
        "Profit from Long Call": np.arange(k2 - 5 - k1, k2 + 5 - k1) - 2
    })
    L = pd.concat([L1, L2], ignore_index=True)
    
    # Short Call payoff
    S1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k2 + 1),
        "Profit from Short Call": c1  # Premium received (constant)
    })
    S2 = pd.DataFrame({
        "Stock Price": np.arange(k2 + 1, k2 + 6),
        "Profit from Short Call": 1 - np.arange(k2 - 4 - k1, k2 - k1 + 1)
    })
    S = pd.concat([S1, S2], ignore_index=True)
    
    # Merge payoffs
    DF = pd.merge(L, S, on="Stock Price")
    DF["Total Payoff"]=DF["Profit from Long Call"]+DF["Profit from Short Call"]
    
    # Plot
    plt.figure(figsize=(8,6))
  
    plt.plot(DF["Stock Price"],
             DF["Total Payoff"],
             label="Total Payoff",
             color="red",
             linewidth=3)
  
    plt.plot(DF["Stock Price"],
             DF["Profit from Long Call"],
             linestyle="--",
             linewidth=2,
             label="Long Call")
  
    plt.plot(DF["Stock Price"],
             DF["Profit from Short Call"],
             linestyle="--",
             linewidth=2,
             label="Short Call")
    
    plt.axhline(0, color="black", linewidth=1)  # break-even line
    plt.grid(True, linestyle=":", color="grey")
    
    plt.title("P&L from Bull Spread using Calls")
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.legend()
    
    # Annotations
    plt.text(k1-2.5, 1.25, f"Short Call, Strike Price of ${k2}")
    plt.text(k1-2.5, -2.75, f"Long Call, Strike Price of ${k1}")
    
    plt.show()
    
    return DF

df = spread_bull_call(30, 35, 1, 3) # Test run
print(df)
