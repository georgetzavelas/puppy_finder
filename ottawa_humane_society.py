from bs4 import BeautifulSoup
import scraper
import messages
import utils
import pdb

url = "https://ottawahumane.ca/adopt/dogs-for-adoption/"
filename = 'data_ottawa_humane_society.txt'


def get_current_dogs():
    driver = scraper.get(url)

    dogs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for dog in soup.find_all("div", "info-card-grid__item"):
        dog_info = dog.find_all("div")
        dog_details = dog_info[1].find_all("li")
        dogs.append({
            "id": dog_details[4].get_text(strip=True),
            "url": dog.a['href'],
            "image": dog_info[0].img['src'],
            "name": dog_info[2].get_text(strip=True),
            "breed": dog_details[0].get_text(strip=True),
            "gender": dog_details[2].get_text(strip=True),
            "age": dog_details[1].get_text(strip=True)
        })
    driver.close()
    return dogs


def alert_about_new_dogs(new_dogs):
    for dog in new_dogs:
        print(dog)
        messages.send_message("Ottawa Humane Society", dog['name'], dog['gender'], dog['age'], dog['image'])


known_dogs = utils.get_known_dogs(filename)
current_dogs = get_current_dogs()
new_dogs = utils.find_new_dogs(known_dogs, current_dogs)
alert_about_new_dogs(new_dogs)
utils.save_new_dogs(filename, known_dogs, new_dogs)
