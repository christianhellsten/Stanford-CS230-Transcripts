PLAYLIST = https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X

download:
	yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 \
		--output "../audio/%(playlist_index)02d - %(title)s.%(ext)s" \
		$(PLAYLIST)

transcribe:
	uv run --with faster-whisper python transcribe.py
