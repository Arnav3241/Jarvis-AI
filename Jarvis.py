ConvL = [
  "",
  ""
]

from Functions.Listen import Listen
from Functions.Speak import Speak

ConvT = 100

def Execution():
  while True:
    query = Listen()
    Speak(query)

if __name__ == "__main__":
  Execution()

