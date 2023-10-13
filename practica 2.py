import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('archivo.csv')

# Lista de nombres de las columnas a eliminar
columnas_a_eliminar = ['id', 'timezone', 'venue_id']

# Elimina las columnas
df = df.drop(columnas_a_eliminar, axis=1)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('archivo_modificado.csv', index=False)
 
 #--------------------------------------------------------


# Lee el archivo CSV
df = pd.read_csv('archivo_modificado.csv')

# Diccionario de mapeo para cambiar los nombres de las columnas
nombres_nuevos = {
    'referee': 'Arbitro',
    'date': 'fecha',
    'venue_name': 'Estadio',
    'venue_city': 'Ciudad',
    'season': 'Temporada',
    'round': 'Ronda',
    'home_team': 'Equipo de casa',
    'away_team': 'Equipo visita',

}

# Cambia los nombres de las columnas
df = df.rename(columns=nombres_nuevos)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('archivo_modificado.csv', index=False)