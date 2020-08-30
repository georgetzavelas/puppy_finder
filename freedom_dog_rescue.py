from bs4 import BeautifulSoup
import scraper
import messages
import utils

url = "http://www.freedomdogrescue.ca/available-for-adoption.html"
filename = 'data_freedom_dog_rescue.txt'


def get_current_dogs():
    driver = scraper.get(url)

    dogs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dogs_info = soup.find_all("div", "wsb-media-carousel")
    for dog in dogs_info[0].find_all("a"):
        dogs.append({
            "id": dog['rel'][0],
            "image": "http:" + dog['href'],
            "info": dog['title']
        })
    driver.close()
    return dogs


def alert_about_new_dogs(new_dogs):
    for dog in new_dogs:
        print(dog)
        messages.send_message("Freedom Dog Rescue", dog['info'], dog['image'], '', '')


known_dogs = utils.get_known_dogs(filename)
current_dogs = get_current_dogs()
new_dogs = utils.find_new_dogs(known_dogs, current_dogs)
alert_about_new_dogs(new_dogs)
utils.save_new_dogs(filename, known_dogs, new_dogs)
