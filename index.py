import requests

from bs4 import BeautifulSoup

# for opening browsers
import webbrowser


while True:
    # wiki pedia
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    soup = BeautifulSoup(url.content, "html.parser")

    # find title
    title = soup.find(class_="firstHeading").text

    answer = input(f"{title} \n Do You Want To View It: (Y/N)").lower()

    # condition
    if answer == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif answer == "n":
        print("Try Again...")
        continue
    else:
        print("not found :/")
        break
