
sports_team_rosters = {
    "Manchester City": ["Haaland", "Grealish", "Foden"],
    "Spurs": ["Son", "Harry Kane", "Hugo Lloris"],
    "Chelsea": ["Cucurella", "Sterling", "Kante"],
    "Liverpool": ["Ruiz Diaz", "Salah", "Arnold"]
}

sports_team_rosters["Manchester United"] = ["Cristiano", "Bruno", "Fred"]

print(sports_team_rosters["Manchester City"])
print(sports_team_rosters["Manchester United"])
# Espacio 0
print()
print(sports_team_rosters)

print() # Primer Espacio
sports_team_rosters.pop("Manchester United")
print(sports_team_rosters)


print() # Segundo Espacio 
video_game_options = {}

# or 
# video_game_options = dict()

video_game_options["Subtitles"] = True
video_game_options["Difficulty"] = "Hard"
video_game_options["Volume"] = 6

print(video_game_options)

video_game_options["Difficulty"] = "Medium"
video_game_options["Subtitles"] = False

print(video_game_options)

# Crear un contador de palabras con dictionaries 
print() # Tercer Espacio

words = ["Melissa", "Me", "Encanta", "<3"]

def word_count(word):

    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts

print(word_count(words))