players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
#player_names = list(players.copy().values())
#print(player_names)

#print(players.keys())
#dict_keys(['ss', '2b', '3b', 'DH', 'OF'])

#print(players.values())
#dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])

#print(players.items())
#dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()
print(list(team_groupings)[1][1][0]) #[1] = ('angels', ['Trout', 'Pujols']), [1] = ['Trout', 'Pujols'], [0] = Trout

"""
[
    [('astros', ['Altuve', 'Correa', 'Bregman']), 
    ('angels', ['Trout', 'Pujols']), 
    ('yankees', ['Judge', 'Stanton']), 
    ('red sox', ['Price', 'Betts'])]
]
"""