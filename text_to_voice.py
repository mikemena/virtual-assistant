from gtts import gTTS
import os
import platform
import datetime


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


def ask_day():
    day = datetime.date.today()
    print(day)
    week_day = day.weekday()
    print(week_day)
    return week_day


week_day = ask_day()

# Example usage
text = "rata de dos patas, te estoy hablando a ti."
text_to_speech(f"today is {week_day}")
text_to_speech(text)
