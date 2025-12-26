#!/usr/bin/env python3
"""Transcribe audio files using faster-whisper."""

from pathlib import Path
from faster_whisper import WhisperModel


def format_timestamp(seconds: float) -> str:
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{ms:03d}"


def transcribe_lectures(
    audio_dir: Path,
    output_dir: Path,
    model_size: str = "medium",
) -> None:
    """Transcribe all MP3 files in audio_dir and save to output_dir."""
    print(f"Loading Whisper model: {model_size}")
    model = WhisperModel(model_size, device="auto", compute_type="auto")

    audio_files = sorted(audio_dir.glob("*.mp3"))
    print(f"Found {len(audio_files)} audio files to transcribe\n")

    for i, audio_file in enumerate(audio_files, 1):
        print(f"[{i}/{len(audio_files)}] Transcribing: {audio_file.name}")

        segments, info = model.transcribe(
            str(audio_file),
            language="en",
            beam_size=5,
            vad_filter=True,
        )

        segments = list(segments)
        print(f"  Detected language: {info.language} (prob: {info.language_probability:.2f})")

        # Plain text output
        txt_path = output_dir / f"{audio_file.stem}.txt"
        with open(txt_path, "w") as f:
            for seg in segments:
                f.write(f"{seg.text.strip()}\n")

        # SRT output with timestamps
        srt_path = output_dir / f"{audio_file.stem}.srt"
        with open(srt_path, "w") as f:
            for j, seg in enumerate(segments, 1):
                start = format_timestamp(seg.start)
                end = format_timestamp(seg.end)
                f.write(f"{j}\n{start} --> {end}\n{seg.text.strip()}\n\n")

        print(f"  Saved: {txt_path.name}")
        print(f"  Saved: {srt_path.name}\n")

    print("Transcription complete!")


if __name__ == "__main__":
    transcribe_lectures(
        audio_dir=Path("../audio"),
        output_dir=Path("../transcripts"),
        model_size="medium",
    )
