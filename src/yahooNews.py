import bs4
import requests
from random import choice
import tkinter as tk

# main tkinter window
root = tk.Tk()
root.title("Yahoo News App")

# requests object
url = "https://www.yahoo.com/news"
r = requests.get(url)

# soup object
soup = bs4.BeautifulSoup(r.text,'lxml')
pTags = [i.getText() for i in soup.find_all("p")]

# return random <p> tag
def returnRandomElement():
    randElement = choice(pTags)
    return randElement

def main():
    tk.Label(root,text="Yahoo News",font=("Helvetica", 45),background="gold").grid(row=0,ipadx=110)
    for i in range(2):
        tk.Label(root,text=returnRandomElement(),wraplength=500,font=("Helvetica", 20), background="whitesmoke").grid(row=i+1)
    tk.Button(root, text="Exit",command=root.destroy,font=("Helvetica", 22)).grid(row=1,column=2)


main()
root.mainloop()
