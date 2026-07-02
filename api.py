import requests
import json

def main():
    res=requests.get("https://openlibrary.org/search.json",{"q":"monet"})
    con=res.json()
    for artwor in con["docs"]:
        print(artwor['title'])



main()
