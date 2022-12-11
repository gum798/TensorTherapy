import speech_recognition as sr
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something! : ")
        audio = r.record(source, duration=20)
        try:
            text = r.recognize_google(audio_data=audio, language='ko-KR')
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")    
    # key interrupt signal
    try:
        pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
