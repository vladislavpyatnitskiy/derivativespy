import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def spread_bull_put(k1, k2, c1, c2):
    # check strike order
    if k1 >= k2:
        print("Long put cannot be greater than Short Put")
        return None

    # Long Put dataframe
    L1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k1 + 1, 1),
        "Profit from Long Put": k1 + c1 - c2 - np.arange(k1 - 5, k1 + 1, 1)
    })

    L2 = pd.DataFrame({
        "Stock Price": np.arange(k1 + 1, k2 + 6, 1),
        "Profit from Long Put": np.full(len(np.arange(k1+1, k2+6, 1)), c1-c2)
    })

    L = pd.concat([L1, L2], ignore_index=True)

    # Short Put dataframe
    S1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k2, 1),
        "Profit from Short Put": np.arange(k1 - 5, k2, 1) - k1 - 1
    })

    S2 = pd.DataFrame({
        "Stock Price": np.arange(k2, k2 + 6, 1),
        "Profit from Short Put": np.full(len(np.arange(k2, k2+6, 1)), k2-k1-c1)
    })

    S = pd.concat([S1, S2], ignore_index=True)

    # Merge by Stock Price
    DF = pd.merge(L, S, on="Stock Price")
    DF["Total Payoff"] = DF["Profit from Long Put"]+DF["Profit from Short Put"]

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
      DF["Profit from Long Put"],
      linestyle="--",
      linewidth=2,
      label="Long Put"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Short Put"],
      linestyle="--",
      linewidth=2,
      label="Short Put"
      )

    plt.axhline(0, color="black", linewidth=1)
    plt.grid(True, linestyle=":", color="grey")
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("P&L from Bull Spread using Puts")

    # annotations
    plt.text(k2, 3.25, f"Short Put, Strike Price of ${k2}")
    plt.text(k2, -1.75, f"Long Put, Strike Price of ${k1}")

    plt.legend()
    plt.show()

    return DF

spread_bull_put(30, 35, 1, 3) # Test
