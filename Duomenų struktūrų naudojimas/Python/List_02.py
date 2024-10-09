# Sąrašo sukūrimas
vaisiai = ["Obuolys", "Bananai", "Vyšnios"]

# Elementų pasiekimas
print(vaisiai[0])  # Išvestis: Obuolys

# Elementų pridėjimas
vaisiai.append("Apelsinas")
vaisiai.append("Mango")
vaisiai.append("Kivis")

# Elementų šalinimas
vaisiai.remove("Bananai")

print(vaisiai) 

# Sąrašo dalijimas
print(vaisiai[1:3])  # Išvestis: ['Vyšnios', 'Apelsinas']
print(vaisiai[2:4])  # Išvestis: ['Apelsinas', 'Mango']