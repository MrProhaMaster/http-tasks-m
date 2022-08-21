import requests


def task1():
    heroes = {"hulk": '', "Captain America": '', "Thanos": ''}
    beggining = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/"
    id_request = "https://www.superheroapi.com/api.php/2619421814940190/search/"
    for i in heroes:
        mx = 0
        r = requests.get(id_request+i)
        id = r.json()["results"][0]["id"]
        url = beggining + id + '.json'
        r = requests.get(url)
        heroes[i] = int(r.json()["intelligence"])
        if heroes[i]>mx:
            mx = heroes[i]
            mx_hero = i
    print(f'Самый умный: {mx_hero} - {mx}')

task1()