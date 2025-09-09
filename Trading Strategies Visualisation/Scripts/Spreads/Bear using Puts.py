import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def spread_bear_put(k1, k2, c1, c2):
    # Bear Spread using Puts
    
    if k1 >= k2:
        print("Short put cannot be higher than Long Put")
        return None
    
    # Long Put payoff
    L1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k2 + 1),
        "Profit from Long Put": k1 + c2 - c1 - np.arange(k1 - 5, k2 + 1)
    })
    
    L2 = pd.DataFrame({
        "Stock Price": np.arange(k2 + 1, k2 + 6),
        "Profit from Long Put": -c2
    })
    
    L = pd.concat([L1, L2])
    
    # Short Put payoff
    S1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k1),
        "Profit from Short Put": np.arange(k1 - 5, k1) - k1 + c1
    })
    
    S2 = pd.DataFrame({
        "Stock Price": np.arange(k1, k2 + 6),
        "Profit from Short Put": c1
    })
    
    S = pd.concat([S1, S2])
    
    DF = pd.merge(L, S, on="Stock Price") # Merge
    
    # Total payoff
    DF["Total Payoff"] = DF["Profit from Long Put"]+DF["Profit from Short Put"]
    
    plt.figure(figsize=(8,6)) # Plot
    
    plt.plot(
      DF["Stock Price"],
      DF["Total Payoff"],
      label="Total Payoff",
      linewidth=3,
      color="red"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Put"],
      linestyle="--",
      label="Long Put",
      linewidth=2
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Short Put"],
      linestyle="--",
      label="Short Put",
      linewidth=2
      )
    
    plt.axhline(0, color="black")
    plt.grid(True, linestyle=":", color="grey")
    
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("P&L from Bear Spread using Puts")
    plt.legend()
    
    plt.text(k2, 1.25, f"Short Put, Strike Price of ${k1}")
    plt.text(k2, -2.75, f"Long Put, Strike Price of ${k2}")
    
    plt.show()
    
    return DF

spread_bear_put(30, 35, 1, 3) # Test
