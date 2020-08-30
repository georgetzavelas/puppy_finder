from bs4 import BeautifulSoup
import scraper
import messages
import utils

url = "https://adoptapet.com/pet-search?clan_id=1&geo_range=50&location=Kanata,%20ON"
filename = 'data_adopt_a_pet.txt'


def get_current_dogs():
    driver = scraper.get_and_wait(url, "searchResultsContainer")

    dogs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for dog in soup.find_all("div", "search__result"):
        dog_info = dog.div.a.div.div.find_all("div")
        dog_details = dog_info[1].find_all("span")
        if not dog_details:
            dogs.append({
                "id": dog.div['id'],
                "url": dog.div.a['href'],
                "image": dog.div.a.div.img['src'],
                "name": dog_info[0].get_text(strip=True),
                "gender": "unknown",
                "age": "unknown"
            })
        else:
            dogs.append({
                "id": dog.div['id'],
                "url": dog.div.a['href'],
                "image": dog.div.a.div.img['src'],
                "name": dog_info[0].get_text(strip=True),
                "gender": dog_details[0].get_text(strip=True),
                "age": dog_details[2].get_text(strip=True)
            })
    driver.close()
    return dogs


def alert_about_new_dogs(new_dogs):
    for dog in new_dogs:
        print(dog)
        messages.send_message("Adopt A Pet", dog['name'], dog['gender'], dog['age'], dog['image'])


known_dogs = utils.get_known_dogs(filename)
current_dogs = get_current_dogs()
new_dogs = utils.find_new_dogs(known_dogs, current_dogs)
alert_about_new_dogs(new_dogs)
utils.save_new_dogs(filename, known_dogs, new_dogs)
