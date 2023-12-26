from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import warnings

url = "https://speechnotes.co/dictate/"
warnings.simplefilter("ignore")

try:
  user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
  chrome_options = Options()
  chrome_options.add_argument(f'user-agent={user_agent}')
  chrome_options.add_argument(f'--headless=new')
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
  driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')

  try:
    driver.find_element(by=By.XPATH,value="/html/body/div[4]/div/div[1]/div[1]/div[2]/div").click()
  except:
    pass

  print("Microphone is turned on")
except Exception as e:
  print(e)

def Listen():
  text_element_xpath = '/html/body/div[4]/div/div[1]/div[2]/textarea'
  text_element = driver.find_element(by=By.XPATH, value=text_element_xpath)
  text = text_element.get_attribute('value')
  
  if len(text) == 0:
    pass
  else:
    # driver.find_element(by=By.XPATH, value="a").click()
    text = text.strip()

    print(f"User   : {text}")
    text_element.clear()
    return text

if __name__ == "__main__":
  while True:
    Listen()