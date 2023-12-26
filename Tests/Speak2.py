import pyttsx3

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0])
Assistant.setProperty('rate', 180)

def SpeakPyttsx3(audio):
  if audio == "":
    return
  Assistant.say(audio)
  print(f"Jarvis : {audio}")
  Assistant.runAndWait()

if __name__ == "__main__":
  SpeakPyttsx3("Hello, I am Jarvis.")
