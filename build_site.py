#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

REPO_PATH = './enhancements'
REPO_NAME = 'FilmLightAPI/enhancements'
error_count = 0

## Put files in a downloadable ZIP
def generate_zip(folder, short_name):
    zipPath = "../../../public/downloads/" + short_name + ".zip"
    try:
        if os.path.exists(zipPath):
            os.remove(zipPath)
        subprocess.run([
            "zip", "-r", zipPath,
            ".",
            "-x", ".*", "*.mp4", "icon.png", "README.md", "screenshot-*" ],
            check=True, cwd=folder)
    except subprocess.CalledProcessError:
        print(f"ERROR: Unable to generate zip file for *{folder}*")
        global error_count
        error_count += 1

## Generate .md file used by Astro to build web page
def generate_md(folder, sub_name, short_name):
    with open(REPO_PATH + '/' + folder + '/' + sub_name + "/README.md", "r") as src, open("./src/pages/software/" + short_name + ".md", "w") as dst:
        bigName = short_name
        descripton = ""
        for line in src:
            if not line.strip():  # empty
                continue
            if line.startswith("#"):
                bigName = line.rstrip()[2:]
            else:
                description = line.rstrip()
                break
                
        frontmatter = [
            "---",
            "layout: ../../layouts/Layout.astro",
            f"name: {bigName}",
            f"description: {description}",
            f"icon: /web/icons/{short_name}.png",
            "category: " + folder,
            f"download: /web/downloads/{short_name}.zip",
            "---",
            "",
            description,
            "",
        ]
        dst.write("\n".join(frontmatter))
        
        for line in src:
            if line.startswith("![Screenshot]"):
                line = line.replace("screenshot-1.jpg", f"/web/screenshots/{short_name}-1.jpg")
            elif line.startswith("[Video]"):
                start = line.find('(') + 1
                end = line.find(')')
                line = '<video style="max-width: 100%; height: auto;" controls><source src="' + line[start:end] + '" type="video/mp4"></video>'
            dst.write(line)

## Copy icons and screenshots into Astro repository
def copy_images(folder, short_name):
    if os.path.exists(folder + '/icon.png'):
        shutil.copy(folder + '/icon.png', './public/icons/' + short_name + '.png')
    if os.path.exists(folder + '/screenshot-1.jpg'):
        shutil.copy(folder + '/screenshot-1.jpg', './public/screenshots/' + short_name + '-1.jpg')

## Iterate through the enhancement subfolders 
def process_folder(folder):
    folderPath = REPO_PATH + '/' + folder
    with os.scandir(folderPath) as enhancements:
        for enhancement in enhancements:
            if enhancement.name == ".DS_Store" or enhancement.name == ".ruff_cache":
                continue
            print(enhancement.name)
            short_name = enhancement.name.lower().replace(" ", "-")
            ## TODO: Remove files for enhancements removed from repository
            generate_zip(folderPath + '/' + enhancement.name, short_name)
            generate_md(folder, enhancement.name, short_name)
            copy_images(folderPath + '/' + enhancement.name, short_name)


## Main
# Pull latest version or repository
if not os.path.exists(REPO_PATH):
    try:
        subprocess.run(["gh", "repo", "clone", REPO_NAME], check=True)
    except subprocess.CalledProcessError:
        print("ERROR: Unable clone github repo. Is GitHub CLI installed?")
        sys.exit()
else:
    try:
        subprocess.run(["git", "pull"], check=True, cwd=REPO_PATH)
    except subprocess.CalledProcessError:
        print("ERROR: Unable to pull git updates.")
        sys.exit()

# Update descriptions, downloads, and graphics
folders = ["App Scripts", "FLAPI Tools", "Shaders"];
for folder in folders:
    process_folder(folder)

# Rebuild the web pages and push changes to GitHub
if error_count == 0:
    try:
        subprocess.run(["npm", "run", "build"], check=True, cwd=REPO_PATH)
    except subprocess.CalledProcessError:
        print("ERROR: Website build failed.")
else:
    print("STOPPED: Skipped building web-page, there were errors.")