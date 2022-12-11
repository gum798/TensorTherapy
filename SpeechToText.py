
class SpeechToText:
    import speech_recognition as sr
    
    def __init__(self):
        self.r = self.sr.Recognizer()
    
    def speech2txt(self,seconds=20):
        with self.sr.Microphone() as source:
            print("Say something! : ")
            audio = self.r.record(source, duration=seconds)
            try:
                text = self.r.recognize_google(audio_data=audio, language='ko-KR')
                print("You said : {}".format(text))
            except:
                text=""
                print("Sorry could not recognize what you said")
        return text
