import os
import pygame

def speak(data):
  voice = 'en-CA-LiamNeural'
  
  command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "Assets//Audio//currently.mp3"'
  os.system(command)

  pygame.init()
  pygame.mixer.init()
  pygame.mixer.music.load("Assets//Audio//currently.mp3")

  try:
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)

  except Exception as e:
    print(e)
  finally:
    pygame.mixer.music.stop()
    pygame.mixer.quit()

if __name__ == "__main__":
  speak("Hello, I am Jarvis: Your personal AI Assistant.")