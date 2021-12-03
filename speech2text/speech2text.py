import speech_recognition as sr


def speech_to_text():
    audio_file=("sample_voice.wav")
    r=sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio=r.record(source)
    try:
        print("audio file contains: \n "+r.recognize_google(audio))
    except sr.UnknownValueError :
        print("google speech recogniser could not understand audio")
    except sr.RequestError:
        print("couldn't get the result")

speech_to_text()