import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import playsound
from time import sleep
import warnings

url = "https://dictation.io/speech"
warnings.simplefilter("ignore")

start = time.time()

try:
  user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
  chrome_options = Options()
  chrome_options.add_argument(f'user-agent={user_agent}')
  # chrome_options.add_argument(f'--headless=new')
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  chrome_options.add_argument('--log-level=3')
  service = Service(ChromeDriverManager().install())
  chrome_options.add_argument("--use-fake-ui-for-media-stream")
  chrome_options.add_argument("--use-fake-device-for-media-stream")
except Exception as e:
  print(e)

try:
  driver = webdriver.Chrome(service=service, options=chrome_options)
  driver.get(url)
  driver.refresh()

  try:
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div").click()
  except:
    pass


  driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
  # sleep(1)

  clear_button_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]'
  driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
  # sleep(1)

  start_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
  driver.find_element(by=By.XPATH, value=start_button_xpath).click()
  print("Microphone is turned on")
except Exception as e:
  print(e)

end = time.time()
print(end - start)

def Listen():
  text_element_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
  text = driver.find_element(by=By.XPATH, value=text_element_xpath).text

  if len(text) == 0:
    return ""
  else:
    driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
    text = text.strip()

    print(f"User   : {text}")
    return text

if __name__ == "__main__":
  while True:
    Listen()
