# converter.py

from pydub import AudioSegment

def convert_audio(input_file: str, output_file: str, output_format: str, channels: int = None):
    """
    Convert an audio file to a specified format and optionally adjust channels.

    Parameters:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the converted audio file.
        output_format (str): Format of the output file (e.g., 'mp3', 'wav').
        channels (int, optional): Number of audio channels (1 for mono, 2 for stereo).
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the output format or channel value is invalid.
    """
    try:
        # Load the input audio file
        audio = AudioSegment.from_file(input_file)
        
        # Adjust the number of channels if specified
        if channels:
            if channels == 1:
                audio = audio.set_channels(1)  # Convert to mono
            elif channels == 2:
                audio = audio.set_channels(2)  # Convert to stereo
            else:
                raise ValueError("Invalid channel value. Use 1 for mono or 2 for stereo.")
        
        # Export the audio file in the desired format
        audio.export(output_file, format=output_format)
        print(f"Successfully converted {input_file} to {output_format} format at {output_file}")
        if channels:
            print(f"Adjusted to {channels}-channel audio.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
