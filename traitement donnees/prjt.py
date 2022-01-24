import requests
import json
import donnees as d
import time 


def horaire_ligne(url, heure):
    reponse = requests.get(url)
    data = json.loads(reponse.text)
    liste=[]
    

    for i in range(len(data['records'])):
        a = data['records'][i]['fields']['arrivee']
        liste.append(a)
    
        liste[i]=liste[i][11:16]
        if (liste[i] < heure):
            liste[i]="99:99"

    liste.sort()
    horaire = liste[0]
    return horaire

while True :
    debut = time.perf_counter()
    date = time.strftime("%d/%m/%Y")
    heure = time.strftime("%H:%M")

    reponse_meteo = requests.get(d.url_meteo)
    data_meteo = json.loads(reponse_meteo.text)

    temperature = str(data_meteo['main']['temp'] - 273.15)
    temperature = temperature[0:3]
    print(temperature)

    icone = data_meteo['weather'][0]['icon']
    print(icone)

    meteo = data_meteo['weather'][0]['main']
    print(meteo)
    
    for i in range(6):
        try:
            d. horaires[i] = horaire_ligne(d.urls[i],heure)
        except IndexError:
            horaire = '---'
        print(d.horaires[i])
    
    text = {'temp' : temperature, 'icone' : icone, 'meteo' : meteo, 'heure' : heure, 'date' : date, 'bus' : [d.horaires[0],d.horaires[1],d.horaires[2],d.horaires[3],d.horaires[4],d.horaires[5]]}

    text_json = json.dumps(text)
    print(text_json)

    table_file = open('index.html', 'w')
    table_file.write(text_json)
    table_file.close()
    fin  = time.perf_counter()
    fin = fin - debut
    print(fin)
    fin = 120 - fin
    time.sleep(fin)