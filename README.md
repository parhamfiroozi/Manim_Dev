# Manim_Dev

A cinematic Manim Community Edition project that showcases a branded animation combining Persian calligraphy, a real-time convolution demo, and a dynamic warped-star sequence.

## Overview

This repository contains a Manim scene that blends:

- Persian (Farsi) typography using XeLaTeX + XePersian
- Live convolution visualization with shading and animated integrals
- A warped Cartesian grid and animated star constellation
- Glitch effects, digital rain, and cinematic camera motion

The actual animation code lives in the `manimations/` folder.

## Requirements

- Python 3.10+
- Manim Community Edition
- XeLaTeX for Persian text rendering
- XePersian TeX package
- System font: Vazirmatn (or another Persian-capable font)

## Install

```bash
cd manimations
python -m pip install -r requirements.txt
```

> If `requirements.txt` is not present, install Manim directly:
> `python -m pip install manim`

## Usage

From the `manimations/` directory:

```bash
python -m manim main.py SimulationTheoryDev -ql
```

Replace `-ql` with `-qp` or `-qh` for higher quality renders.

## Project Structure

- `manimations/main.py` — Main Manim scene and animation logic
- `manimations/pyproject.toml` — Python project metadata and dependencies
- `manimations/README.md` — Detailed animation description and requirements

## License

This project is licensed under the MIT License. See `LICENSE` for details.
