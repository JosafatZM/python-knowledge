tv_shows = {
    "Club de Cuervos": {
        "Season 1": {
            "Episodes": ["Hola Hugo Sanchez", "El partido"],
            "Genre": "Comedy",
            "Year": 2017
        },
        "Season 2":{
            "Episodes": ["El Descenso"],
            "Genere": "Comedy",
            "Year": 2018
        }
    },
    "House of cards": {
        "Season 1": {
            "Episodes": ["Wellcome to the capitolio"],
            "Genre": "Drama", 
            "Year": 2014
        }
    }
}

print(tv_shows["Club de Cuervos"]["Season 1"]["Episodes"][1])
año = tv_shows["Club de Cuervos"]["Season 2"]["Year"]
print(f"El año en el que salio la segunda temporada de club de cuervos fue {año}")

