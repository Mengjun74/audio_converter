from flask import Flask, request, jsonify, send_file
from audio_converter.converter import convert_audio
import os

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Audio Converter</h1>
    <form action="/convert" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".wav,.mp3,.flac,.ogg,.aac,.m4a,.wma,.opus,.aiff" required><br><br>
        
        <label for="format">Choose output format:</label>
        <select name="format" id="format">
            <option value="mp3">MP3</option>
            <option value="wav">WAV</option>
            <option value="flac">FLAC</option>
            <option value="ogg">OGG</option>
            <option value="aac">AAC</option>
            <option value="m4a">M4A</option>
            <option value="wma">WMA</option>
            <option value="opus">Opus</option>
            <option value="aiff">AIFF</option>
        </select><br><br>
        
        <label for="channels">Choose number of channels:</label>
        <select name="channels" id="channels">
            <option value="1">Mono</option>
            <option value="2">Stereo</option>
        </select><br><br>
        
        <input type="submit" value="Convert">
    </form>
    """

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    format = request.form['format']
    channels = int(request.form['channels'])  # Get the selected channels (1 for Mono, 2 for Stereo)
    
    input_path = os.path.join('uploads', file.filename)
    output_path = os.path.splitext(input_path)[0] + f".{format}"

    # Save the uploaded file
    file.save(input_path)

    # Convert the audio
    try:
        convert_audio(input_path, output_path, output_format=format, channels=channels)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
