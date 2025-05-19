# Superheavy Element Decay Modeling: Island of Stability Analysis

This project presents a predictive decay analysis across superheavy isotopes (Z = 114–121, A = 385–400) to identify candidates with potential alpha-stable behavior near the hypothesized island of stability.

---

## 🔬 Methodology

- **Qₐ Energetics** estimated using a semi-empirical mass formula (SEMF)
- **Alpha Decay Half-Lives** from the Geiger–Nuttall law
- **Spontaneous Fission (SF)** modeled via Z²/A instability heuristic
- **Shell Correction** applied for Z = 114, N = 184–196 using a ×10¹⁰ SF half-life boost
- **Stability Score**:  
  \[
  \log_{10}\left(\frac{\text{SF Half-Life}}{\text{Alpha Half-Life}}\right)
  \]

---

## 📈 Key Results

- Qₐ becomes energetically favorable above A ≈ 392
- Without shell suppression, SF dominates all isotopes
- With suppression modeled, **Flerovium-396 to 400 (Z = 114)** show positive stability scores
- These isotopes are proposed as synthesis candidates for observing measurable alpha decay chains

---

## 📄 Manuscript

> Full LaTeX manuscript and figures included in this repo:  
➡️ [`manuscript.tex`](manuscript.tex)  
➡️ Compile it via [Overleaf.com](https://overleaf.com) or LaTeX locally to view the PDF

---

## 🔍 Appendix B: Computational Details

Included in the manuscript:
- Full SEMF equation for Qₐ
- Geiger–Nuttall constants used
- SF decay modeling assumptions
- Shell suppression heuristic implementation

---

**Author**: Aidan Fumagalli  
With predictive modeling support from OpenAI tools
