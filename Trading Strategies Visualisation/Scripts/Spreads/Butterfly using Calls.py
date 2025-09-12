import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def spread_butterfly_call(k1, k2, k3, c1, c2, c3):
    # Check if strike prices are mixed up
    if k1 > k2 > k3:
        print("Incorrect values of strike prices")
        return None

    # First Long Call
    L1 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k1 + 1, 1),
        "Profit from First Long Call": -c1
    })
    extra1 = pd.DataFrame({
        "Stock Price": np.arange(k1 + 1, k3 + 6, 1),
        "Profit from First Long Call": np.arange(k1 - k3 + 1, k2 - k1 + 1, 1)
    })
    L1 = pd.concat([L1, extra1], ignore_index=True)

    # Second Long Call
    L2 = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k3 + 1, 1),
        "Profit from Second Long Call": -c3
    })
    extra2 = pd.DataFrame({
        "Stock Price": np.arange(k3 + 1, k3 + 6, 1),
        "Profit from Second Long Call": np.arange(1, k3 - k2 + 1, 1) - 5
    })
    L2 = pd.concat([L2, extra2], ignore_index=True)

    # Short Call
    S = pd.DataFrame({
        "Stock Price": np.arange(k1 - 5, k2 + 1, 1),
        "Profit from Short Call": c2
    })
    extra3 = pd.DataFrame({
        "Stock Price": np.arange(k2 + 1, k3 + 6, 1),
        "Profit from Short Call": c2 - np.arange(1, k3 - k1 + 1, 1)
    })
    S = pd.concat([S, extra3], ignore_index=True)

    # Merge dataframes
    DF = L1.merge(S, on="Stock Price").merge(L2, on="Stock Price")

    # Total Payoff
    DF["Total Payoff"] = DF["Profit from First Long Call"] + \
                         2 * DF["Profit from Short Call"] + \
                         DF["Profit from Second Long Call"]

    plt.figure(figsize=(10,6)) # Plot
    
    plt.plot(
      DF["Stock Price"],
      DF["Total Payoff"],
      label="Total Payoff",
      color="red",
      linewidth=3
      )

    plt.plot(
      DF["Stock Price"],
      DF["Profit from First Long Call"],
      linestyle="--",
      linewidth=1.5,
      label="First Long Call"
      )
    
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Short Call"],
      linestyle="--",
      linewidth=1.5,
      label="Short Call"
      )
    
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Second Long Call"],
      linestyle="--",
      linewidth=1.5,
      label="Second Long Call"
      )
    
    plt.text(k1 - 5, -c1+0.5, f"Long Call, Strike ${k1}")
    plt.text(k1 - 5, c2-1, f"Short Call, Strike ${k2}")
    plt.text(k1 - 5, -c3-1, f"Long Call, Strike ${k3}")
    
    plt.axhline(0, color="black", linewidth=1)  # Break-even line
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.title("P&L from Butterfly Spread using Calls")
    plt.legend()
    plt.show()
    
    return DF

spread_butterfly_call(55, 60, 65, 10, 7, 5) # Test
