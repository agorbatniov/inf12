import pandas as pd

# Sukuriamas duomenų rinkinys
data = {
    'Vardas': ['Jonas', 'Asta', 'Lukas', 'Rūta'],
    'Amžius': [25, 22, 24, 23],
    'Pajamos': [500, 600, 700, 550]
}

df = pd.DataFrame(data)

# Rūšiavimas pagal pajamas
sorted_df = df.sort_values(by='Pajamos', ascending=False)
print("Rūšiuoti pagal pajamas:")
print(sorted_df)

# Filtravimas pagal amžių (>23)
filtered_df = df[df['Amžius'] > 23]
print("Filtruoti pagal amžių > 23:")
print(filtered_df)

# Grupavimas (pvz., amžiaus grupės)
df['Amžiaus_grupė'] = pd.cut(df['Amžius'], bins=[20, 23, 26], labels=['20-23', '23-26'])
grouped = df.groupby('Amžiaus_grupė').mean()
print("Grupuoti pagal amžiaus grupes:")
print(grouped)