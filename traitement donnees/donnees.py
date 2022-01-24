url_meteo="http://api.openweathermap.org/data/2.5/weather?q=Rennes,FRA&appid=f9d001a2f0812362b72a547a1cbe5de7"
url_c4gc = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=1291&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.nomcourtligne=C4"
url_c4za = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=1314&facet=nomcourtligne&facet=destination&refine.idligne=0004&refine.destination=ZA+Saint-Sulpice"
url_14b = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=1314&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.nomcourtligne=14"
url_14rp = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=9217&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.idligne=0014"
url_40re = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=9217&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.idligne=0040"
url_40b = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=9218&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.idligne=0040"
url_32b = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=9218&facet=idligne&facet=sens&facet=destination&facet=precision&refine.destination=Beaulieu+IUT&refine.idligne=0032"
url_32t = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&q=9217&sort=-nomarret&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.idligne=0032"

horaire_c4gc = 0
horaire_c4za = 0
horaire_14b = 0
horaire_14rp = 0
horaire_32b = 0
horaire_32t = 0

urls = [url_c4gc, url_c4za, url_14b, url_14rp, url_32b, url_32t]
horaires = [horaire_c4gc, horaire_c4za, horaire_14b, horaire_14rp, horaire_32b, horaire_32t]
bus = ["c4_gc", "c4_za", "14b", "14rp", "32b", "32t"]

meteo_eng  = ["Clouds", "Mist", "Few clouds"]
meteo_fr = ["Nuageux", "Brumeux", "Qlq nuages"]