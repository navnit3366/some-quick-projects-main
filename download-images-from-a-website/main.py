import requests
from bs4 import BeautifulSoup
import os

url = "http://www.centrale-casablanca.ma/fr/entreprise/partenariats/aident-centrale-casablanca-a-se-developper"

FOLDER = r"C:\Users\user\Desktop\inut\img"


def get_img():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('img')

    for i, headline in enumerate(headlines):
        #if i==9: break
        print(100 * i / len(headlines), "%", end=" ")
        link = headline['src']
        filename = link.split("/")[-1]
        print(link)
        r = requests.get(link)
        image_name = os.path.join(FOLDER, filename)  # f"image{i}.jpg"
        with open(image_name, 'wb') as f:
            f.write(r.content)


def main():
    get_img()


if __name__ == '__main__':
    main()
