import whisper
import sys

def transcribe_audio(audio_path):
    # Load the model
    model = whisper.load_model("medium")

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Return the transcription text
    return result['text']

def save_transcript(transcript, output_path):
    # Save the transcript to a file
    with open(output_path, 'w') as file:
        file.write(transcript)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python transcribe.py <audio_path> <output_path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_path = sys.argv[2]

    # Transcribe the audio
    transcript = transcribe_audio(audio_path)

    # Save the transcript
    save_transcript(transcript, output_path)

    print(f"Transcription completed and saved to {output_path}")