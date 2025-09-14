import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def spread_butterfly_put(k1, k2, k3, c1, c2, c3, save_plot=True):
    
    if (k1 >= k2) and (k2 >= k3) and (k1 >= k3):
        print("Incorrect values for strike prices")
        return None
    
    # --- First Long Put (L1) ---
    s1 = np.arange(k1 - 5, k1)                          
    seq1 = 1 - np.arange(1, (k2 - k1) + 1)              
    profit1 = np.resize(seq1, s1.shape[0])              
    
    s2 = np.arange(k1, k3 + 6)                          
    profit2 = np.full(s2.shape[0], -c1, dtype=int)      
    
    stock_L1 = np.concatenate([s1, s2])
    profit_L1 = np.concatenate([profit1, profit2])
    L1 = pd.DataFrame({"Stock Price": stock_L1,
                       "Profit from First Long Put": profit_L1})
    
    # --- Short Put (S) ---
    s3 = np.arange(k1 - 5, k2)                          
    profit_s1 = s3 - k2 + c2
    
    s4 = np.arange(k2, k3 + 6)                          
    profit_s2 = np.full(s4.shape[0], c2, dtype=int)
    
    stock_S = np.concatenate([s3, s4])
    profit_S = np.concatenate([profit_s1, profit_s2])
    S = pd.DataFrame({"Stock Price": stock_S,
                      "Profit from Short Put": profit_S})
    
    # --- Second Long Put (L2) ---
    s5 = np.arange(k1 - 5, k3)                          
    seq_len = (k3 - k1) + c3 - 5
    seq2 = c3 - np.arange(1, seq_len + 1) - 4
    profit_l2_part1 = np.resize(seq2, s5.shape[0])
    
    s6 = np.arange(k3, k3 + 6)                          
    profit_l2_part2 = np.full(s6.shape[0], -c3, dtype=int)
    
    stock_L2 = np.concatenate([s5, s6])
    profit_L2 = np.concatenate([profit_l2_part1, profit_l2_part2])
    L2 = pd.DataFrame({"Stock Price": stock_L2,
                       "Profit from Second Long Put": profit_L2})
    
    # --- Merge ---
    DF = pd.merge(L1, S, on="Stock Price")
    DF = pd.merge(DF, L2, on="Stock Price")
    DF = DF.sort_values("Stock Price").reset_index(drop=True)
    DF.index = np.arange(1, len(DF) + 1)  # R-style 1-based index
    
    # Total payoff
    DF["Total Payoff"] = (
        DF["Profit from First Long Put"]
        + 2 * DF["Profit from Short Put"]
        + DF["Profit from Second Long Put"]
    )
    
    # --- Plot ---
    plt.figure(figsize=(10,6))
    
    plt.plot(
      DF["Stock Price"],
      DF["Total Payoff"],
      linewidth=5,
      color="red",
      label="Total Payoff"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from First Long Put"],
      linestyle="--",
      linewidth=2,
      label=f"Long Put, Strike ${k1})"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Short Put"],
      linestyle="--",
      linewidth=2,
      label=f"Short Put, Strike ${k2})"
      )
      
    plt.plot(
      DF["Stock Price"],
      DF["Profit from Second Long Put"],
      linestyle="--",
      linewidth=2,
      label=f"Long Put, Strike ${k3})"
      )
    
    plt.text(k3, -c1+.5, f"Long Put, Strike ${k1}")
    plt.text(k3, c2-1, f"Short Put, Strike ${k2}")
    plt.text(k3, -c3+.5, f"Long Put, Strike ${k3}")
    
    plt.axhline(0, color="black", linewidth=1)
    plt.title("P&L from Butterfly Spread using Puts")
    plt.xlabel("Stock Price ($)")
    plt.ylabel("Profit ($)")
    plt.grid(linestyle="--", alpha=0.6)
    
    plt.show()
    
    return DF

spread_butterfly_put(55, 60, 65, 5, 7, 10)
