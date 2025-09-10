import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def spread_bear_call(k1, k2, c1, c2):
    # Bear Spread using Calls
    
    if k1 >= k2:
        print("Short Call can't be higher than Long Call")
        return None
    
    # Long Call payoff
    L1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k2 + 1),
        "Profit from Long Call": -c1
    })
    L2 = pd.DataFrame({
        "Stock Price": np.arange(k2 + 1, k2 + 6),
        "Profit from Long Call": np.arange(k2 - 4 - k1, k2 - k1 + 1) - 1
    })
    L = pd.concat([L1, L2], ignore_index=True)
    
    # Short Call payoff
    S1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k1 + 1),
        "Profit from Short Call": c2
    })
    S2 = pd.DataFrame({
        "Stock Price": np.arange(k1 + 1, k2 + 6),
        "Profit from Short Call": c2 - np.arange(1, 11)
    })
    S = pd.concat([S1, S2], ignore_index=True)
    
    DF = pd.merge(L, S, on="Stock Price") # Merge both
    
    # Total payoff
    DF["Total Payoff"]=DF["Profit from Long Call"]+DF["Profit from Short Call"]
    
    # Plot
    plt.figure(figsize=(10,6))
    
    plt.plot(
      DF["Stock Price"],
      DF["Total Payoff"],
      label="Total Payoff",
      color="red",
      linewidth=3
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Call"],
      label="Long Call",
      linestyle="--"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Short Call"],
      label="Short Call",
      linestyle="--"
      )
    
    plt.axhline(0, color="black", linewidth=1)
    plt.grid(linestyle="--", alpha=0.7)
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("P&L from Bear Spread using Calls")
    plt.legend()
    
    # Annotating strikes
    plt.text(k1 - 5, 3.25, f"Short Call, Strike Price of ${k1}")
    plt.text(k1 - 5, -0.75, f"Long Call, Strike Price of ${k2}")
    
    plt.show()
    
    return DF

spread_bear_call(30, 35, 1, 3) # Test
