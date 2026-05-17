---
layout: ../../layouts/Layout.astro
name: Delete Old Galleries
description: Delete old gallery scenes from the job database (based on modified date)
icon: /web/icons/delete-old-galleries.png
category: App Scripts
download: /web/downloads/delete-old-galleries.zip
---

Delete old gallery scenes from the job database (based on modified date)

![Screenshot](/web/screenshots/delete-old-galleries-1.jpg)

## How To Use

Select *Delete Old Galleries* from under the main *Baselight* menu.

If you're not using the default "baselight_gallery" job for your galleries, you'll need to edit the script with your custom job name (matching your _Prefences > Cuts View, Gallery and Scratchpad > Gallery Job_ setting).

## Installation

Place `DeleteOldGalleries.py` into the */vol/.support/scripts* folder which is the same as
- **Linux:** /usr/fl/scripts
- **MacOS:** /Library/Application Support/FilmLight/scripts

Restart Baselight or select *Views > Scripts > <span style="display:inline-block; vertical-align: middle;">![Gear](/web/gear.png)</span> > Reload Scripts…* to load.