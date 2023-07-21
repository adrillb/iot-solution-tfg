import speech_recognition as sr

def recognize_speech():
     recognizer = sr.Recognizer()

     with sr.Microphone() as source:
          print("Listening")
          recognizer.adjust_for_ambient_noise(source)
          audio = recognizer.listen(source)

     try:
          text = recognizer.recognize_google(audio, language='es-ES')

          print("You said:", text)
          return text
     except sr.UnknownValueError:
          print("Didn't get that")
     except sr.RequestError as e:
          print("Error caling Google Search Speech Recognition; {0}".format(e))

