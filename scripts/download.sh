#!/bin/bash
set -e

PLAYLIST="https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X"
OUTPUT_DIR="../audio"

mkdir -p "$OUTPUT_DIR"

yt-dlp \
  --extract-audio \
  --audio-format mp3 \
  --audio-quality 0 \
  --output "$OUTPUT_DIR/%(playlist_index)02d - %(title)s.%(ext)s" \
  --download-archive "$OUTPUT_DIR/.downloaded" \
  --no-overwrites \
  --progress \
  "$PLAYLIST"
