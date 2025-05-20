# Superheavy Element Decay Modeling: Island of Stability Analysis

This project models alpha decay and spontaneous fission (SF) lifetimes for superheavy isotopes (Z = 114–121, A = 385–400), identifying viable synthesis targets near the theorized island of stability.

---

## 🔬 Methodology Overview

- **Qₐ (Alpha Decay Energy):** From a semi-empirical mass formula (SEMF)
- **Alpha Half-Life:** Calculated via the Geiger–Nuttall relation
- **Spontaneous Fission:** Estimated via Z²/A instability factor
- **Shell Effects:** Modeled as a ×10¹⁰ SF half-life boost for Z = 114, N = 184–196
- **Stability Score:**  
  \[
  \log_{10}\left(\frac{T_{1/2}^{\text{SF}}}{T_{1/2}^{\alpha}}\right)
  \]

---

## 📈 Key Findings

- Qₐ becomes favorable (Qₐ > 0) beginning around A ≈ 392
- Without shell suppression, SF dominates all isotopes
- With modeled suppression, **Flerovium-396 to 400** show positive stability scores and possible multi-step alpha chains

---

## 📄 Manuscript

- [`manuscript.tex`](manuscript.tex) — Full LaTeX source
- Compile in [Overleaf](https://overleaf.com) or locally with `pdflatex`
- Includes:
  - Appendix **B**: Computational methods (equations and constants)
  - Appendix **C**: Visualizations (heatmaps, bar chart)

---

## 💻 Code

The `/code` directory contains all Python scripts used in this study:

### `code/decay_model.py`
- Computes Qₐ, alpha half-life, SF half-life, and log₁₀ stability scores

### `code/generate_figures.py`
- Generates:
  - Qₐ heatmap
  - Decay mode dominance map
  - Adjusted stability score heatmap
  - Relative stability chart for Flerovium

---

**Author**: Aidan Fumagalli  
Modeling and tooling support via OpenAI

---

## 📬 Contact

Open to collaboration, feedback, or experimental proposals — feel free to fork, cite, or reach out via GitHub.
