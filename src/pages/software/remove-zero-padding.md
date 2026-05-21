---
layout: ../../layouts/Layout.astro
name: Remove Zero Padding
description: Remove leading '0's from Scene and Take metadata.
icon: /web/icons/remove-zero-padding.png
category: App Scripts
download: /web/downloads/remove-zero-padding.zip
---

Remove leading '0's from Scene and Take metadata.

For dailies, Scene and Take metadata imported from audio files often has leading zeros, which some editors ask be removed. This script quickly removes them for all shots in the current Daylight/Baselight scene.

Access **Remove Zero Padding** under the <span style="display:inline-block; vertical-align: middle;">![Gear](/web/gear.png)</span> menu in Shots view.

## Installation

Place `RemoveZeroPadding.py` into the */vol/.support/scripts* folder which is the same as
- **Linux:** /usr/fl/scripts
- **MacOS:** /Library/Application Support/FilmLight/scripts

Restart Baselight or select *Views > Scripts > <span style="display:inline-block; vertical-align: middle;">![Gear](/web/gear.png)</span> > Reload Scripts…* to load.