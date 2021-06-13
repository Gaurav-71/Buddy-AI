from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googlesearch import search

CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

class Links:
  def __init__(self, text, link):
      self.text = text
      self.link = link

news_url = "https://www.unisys.com/about-us/newsroom/news-release-archive"
about_url = "https://www.unisys.com/about-us"
zomato_url = "https://www.zomato.com/bangalore/delivery?zomato_place_v2=20239"

def news():
  driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                          )
  driver.get(news_url)
  elems = driver.find_elements_by_css_selector("#NewsReleaseArchiveBox a")
  results = []
  for index,elem in enumerate(elems):
      results.append(Links(elem.text,elem.get_attribute("href")))
      if index == 2:
        break
  results.append(Links("Read more news on our website", "https://www.unisys.com/about-us/newsroom/news-release-archive"))
  driver.close()
  return results

def about():
  # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
  #                         chrome_options=chrome_options
  #                         )
  # driver.get(about_url)
  # elems = driver.find_elements_by_xpath('//*[@id="card-overview-description"]/article/p[1]')
  # results = ""
  # for elem in elems:
  #   results = elem.text
  # driver.close()
  return "Unisys is a global IT solutions company that delivers successful outcomes for the most demanding businesses and governments. Unisys offerings include digital workplace services, cloud and infrastructure services, software operating environments for high-intensity enterprise computing, business process solutions and application development services. Unisys integrates security into all of its solutions."

def motto():
  # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
  #                         chrome_options=chrome_options
  #                         )
  # driver.get(about_url)
  # elems = driver.find_elements_by_xpath('//*[@id="card-overvie-body"]/h2')
  # results = []
  # for elem in elems:
  #   results = elem.text
  # driver.close()
  return "Enhancing people’s lives through secure, reliable advanced IT solutions"

# saving blogs directly to save time
def blogs():
  results = []
  results.append(Links("Three Surprises that Blockchain Brings to Worker Experience","https://blogs.unisys.com/podcasts/dwsdeepdive/23-three-surprises-that-blockchain-brings-to-worker-experience/"))
  results.append(Links("Read more blogs on our website", "https://blogs.unisys.com/"))
  return results

def googleSearch(query):
  sr = search(query,num_results=0)[0]
  result = []
  result.append(Links(sr,sr))
  return result

def restaurants():
  # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
  #                         chrome_options=chrome_options
  #                         )
  # driver.get(zomato_url)
  # elems = driver.find_elements_by_xpath('//*[@id="root"]/div/div[8]/div/div[1]/div/div/a[2]/div[1]/p')
  # results = ""
  # for elem in elems:
  #   results = elem.text
  # driver.close()
  results = []
  results.append(Links("Hatti Kaapi","https://www.zomato.com/bangalore/hatti-kaapi-malleshwaram-bangalore/info?contextual_menu_params=eyJkaXNoX3NlYXJjaCI6eyJ0aXRsZSI6IkJlc3QgaW4gQ2FmZSIsImRpc2hfaWRzIjpbXSwiY3Vpc2luZV9pZHMiOlsiMzAiXX19"))
  results.append(Links("Tata Cha","https://www.zomato.com/bangalore/tata-cha-malleshwaram-bangalore/info?contextual_menu_params=eyJkaXNoX3NlYXJjaCI6eyJ0aXRsZSI6IkJlc3QgaW4gQ2FmZSIsImRpc2hfaWRzIjpbXSwiY3Vpc2luZV9pZHMiOlsiMzAiXX19"))
  results.append(Links("Cafe Coffee Day","https://www.zomato.com/bangalore/cafe-coffee-day-1-rajajinagar/info?contextual_menu_params=eyJkaXNoX3NlYXJjaCI6eyJ0aXRsZSI6IkJlc3QgaW4gQ2FmZSIsImRpc2hfaWRzIjpbXSwiY3Vpc2luZV9pZHMiOlsiMzAiXX19"))
  return results

