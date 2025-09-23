import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def combo_straddle(k, call, put):
    # Long Call payoff
    C_left = np.column_stack((np.arange(k - 10, k + 1),np.full(11, -call)))
    C_right = np.column_stack((np.arange(k+1, k+11),np.arange(1, 11) - call))
    C = np.vstack((C_left, C_right))
    
    # Long Put payoff
    P_left = np.column_stack((np.arange(k-10, k), put - np.arange(-5, 5) - 1))
    P_right = np.column_stack((np.arange(k, k + 11), np.full(11, -put)))
    P = np.vstack((P_left, P_right))
    
    # Create DataFrames
    df_C = pd.DataFrame(C, columns=["Stock Price", "Profit from Long Call"])
    df_P = pd.DataFrame(P, columns=["Stock Price", "Profit from Long Put"])
    
    # Merge on Stock Price
    DF = pd.merge(df_C, df_P, on="Stock Price")
    
    # Total payoff
    DF["Total Payoff"] = DF["Profit from Long Call"]+DF["Profit from Long Put"]
    
    # Plot
    plt.figure(figsize=(10,6))
    
    plt.plot(
      DF["Stock Price"],
      DF["Total Payoff"],
      label="Total Payoff",
      linewidth=3,
      color="red"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Call"],
      linestyle="--",
      linewidth=2,
      label="Long Call"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Long Put"],
      linestyle="--",
      linewidth=2, label="Long Put"
      )
    
    plt.axhline(0, color="black", linewidth=1)
    plt.grid(True, linestyle=":", color="grey")
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("Profit & Loss from Straddle")
    plt.legend()
    
    # Annotate text
    plt.text(k + 2.5, 0.25 - put, f"Long Put, Strike Price of ${k}")
    plt.text(k - 10.5, 0.25 - call, f"Long Call, Strike Price of ${k}")
    
    plt.show()
    
    return DF

combo_straddle(70, 1, 3) # Test
