from gtts import gTTS
import os
import platform


def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")

    # Determine the platform and execute the appropriate command to open the file
    if platform.system() == "Windows":
        os.system("start output.mp3")
    elif platform.system() == "Darwin":  # macOS
        os.system("open output.mp3")
    else:  # Assuming Linux or other Unix-like
        os.system("xdg-open output.mp3")


# Example usage
text = "rata de dos patas, te estoy hablando a ti."
text_to_speech(text)
