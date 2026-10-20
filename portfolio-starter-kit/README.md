# Engineering Portfolio Architecture & Playbook
### *How to Build a High-Impact, Minimalist Technical Portfolio (From First Principles)*

> **Who this guide is for**: An engineer who wants a personal website that stands out instantly to recruiters, research directors, and senior engineering leads. This is not a generic tutorial for a template; it is a breakdown of every design, content, and architectural decision behind this portfolio.

---

## 📑 Table of Contents
1. [The Core Philosophy: Precision Instrument vs. Generic SaaS](#1-the-core-philosophy)
2. [UI & Visual Perspective: Every Decision Explained](#2-ui--visual-perspective)
   - [The Color Palette: Raw Copper & Champagne Gold](#21-the-color-palette)
   - [Typography: Editorial Authority Meets Silicon Telemetry](#22-typography)
   - [Hero Image Placement: The Ambient Edge Bleed (No Passport Card)](#23-hero-image-placement)
   - [The Decluttering Decisions: What We Deliberately Removed](#24-decluttering-decisions)
   - [Micro-Interactions: Silicon Background & Live Clock Domain](#25-micro-interactions)
3. [Content & Storytelling Perspective: How to Sell Your Engineering](#3-content--storytelling-perspective)
   - [The Hook: First-Principles Framing in Under 3 Seconds](#31-the-hook)
   - [Project Framing: The 4-Part Architecture Formula](#32-project-framing)
   - [The Signature Interactive Demo (The Anchor Widget)](#33-the-signature-interactive-demo)
   - [Technical Deep Dives (Blog): Writing About Bugs & Silicon Zero-Days](#34-technical-deep-dives)
4. [Code Architecture: Why Zero-Build Static HTML is a Superpower](#4-code-architecture)
5. [Step-by-Step Customization Guide for Your Own Portfolio](#5-step-by-step-customization-guide)
6. [Free Deployment via GitHub Pages (5 Minutes)](#6-free-deployment-via-github-pages)

---

## 1. The Core Philosophy: Precision Instrument vs. Generic SaaS

Most engineer portfolios make one of two mistakes:
1. **The Academic Resume Dump**: A stark white HTML document that looks like a plain PDF resume exported to the web. It has zero personality and doesn't showcase design taste or attention to detail.
2. **The Over-Engineered SaaS Template**: Built with heavy React/Next.js frameworks, pastel gradient buttons, generic stock icons, and animated cards that look like a cryptocurrency startup or a generic B2B landing page.

### Our Guiding Principle:
> **"Treat the website like a piece of high-precision laboratory test equipment."**

When someone opens this website, the visual cues evoke high-end instruments (like Rohde & Schwarz logic analyzers, HP/Agilent cathode-ray oscilloscopes) and physical silicon packaging (FR4 printed circuit boards, exposed copper routing traces, gold wirebonding).

This immediately signals to the visitor:
* *This person understands low-level physical realities.*
* *This person pays obsessive attention to craft and constraints.*
* *This person doesn't rely on generic boilerplate.*

---

## 2. UI & Visual Perspective: Every Decision Explained

### 2.1 The Color Palette: Raw Copper & Champagne Gold
Many dark-mode websites use blinding neon orange, bright blue, or pure jet black (`#000000`). Pure black feels harsh, creates high-contrast eye fatigue, and feels empty.

We engineered **Palette 3 (Raw Copper & Champagne Gold)**:

| Semantic Role | Hex Code | Visual Inspiration | Purpose / Why Chosen |
|---|---|---|---|
| **Deep Chassis Background** | `#111215` | Matte carbon charcoal | Absorbs ambient contrast; significantly softer on the eyes than `#000000`. |
| **Console / Card Surface** | `#191a1f` | Anodized equipment chassis | Creates a crisp layer of elevation without needing drop shadows. |
| **Silkscreen / Grid Borders**| `#2b2c34` & `#353640` | PCB silkscreen lines | Subtle grid definition; frames oscilloscope displays without visual noise. |
| **Primary Trace Accent** | `#e07a5f` | Raw etched copper / terracotta | Warm, grounded, organic accent representing physical circuit traces. |
| **Secondary Accent** | `#e6c280` | Wirebonding champagne gold | High-precision contrast element; used for delta spikes and critical tags. |
| **Primary Headings & Text** | `#f7f4ee` | Warm bone cream | Warm off-white; readable without the piercing glare of `#ffffff`. |
| **Telemetry & Metadata** | `#a2a09c` | Muted silver nickel | Clear secondary hierarchy for status lines, registers, and sub-labels. |

> **Key Rule for Your Friend**: Choose **one primary accent** and **one secondary accent** rooted in your engineering discipline. If you do RF/Radar, consider Phosphor Emerald (`#10b981`). If you do Aerospace/Quantum, consider Ice Cyan (`#38bdf8`) or Violet. Never use more than 2 saturated colors simultaneously.

---

### 2.2 Typography: Editorial Authority Meets Silicon Telemetry
Instead of a single default font like `Inter` or `Arial`, we paired two contrasting typographic voices:

1. **Editorial Display Voice (`EB Garamond`)**:
   - Used for main section headers, narrative quotes, and philosophical anchors.
   - Why: A classic serif typeface brings academic weight, serious literary tone, and immediate intellectual authority. It breaks the "tech-bro" monospace monotony.
2. **Silicon Telemetry Voice (`JetBrains Mono` & `Silkscreen`)**:
   - Used for register values, FSM states, pinouts, clock frequencies, and formulas.
   - Why: Fixed-width monospacing aligns columns cleanly, mimics oscilloscope readouts, and gives telemetry data an authentic hardware look.

---

### 2.3 Hero Image Placement: The Ambient Edge Bleed (No Passport Card)
The most common mistake on personal websites is placing a small, centered, 150×150 circular photo with a harsh border that looks like an ID card or LinkedIn badge.

#### How We Solved It:
1. **Oversized & Edge-Anchored**: The portrait is positioned in the **absolute top-right corner**, scaling from 420px up to 680px on desktop screens.
2. **Dual-Axis CSS Gradient Mask (The "Bleed Effect")**:
   Instead of a hard border, the image is faded using a directional alpha mask:
   ```css
   .hero-portrait-frame {
     /* Fades bottom 32% softly into chassis background */
     -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 68%, rgba(0,0,0,0) 100%);
     mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 68%, rgba(0,0,0,0) 100%);
   }
   .hero-portrait-img {
     /* Fades left edge across 0% to 75% so text floats effortlessly on top */
     -webkit-mask-image: linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,0.25) 20%, rgba(0,0,0,0.88) 48%, rgba(0,0,0,1) 75%);
     mask-image: linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,0.25) 20%, rgba(0,0,0,0.88) 48%, rgba(0,0,0,1) 75%);
   }
   ```
3. **The Result**: Your face blends naturally into the dark carbon background as if it were etched into the chassis itself. Text on the left remains 100% legible, and the screen feels expansive.
4. **Multi-Format Image Pipeline**:
   Browsers on iOS/Safari can fail if a PNG file is accidentally named `.jpeg`. We generate true format copies (`photo.png`, `photo.jpeg`, `photo.jpg`, `photo.webp`) and use a resilient fallback handler:
   ```javascript
   function handlePhotoFallback(img) {
     const path = new URL(img.src, window.location.href).pathname.toLowerCase();
     if (path.endsWith('photo.jpeg')) img.src = 'photo.png';
     else if (path.endsWith('photo.png')) img.src = 'photo.jpg';
     else if (path.endsWith('photo.jpg')) img.src = 'photo.webp';
   }
   ```

---

### 2.4 Decluttering Decisions: What We Deliberately Removed
Great design is defined as much by what you remove as what you add:
1. **Removed the "Cinema Deck" & Desk Notes**: Earlier revisions had decorative badges and sticky desk notes that competed with the main project content. Removing them let the typography and projects breathe.
2. **Removed the `[MORPH]` Button**: We originally had a small sync button next to the hero headline. It felt like an unnecessary UI gimmick. We removed the button, allowing the title to morph smoothly on an automatic ambient cycle while still allowing a manual click directly on the headline.
3. **Eliminated Intrusive Audio**: Avoid autoplay sound effects or chime noises during page navigation. Users find involuntary sound jarring. Keep audio strictly optional (e.g., inside an explicit lab controller or synthesizer dock).

---

### 2.5 Micro-Interactions: Silicon Background & Live Clock Domain
Subtle interactive details reward curious visitors without being distracting:
1. **Interactive Silicon Wafer Traces (`#silicon-bg-canvas`)**:
   A lightweight HTML5 canvas script animates orthogonal circuit routing lines in the background. When the user moves their mouse, nearby trace nodes glow softly in raw copper (`#e07a5f`).
2. **Top-Bar Clock Waveform (`#clock-canvas`)**:
   A live square wave pulses in the navigation bar. Clicking it cycles the clock domain between `10 MHz` (Tiny Tapeout ASIC), `166 MHz` (FPGA interconnect), and `1.2 GHz` (Deep compute), playing a gentle synthesized blip via Web Audio API.

---

## 3. Content & Storytelling Perspective: How to Sell Your Engineering

### 3.1 The Hook: First-Principles Framing in Under 3 Seconds
Recruiters spend an average of **6 to 8 seconds** reviewing a candidate's portfolio. If your site opens with:
> *"Hello! I am a computer science student passionate about technology and problem solving."*

...you have already lost them. That describes 200,000 other graduates.

#### Our Hook:
> **"I have a favourite chip, and it isn't made of silicon. It's the one you're using to read this sentence."**

This hook works because:
1. It immediately anchors the narrative in biology vs silicon (the 20-Watt human brain).
2. It sets up an intellectual thesis: modern computing is choked by clock trees and brute-force power, whereas biological event-driven computing is the future.
3. It makes the reader want to scroll down to see how you prove that claim.

> **Challenge for Your Friend**: What is the core contradiction or paradox in your field?
> - *Embedded*: "Microcontrollers are everywhere, but 99% of their clock cycles are spent waiting for slow sensors. Here is how I make silicon sleep until it matters."
> - *Robotics*: "A robot doesn't fail because its motors aren't strong; it fails because its perception loop is 50 milliseconds too slow."
> - *Backend*: "Writing code that scales to 1,000 users is trivial. Writing code that doesn't melt your database when 50,000 requests hit simultaneously requires understanding hardware caches."

---

### 3.2 Project Framing: The 4-Part Architecture Formula
Never list projects as generic bullet points ("Built a calculator", "Made an edge detector").

Structure every project showcase using the **4-Part Architecture Formula**:

```
[1. The Problem / Real-World Context]
       │
       ▼
[2. The Architectural Constraint / Bottleneck]
       │
       ▼
[3. The Engineering Innovation / Trade-off Made]
       │
       ▼
[4. The Quantifiable Telemetry (Hard Numbers)]
```

#### Example Breakdown from this Portfolio:

* **Bad Description**: *"Created an Atrial Fibrillation detector in Verilog for an ASIC competition."*
* **Our Formulation**:
  1. *Context*: Cardiac arrhythmia detection requires continuous, 24/7 edge monitoring on wearable patients without depleting a coin-cell battery.
  2. *Constraint*: Tiny Tapeout 09 allocates exactly a single $160 \times 100\,\mu\text{m}$ tile: approximately 1,000 standard cells and zero DSP multiplier blocks. Conventional machine learning neural networks consume 200+ cells for a single 8-bit multiplier.
  3. *Innovation*: Formulated an integer Leaky Integrate-and-Fire neuron where continuous exponential decay is replaced by a hardware arithmetic right-shift by 1 (`potential >> 1`). Because wire shifts consume zero logic gates, each neuron synthesized to **only 24 standard cells**.
  4. *Quantified Telemetry*:
     - **Cell Count**: 959 / 1,000 cells (41 cells to spare).
     - **Operating Frequency**: 10.0 MHz (Setup Slack: +42.1 ns).
     - **Quiescent Power**: 8.4 nW between beats.
     - **Core Utilization**: 48.7%, Zero DRC/LVS violations.

---

### 3.3 The Signature Interactive Demo (The Anchor Widget)
If your website only has static text and GitHub links, visitors have to leave your site and clone your code to see if it works (which 99% will never do).

**Having one live interactive widget in the browser keeps visitors engaged for minutes.**

On this site, we built the **Cycle-Accurate LIF Spiking SNN Simulator**:
* A simulated CRT oscilloscope displays the analog ECG heartbeat signal.
* An 8-channel spike raster shows individual biological neurons firing in real-time.
* Users can click buttons to inject an **Arrhythmic AFib burst**, an **Isolated PVC beat**, or an **Asystole flatline** and watch the internal 4-bit neuron potential bars charge, decay, and trigger majority coincidence voting.

> **Ideas for Your Friend's Signature Demo**:
> - **Embedded / IoT**: An interactive state machine visualizer or sensor filtering simulator (Kalman / Low-Pass filter slider).
> - **VLSI / Logic Design**: An interactive logic gate timing diagram generator or truth-table solver.
> - **Robotics**: A 3D kinematics arm simulator using Three.js or a real-time 2D pathfinding grid (A* / Dijkstra).
> - **Computer Vision**: An interactive image kernel convolution matrix (Sobel, Gaussian blur, Sharpen) running live on webcam feed or sample canvas.

---

### 3.4 Technical Deep Dives (Blog): Writing About Bugs & Silicon Zero-Days
Don't write high-level tutorial blogs like *"Getting Started with Verilog"*. Write about **real bugs, failure modes, and debugging journeys**.

In our Blog Post 2:
> *"Reverse Engineering a Physical ASIC Layout: Extracting Zero-Days with Graph Isomorphism and Z3 SMT Solving"*

We detailed:
1. Why MOSFET Source and Drain terminals are geometrically symmetric in planar CMOS, causing standard subgraph isomorphism algorithms (VF2) to fail.
2. How we invented the **Degree of Connectivity Index (DCI)** to produce an invariant topological fingerprint.
3. How unrolling 122 clock cycles into the **Z3 SMT solver** exposed a hardware race condition on Pin 42 where the chip violated the rules of the Star Battle puzzle.

**Why this matters**: Senior engineers and hiring managers respect candidates who know how to decompile, debug, and reason under failure.

---

## 4. Code Architecture: Why Zero-Build Static HTML is a Superpower

Modern web development has a disease: installing 400 MB of `node_modules` just to render a personal homepage.

### Why We Chose a Single Clean `index.html` Architecture:
1. **Zero Maintenance Burden**: There are no dependencies that break when Node.js updates 12 months from now. It will render identically in 2035.
2. **Lightning Load Times**: Hosted directly from GitHub's CDN edge. First Contentful Paint is typically **< 180 ms**.
3. **Tailwind CSS via CDN with Semantic Theme Extension**:
   All colors are defined once inside `tailwind.config` in the `<head>`:
   ```javascript
   tailwind.config = {
     darkMode: 'class',
     theme: {
       extend: {
         colors: {
           "dark-bg": "#111215",
           "dark-surface": "#191a1f",
           "dark-border": "#2b2c34",
           "dark-text": "#f7f4ee",
           "dark-text-muted": "#a2a09c",
           copper: { 500: '#e07a5f' },
           gold: { 500: '#e6c280' }
         }
       }
     }
   }
   ```
4. **Vanilla JS SPA Router**:
   Switching between `HOME`, `PROJECTS`, `SIMULATOR`, and `BLOG` is handled with zero full-page reloads using a lightweight JavaScript router:
   ```javascript
   function navigateTo(pageId) {
     document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
     document.getElementById('page-' + pageId).classList.add('active');
     window.scrollTo({ top: 0, behavior: 'smooth' });
   }
   ```

---

## 5. Step-by-Step Customization Guide for Your Own Portfolio

To adapt this template for yourself:

1. **Step 1: Replace Your Name & Identity**
   - Search for `Sanjay Krishna` in `index.html` and replace it with your full name.
   - Update the `<title>` and `<meta name="description">` tags in the `<head>`.
2. **Step 2: Add Your Portrait Photo**
   - Save your photo as `photo.png` or `photo.jpg` in the root folder.
   - Run our Python script (included in this folder) to generate optimized `photo.jpeg`, `photo.jpg`, and `photo.webp` formats.
   - Your face will automatically blend into the top right corner with the gradient mask!
3. **Step 3: Define Your Own Narrative Hook**
   - Edit the hero headline (`#title-line-1` and `#title-line-2`).
   - Edit the 3 opening paragraphs in `#page-home` to reflect your specific engineering obsession.
4. **Step 4: Update Your Flagship Projects**
   - Under `#page-projects`, replace the 4 project cards with your own work.
   - Ensure each project includes:
     - Clear GitHub / Tapeout link.
     - 4-item technical specs grid (e.g. Speed, Footprint, Power, Toolchain).
     - Architecture block diagram or key code snippet.
5. **Step 5: Customize Your Signature Interactive Widget**
   - Under `#page-simulator`, modify the canvas and control buttons to simulate something unique to your domain.

---

## 6. Free Deployment via GitHub Pages (5 Minutes)

You never have to pay for hosting:

1. **Create a GitHub Repository**:
   - Create a new public repo named `portfolio` (or `<your-username>.github.io`).
2. **Push Your Files**:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
3. **Enable GitHub Pages**:
   - Go to your repository on GitHub.
   - Click **Settings** $\rightarrow$ **Pages** (in the left sidebar).
   - Under **Build and deployment $\rightarrow$ Branch**, select **`main`** and **`/ (root)`**.
   - Click **Save**.
4. **Live in 60 Seconds**:
   - Your website will be permanently live for free at:
     `https://<your-username>.github.io/<your-repo-name>/`
   - Every time you push a change with `git push`, GitHub will automatically re-deploy your site.

---

*Authored with care for engineering peers who value craft, minimal aesthetics, and first-principles design.*
