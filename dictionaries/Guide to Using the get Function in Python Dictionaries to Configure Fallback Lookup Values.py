teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}
                                    #fallback in case my lookup doesn't exsist
featured_team = teams.get("mets", 'No featured team' )

print(featured_team)