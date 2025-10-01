import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def combo_strap(k, call, put):
  
    # Long Calls (two calls in strap)
    C1 = np.column_stack([np.arange(k - 10, k + 1), -call * np.ones(10 + 1)])
    C2 = np.column_stack([np.arange(k + 1, k + 11), np.arange(1, 11) - call])
    C = np.vstack([C1, C2])
    
    # Long Put
    P1 = np.column_stack([np.arange(k - 10, k), put - np.arange(-5, 5) - 1])
    P2 = np.column_stack([np.arange(k, k + 11), -put*np.ones(k + 10 - k + 1)])
    P = np.vstack([P1, P2])
    
    # DataFrames
    dfC = pd.DataFrame(C, columns=["Stock Price", "Profit from Long Call"])
    dfP = pd.DataFrame(P, columns=["Stock Price", "Profit from Long Put"])
    
    # Merge on Stock Price
    DF = pd.merge(dfC, dfP, on="Stock Price")
    
    # Total payoff = 2 Calls + 1 Put
    DF["Total Payoff"]=2*DF["Profit from Long Call"]+DF["Profit from Long Put"]
    
    # Plot
    plt.figure(figsize=(10, 6))
    
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
      "--",
      label="Long Call",
      linewidth=1.5
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Put"],
      "--",
      label="Long Put",
      linewidth=1.5
      )
    
    plt.axhline(0, color="black", linewidth=1)
    plt.grid(True, linestyle="--", alpha=0.6)
    
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("Profit & Loss from Strap Strategy")
    plt.legend()
    
    # Annotation text
    plt.text(k + 5, 0.25 - put, f"Long Put, Strike ${k}")
    plt.text(k - 10, -1 - call, f"2 Long Calls, Strike ${k}")
    
    plt.show()
    
    return DF

combo_strap(70, 1, 3) # Test
