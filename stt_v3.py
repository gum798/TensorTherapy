import speech_recognition as sr
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print(recognizer.recognize_google(audio, language='ko-KR'))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)

# import pyaudio
# import speech_recognition as sr
#
# r = sr.Recognizer()
# r.energy_threshold=4000
#
# with sr.Microphone() as source:
#     audio = r.listen(source)
#
# try:
#     print("Speech was:" + r.recognize_google(audio))
# except LookupError:
#     print('Speech not understood')