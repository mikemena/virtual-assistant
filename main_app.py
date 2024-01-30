import voice_to_text as vt
import text_to_voice as tv
import webbrowser
import pyjokes


def my_assistant():
    tv.speak("Hello, I'm Sophie. how can I assist you today?")

    go_on = True
    while go_on:
        # Record audio
        recorded_audio = vt.record_audio(duration=5)
        print("recorded_audio type -> ", type(recorded_audio))

        # Convert the NumPy array to raw audio bytes
        audio_bytes = recorded_audio.tobytes()
        print("audio_bytes type -> ", type(audio_bytes))

        # Recognize the recorded audio
        my_request = vt.transform_audio_into_text(audio_bytes)
        print(my_request)
        if my_request:
            if "what is today" in my_request:
                day = tv.ask_day()
                tv.speak(f"Today is {day}")
                continue
            if "what's the time" in my_request:
                time = tv.ask_time()
                tv.speak(f"The current time is {time}")
                continue
            if "open YouTube" in my_request:
                tv.speak("Sure, I am opening YouTube.")
                webbrowser.open("https://www.youtube.com")
                continue
            elif "open browser" in my_request:
                tv.speak("Of course, I am on it.")
                webbrowser.open("https://www.google.com")
                continue
            elif "joke" in my_request:
                tv.speak(pyjokes.get_joke())
                continue
            elif "goodbye" in my_request:
                tv.speak("I am going to rest. Let me know if you need anything.")
                go_on = False
            else:
                tv.speak("I'm sorry, I didn't understand that. Can you please repeat?")
        else:
            tv.speak("I'm sorry, I did'nt catch that. Could you please repeat?")


my_assistant()
