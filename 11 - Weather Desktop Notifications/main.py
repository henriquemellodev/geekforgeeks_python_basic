import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
  r = requests.get(url)
  return r.text

htmldata = getdata("https://weather.co/en_IN/weather/1/25.59,85.14?par=google&temp=c/")
soup = BeautifulSoup(htmldata, 'html.parser')
current_temp = soup.find_all("span", class_="_-_-components-src-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions--precipValue--2aJSf")
temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "current_temp" + temp[128:-9] + " in patna bihar" + "\n" + temp_rain[131:-4]
n.show_toast("live Weather update", result, duration = 10)