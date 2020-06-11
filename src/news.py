import tkinter as tk
import requests
import bs4
from random import choice

# main tkinter window
root = tk.Tk()

# requests object
url = "http://www.yahoo.com/news"
r = requests.get(url)

# soup object
soup = bs4.BeautifulSoup(r.text,'lxml')
pTags = [i.getText() for i in soup.find_all("p")]

# random element from pTags
def returnRandomElement():
    # randElement = [i.strip() for i in choices(pTags)]
    randElement = choice(pTags)
    return randElement

def main():
    tk.Label(root,text="Yahoo News",font=("Helvetica", 36)).grid(row=0)
    for i in range(2):
        tk.Label(root,text=returnRandomElement(),wraplength=500,font=("Helvetica", 20)).grid(row=i+1)


main()
root.mainloop()
