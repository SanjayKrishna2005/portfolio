# Sanjay Krishna — AI Hardware & Neuromorphic ASIC Engineering Portfolio

Personal engineering website and hardware portfolio of Sanjay Krishna, specializing in AI hardware architecture, edge accelerators, neuromorphic ASICs, event-driven spiking neural networks, and physical reverse engineering.

---

## ⚡ Key Highlights on this Site

* **Monolithic Bitstream Morph Title**: Interactive binary $\leftrightarrow$ ASCII header cycling between `SANJAY KRISHNA` and `TWENTY WATTS`.
* **Cycle-Accurate LIF Spiking Neuron Simulator**: Directly models the SkyWater 130nm ASIC (`tt_um_snn_afib_detector.v`) submitted to Tiny Tapeout 09, featuring:
  * 16-bit tick prescaler & $RR$ interval / $\Delta RR$ HRV rate-spike encoder.
  * 8-LIF neuron reservoir matrix with arithmetic right-shift leak (`potential >> 1`).
  * 1-bit recurrent feedback flip-flop (`spike_reg1` linking $N_0 \to N_7$).
  * Dual-window majority voting (8-beat FAST and 16-beat SLOW coincidence gate).
  * Real-time ECG CRT oscilloscope & 8-channel spike raster display.
* **Hardware Architecture Logs & Post-Mortems**:
  * Micro-architecture in 959 Standard Cells (Tiny Tapeout 09).
  * Reversing the Jane Street ASIC Layout with DCI Graph Isomorphism and Z3 SMT Solving.
  * The Thermodynamics of 20 Watts (Event-driven sparsity vs synchronous clock tree power).
  * Precision-Scalable Systolic Compute (PSMAC 4×4 NPU from gate primitives with per-row runtime INT8/4/2 precision).
* **Interactive Silicon Specimen Deck**: Live pin inspection for real taped-out and synthesized circuits.
* **Breaking Bad Easter Egg**: Dedicated theme playback mode.

---

## 🚀 How to Host for Free via GitHub Pages

### Option A: Via GitHub Web Interface (Simplest & Recommended)

1. Create a new public repository on GitHub (e.g. `sanjaykrishna.github.io` or `portfolio`).
2. Push this repository to GitHub:
   ```bash
   git remote add origin https://github.com/SanjayKrishna2005/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```
3. In your GitHub repository:
   * Go to **Settings** &rarr; **Pages** (under "Code and automation" in the left sidebar).
   * Under **Build and deployment** &rarr; **Source**:
     * Select **Deploy from a branch**.
     * Under **Branch**, select `main` and folder `/ (root)`.
     * Click **Save**.
4. In about 30–60 seconds, your website will be live at:
   `https://SanjayKrishna2005.github.io/<repo-name>/`
   *(Or `https://SanjayKrishna2005.github.io` if the repo is named `SanjayKrishna2005.github.io`)*.

---

### Option B: Via GitHub Actions Workflow

The repository includes a ready-to-use GitHub Pages Actions workflow in `.github/workflows/deploy.yml`.
* In **Settings** &rarr; **Pages** &rarr; **Source**, simply choose **GitHub Actions**.
* Every push to `main` will automatically build and deploy the website.

---

## 🛠 Local Development

Open `index.html` directly in any modern web browser, or run a local static server:

```bash
# Python 3
python3 -m http.server 8000

# Node.js
npx serve .
```

Navigate to `http://localhost:8000`.
