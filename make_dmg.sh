#!/bin/sh
# Ref.: https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/

rm -rf build dist/*

#################################################
# Create app file using pyinstaller
#################################################

pyinstaller --name 'PhotoOrganizer' \
            --icon 'camera.ico' \
            --windowed  \
            main.py


#################################################
# Build the application bundle into a disk image
#################################################

# Create a folder (named dmg) to prepare our DMG in 
# (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -rf dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/PhotoOrganizer.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/PhotoOrganizer.dmg" && rm "dist/PhotoOrganizer.dmg"
create-dmg \
  --volname "PhotoOrganizer" \
  --volicon "camera.ico" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "PhotoOrganizer.app" 175 120 \
  --hide-extension "PhotoOrganizer.app" \
  --app-drop-link 425 120 \
  "dist/PhotoOrganizer.dmg" \
  "dist/dmg/"
