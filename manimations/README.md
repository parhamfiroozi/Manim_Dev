# Simulation Theory — Manim Intro

**A cinematic Manim (Community Edition) animation blending simulation theory, Persian calligraphy, a real-time convolution demo, and a warped-star constellation sequence.**

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Manim](https://img.shields.io/badge/manim-ce-v0.18.1-brightgreen)
![License](https://img.shields.io/badge/license-MIT-yellow)

> Crafted with precision for [`simulationtheory.ir`](https://simulationtheory.ir) — a personal brand exploring the simulation hypothesis through code and motion.

---

https://github.com/user-attachments/assets/ … *(replace with an actual GIF or video link once rendered)*  

---

## 📽 About the Project

This repository contains a fully‑featured Manim scene (`SimulationTheoryDev`) that serves as a **brand intro + technical showcase**.  
It was created to demonstrate:

- **Right‑to‑left (Persian/Farsi) typography** in a mathematical animation environment using XeLaTeX + XePersian.
- **A live, shaded convolution integral** — a rectangle sliding against a decaying exponential, with the output traced in real‑time.
- **A warped Cartesian grid** that reacts to time, overlaid with a golden infinity‑shaped constellation and drifting background stars.
- **Glitch effects, matrix rain, and a dramatic camera zoom** to finalise the piece.

The scene is fully self‑contained; running it with Manim renders the entire sequence at 1080p (or higher) in a few minutes.

---

## 🧩 Scene Breakdown

| Segment                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Digital Rain**       | Matrix‑style falling glyphs (Japanese, Greek, binary) that flicker before fading out. |
| **Glitch Title**       | “SIMULATION THEORY” glitches randomly, then shrinks to the top‑left corner. |
| **Persian Intro**      | Three Farsi lines slide in from the right, introducing the developer and the domain. |
| **Convolution in Action** | A real convolution example with shaded overlap between `x(τ)` and `h(t-τ)`, plus the resulting `y(t)`. |
| **Star Constellation & Warp** | A NumberPlane bends like a rubber sheet while an infinity‑shaped star constellation rises and rotates. |
| **Signature Outro**    | Name, underline, Farsi tagline, domain, and a slow camera push‑in.         |

All transitions between sections are smooth; Persian text enters from the right (RTL) and exits to the left, mimicking natural reading direction.

---

## ⚙️ Requirements

- **Python** ≥ 3.10
- **Manim** (Community Edition) – install with `pip install manim`
- **XeLaTeX** – required for Persian text rendering.  
  On Ubuntu: `sudo apt install texlive-xetex`  
  On macOS: install MacTeX, then update your PATH.
- **XePersian** package – part of TeXLive (`tlmgr install xepersian` if missing).
- **Vazirmatn** font – download from [Vazirmatn GitHub](https://github.com/rastikerdar/vazirmatn) and install it on your system.

Optionally, a video player that supports 60fps to appreciate the smooth animations.

---

## 🚀 Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/simulation-theory-manim.git
   cd simulation-theory-manim