from gtts import gTTS
import os
import platform
import datetime


def speak(text, lang="en"):
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

    calendar = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    day = calendar[week_day]
    speak(f"Today is {calendar[week_day]}")


def ask_time():
    time = datetime.datetime.now().strftime("%I:%M %p")  # Formats time as "HH:MM AM/PM"
    speak(f"The current time is {time}")


def initial_greeting():
    speak("Hello, I am Sophie. How can i help you?")
