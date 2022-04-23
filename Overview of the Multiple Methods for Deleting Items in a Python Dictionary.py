teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

#del teams['mets']
removed_team = teams.pop('mets', 'Team not found') #best practice

print(teams)
print(removed_team)