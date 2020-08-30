from bs4 import BeautifulSoup
import scraper
import messages
import utils

url = "https://www.kijiji.ca/b-chiens-chiots/quebec/c126l9001?ad=offering"
filename = 'data_adopt_a_pet.txt'


# NOT TESTED!!!
def get_current_dogs():
    driver = scraper.get_and_wait(url, "searchResultsContainer")

    dogs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for dog in soup.find_all('div', class_="search-item regular-ad")
        dogs.append({
            "id": dog.attrs['data-listing-id'],
            "url": 'https://www.kijiji.ca' + dog.find('a')['href'],
            "cost": dog.find('div', class_='price').get_text(strip=True),
            "title": dog.find('a', class_='title').get_text(strip=True),
            "distance": dog.find('div', class_='distance').get_text(strip=True),
            "description": dog.find('div', class_='description').get_text(strip=True)
        })
    driver.close()
    return dogs


def alert_about_new_dogs(new_dogs):
    for dog in new_dogs:
        print(dog)
        messages.send_message("Kijiji", dog['name'], dog['gender'], dog['age'], dog['image'])


known_dogs = utils.get_known_dogs(filename)
current_dogs = get_current_dogs()
new_dogs = utils.find_new_dogs(known_dogs, current_dogs)
alert_about_new_dogs(new_dogs)
utils.save_new_dogs(filename, known_dogs, new_dogs)