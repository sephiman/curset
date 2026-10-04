#!/bin/sh
# SPDX-License-Identifier: AGPL-3.0-only
# Renders the Curset artwork in src/assets/brand/ from its SVG sources. The PNGs are what the app
# loads; the SVGs are the sources and set their text in Noto Sans (OFL), which must be installed here.
set -eu
cd "$(dirname "$0")/../src/assets/brand"
for theme in light dark oled; do
  rsvg-convert -w 720 -h 192 "curset-logo-$theme.svg" -o "curset-logo-$theme.png"
done
for theme in light dark; do
  rsvg-convert -w 256 -h 256 "curset-icon-$theme.svg" -o "curset-icon-$theme.png"
done
