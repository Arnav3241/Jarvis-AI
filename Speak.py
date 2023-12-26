from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import warnings
import pyttsx3

url = "https://www.naturalreaders.com/online/"
warnings.simplefilter("ignore")

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0])
Assistant.setProperty('rate', 80)
Assistant.setProperty('volume', 0)

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument(f'--headless=new')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
service = Service(ChromeDriverManager().install())
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

driver.find_element(by=By.XPATH, value="/html/body/app-root/app-voice-selection/div/div[1]/div[2]/div/button[3]").click()
driver.find_element(by=By.XPATH, value="/html/body/app-root/app-voice-selection/div/div[1]/div[3]/button").click()
driver.find_element(by=By.XPATH, value="/html/body/app-root/app-voice-selection/div/div[2]/div[2]/div[1]/a").click()

sleep(3)

TextBoxPath = "/html/body/app-root/app-main/app-pw-page/div/div[2]/app-pw-single-page/div[1]/div[2]/app-pw-text-reading/div/div/div[2]/div"
TextBox = driver.find_element(by=By.XPATH, value=TextBoxPath)
TextBox.clear()


def Speak(text):
  try:
    TextBox.clear()
  except:
    pass
  TextBox.send_keys(text)
  driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pw-page/div/div[2]/app-pw-single-page/div[1]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]").click()
  sleep(1.5)
  
  Assistant.say(text)
  print(f"Jarvis : {text}")
  Assistant.runAndWait()

if __name__ == "__main__":
  Speak("hey there, how are you?")
  Speak("I am fine, how are you?")
  Speak("The world is a complete mess with hate and violence everywhere and that's what i love")
  
