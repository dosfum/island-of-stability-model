import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_heatmap(data, title, filename, cmap="Spectral", cbar_label=""):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, cmap=cmap, cbar_kws={"label": cbar_label}, center=0 if "Score" in title else None)
    plt.title(title)
    plt.xlabel("Z")
    plt.ylabel("A")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

def plot_relative_stability(masses, scores, filename):
    plt.figure(figsize=(8, 5))
    plt.barh(masses, scores, color="steelblue")
    plt.xlabel("Relative Adjusted Stability Score (Δ log10)")
    plt.ylabel("Mass Number (A)")
    plt.title("Flerovium (Z = 114): Relative Stability Gain")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()