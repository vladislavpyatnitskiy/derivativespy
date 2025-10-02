import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def combo_strip(k, call, put):
    # --- Long Call ---
    C1 = np.column_stack((np.arange(k - 10, k + 1, 1), np.full(11, -call)))
    C2 = np.column_stack((np.arange(k+1, k+11, 1), np.arange(1, 11) - call))
    C = np.vstack((C1, C2))
    C = pd.DataFrame(C, columns=["Stock Price", "Profit from Long Call"])
    
    # --- Long Put ---
    P1 = np.column_stack((np.arange(k-10, k, 1), put - np.arange(-5, 5, 1)-1))
    P2 = np.column_stack((np.arange(k, k + 11, 1), np.full(11, -put)))
    P = np.vstack((P1, P2))
    P = pd.DataFrame(P, columns=["Stock Price", "Profit from Long Put"])
    
    # --- Merge ---
    DF = pd.merge(C, P, on="Stock Price")
    DF["Total Payoff"]=DF["Profit from Long Call"]+2*DF["Profit from Long Put"]
    
    # --- Plot ---
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
      linestyle="--",
      label="Long Call",
      linewidth=2
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Put"],
      linestyle="--",
      label="Long Put",
      linewidth=2
      )
    
    plt.axhline(0, color="black", linewidth=1)
    plt.grid(True, linestyle=":", color="grey")
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("Profit & Loss from Strip")
    plt.legend()
    
    # Labels
    plt.text(k + 5.5, 0.25 - put, f"2 Long Puts, Strike ${k}")
    plt.text(k - 10, -0.75 - call, f"Long Call, Strike ${k}")
    
    plt.show()
    
    return DF

combo_strip(70, 1, 3) # Test
