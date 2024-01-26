import speech_recognition as sr
import pyaudio


def transform_audio_into_text():
    r = sr.Recognizer()

    # set microphone as the audio source
    with sr.Microphone() as source:
        r.pause_threshold = 0.8

        # inform the user that recording has started
        print("Recoridng Started")

        # save the recording audio
        audio = r.listen(source)

        try:
            # search on google
            request = r.recognize_google(audio, language="en-us")
            print("You said " + request)
            return request
        except sr.UnknownValueError():
            print("Google Speech Recognition could not understand the audio")
            return "I am still waiting"
        except sr.RequestError as e:
            # Error when there's a problem with the Google Speech Recognition service
            print(
                f"Could not request results from Google Speech Recognition service; {e}"
            )
            return "I am still waiting"

            # return error
            return "I am still waiting"


transform_audio_into_text()
