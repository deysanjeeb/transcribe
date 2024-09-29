# 🎙️ Audio Transcriber

## 📜 Overview

Audio Transcriber is a Python-based tool that converts audio files into text using OpenAI's Whisper model. It's perfect for quickly transcribing interviews, lectures, or any other audio content! 🚀

## ✨ Features

- 🔊 Transcribe audio files to text
- 🧠 Uses OpenAI's Whisper "medium" model for accurate transcription
- 💾 Save transcriptions to text files
- 🖥️ Easy-to-use command-line interface

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- OpenAI Whisper library
- FFmpeg (required by Whisper for audio processing)

## 🔧 Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/audio-transcriber.git
   cd audio-transcriber
   ```

2. Install the required packages:
   ```
   pip install openai-whisper
   ```

3. Install FFmpeg:
   - On macOS: `brew install ffmpeg`
   - On Windows: Download from [FFmpeg official website](https://ffmpeg.org/download.html)
   - On Linux: `sudo apt-get install ffmpeg`

## 🚀 Usage

Run the script from the command line with the following format:

```
python transcribe.py <audio_path> <output_path>
```

For example:

```
python transcribe.py my_audio.mp3 transcript.txt
```

This will transcribe `my_audio.mp3` and save the transcript to `transcript.txt`.

## 📄 Output

The script will generate a text file at the specified output path containing the transcribed text from your audio file.

## ⚠️ Note

- Transcription accuracy may vary depending on audio quality and speech clarity.
- Larger audio files may take longer to process.

## 🤝 Contributing

Contributions to the Audio Transcriber are welcome! Feel free to submit a Pull Request. 🎉

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for providing the transcription model

Happy transcribing! 🎉🔊📝
