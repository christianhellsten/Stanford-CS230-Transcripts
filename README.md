# Stanford CS230: Deep Learning - Lecture Transcripts

Transcripts of the Stanford CS230 Deep Learning course (Autumn 2025).

## Source

**Playlist:** [Stanford CS230: Deep Learning I Autumn 2025](https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X)

## Lectures

| # | Title | Video |
|---|-------|-------|
| 1 | Introduction to Deep Learning | [Watch](https://www.youtube.com/watch?v=_NLHFoVNlbg) |
| 2 | Supervised, Self-Supervised, & Weakly Supervised Learning | [Watch](https://www.youtube.com/watch?v=DNCn1BpCAUY) |
| 3 | Full Cycle of a DL project | [Watch](https://www.youtube.com/watch?v=MGqQuQEUXhk) |
| 4 | Adversarial Robustness and Generative Models | [Watch](https://www.youtube.com/watch?v=aWlRtOlacYM) |
| 5 | Deep Reinforcement Learning | [Watch](https://www.youtube.com/watch?v=4E27qlfYw0A) |
| 6 | AI Project Strategy | [Watch](https://www.youtube.com/watch?v=s6JVGzABKho) |
| 8 | Agents, Prompts, and RAG | [Watch](https://www.youtube.com/watch?v=k1njvbBmfsw) |
| 9 | Career Advice in AI | [Watch](https://www.youtube.com/watch?v=AuZoDsNmG_s) |
| 10 | What's Going On Inside My Model? | [Watch](https://www.youtube.com/watch?v=Ozb1AR_F5MU) |

Note: Lecture 7 is missing from Stanford's original YouTube playlist.

## File Formats

- `.txt` - Plain text transcripts for reading, searching, and text analysis
- `.srt` - Subtitle files with timestamps for video players and time-synced navigation

## How These Transcripts Were Created

### 1. Audio Download

Extracted audio from YouTube with [yt-dlp](https://github.com/yt-dlp/yt-dlp):

```bash
yt-dlp \
  --extract-audio \
  --audio-format mp3 \
  --audio-quality 0 \
  --output "audio/%(playlist_index)02d - %(title)s.%(ext)s" \
  "https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X"
```

### 2. Transcription

Generated with [faster-whisper](https://github.com/SYSTRAN/faster-whisper) using the `medium` model:

```python
from faster_whisper import WhisperModel

model = WhisperModel("medium", device="auto", compute_type="auto")
segments, info = model.transcribe(
    audio_file,
    language="en",
    beam_size=5,
    vad_filter=True,
)
```

## License

For educational purposes only. Original content owned by Stanford University.
