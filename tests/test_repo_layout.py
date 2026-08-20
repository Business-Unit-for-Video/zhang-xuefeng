from pathlib import Path

def test_zhang_corpus_and_state_are_present():
    assert Path("scripts/transcribe_bili.py").is_file()
    assert Path("scripts/transcription_integrity.py").is_file()
    assert Path("state/progress.json").is_file()
    assert any(Path("transcripts").glob("*.txt"))
