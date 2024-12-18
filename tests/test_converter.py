# tests/test_converter.py

import os
import pytest
from audio_converter.converter import convert_audio
from pydub import AudioSegment

# Sample file paths for testing
TEST_INPUT_FILE = "data/Soundstatues_Amnesia.mp3"
TEST_OUTPUT_FILE = "data/Soundstatues_Amnesia2.wav"

@pytest.fixture
def create_test_audio():
    """
    Fixture to create a sample audio file for testing.
    """
    audio = AudioSegment.silent(duration=1000)  # 1 second of silence
    os.makedirs("tests", exist_ok=True)
    audio.export(TEST_INPUT_FILE, format="wav")
    yield
    os.remove(TEST_INPUT_FILE)
    if os.path.exists(TEST_OUTPUT_FILE):
        os.remove(TEST_OUTPUT_FILE)

def test_convert_audio_format(create_test_audio):
    """
    Test conversion of audio format.
    """
    convert_audio(TEST_INPUT_FILE, TEST_OUTPUT_FILE, "mp3")
    assert os.path.exists(TEST_OUTPUT_FILE), "Output file was not created."

def test_convert_audio_channels(create_test_audio):
    """
    Test conversion of audio channels.
    """
    # Convert to mono
    convert_audio(TEST_INPUT_FILE, TEST_OUTPUT_FILE, "mp3", channels=1)
    output_audio = AudioSegment.from_file(TEST_OUTPUT_FILE)
    assert output_audio.channels == 1, "Failed to convert audio to mono."

    # Convert to stereo
    convert_audio(TEST_INPUT_FILE, TEST_OUTPUT_FILE, "mp3", channels=2)
    output_audio = AudioSegment.from_file(TEST_OUTPUT_FILE)
    assert output_audio.channels == 2, "Failed to convert audio to stereo."

def test_invalid_channel_value(create_test_audio):
    """
    Test handling of invalid channel values.
    """
    with pytest.raises(ValueError):
        convert_audio(TEST_INPUT_FILE, TEST_OUTPUT_FILE, "mp3", channels=3)
