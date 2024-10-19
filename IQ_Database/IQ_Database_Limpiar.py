import pandas as pd
import numpy as np
import os

# Obtiene la ruta del directorio actual
current_dir = os.path.dirname(__file__)

# Lee el archivo CSV desde la carpeta del proyecto
csv_path = os.path.join(current_dir, 'IQ_level.csv')
df = pd.read_csv(csv_path)

# Reemplaza las celdas vacías con NaN
df.replace("", np.nan, inplace=True)

# Rellenar valores nulos con la media de las columnas numéricas, redondeada a un decimal
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean().round(1))

# Elimina las filas duplicadas
df = df.drop_duplicates()

# Guarda el DataFrame limpio en un nuevo archivo CSV
# La ruta del archivo CSV a exportar
output_path = os.path.join(current_dir, 'IQ_level_limpio.csv')
df.to_csv(output_path, index=False)