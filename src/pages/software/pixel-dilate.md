---
layout: ../../layouts/Layout.astro
name: Pixel Dilate
description: Pixel dilate or erode with circle, square, or diamond kernels.
icon: /web/icons/pixel-dilate.png
category: Shaders
download: /web/downloads/pixel-dilate.zip
---

Pixel dilate or erode with circle, square, or diamond kernels.

This shader expands highlights (or shadows) while keeping them at full brightness (or darkness).

![Screenshot](/web/screenshots/pixel-dilate-1.jpg)

## Parameters

  - **Radius**: Radius of dilation in pixels
  - **Mode**: Switch between Dilate (exand highlights) and Erode (expand shadows)
  - **Shape**: Circle, Square, or Diamond expansion
  - **Channels**: Which image channels the effect should be applied to (RGBA, RGB only, or Alpha Only)

## Installation

Unzip and place files into the */vol/.support/shaders* folder which is the same as
- **Linux:** /usr/fl/shaders
- **MacOS:** /Library/Application Support/FilmLight/shaders