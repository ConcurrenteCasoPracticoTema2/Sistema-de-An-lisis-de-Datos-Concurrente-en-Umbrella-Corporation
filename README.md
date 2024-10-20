# Sistema de Análisis de Datos Concurrente en Umbrella Corporation

[Repositorio](https://github.com/ConcurrenteCasoPracticoTema2/Sistema-de-An-lisis-de-Datos-Concurrente-en-Umbrella-Corporation.git)

Proyecto realizado por Jose Daniel Martín, Hugo Sanchez, Fernando Santamaría y Jose Antonio Oyono

## Descripción del Proyecto

Este proyecto tiene como objetivo limpiar y analizar un conjunto de datos sobre niveles de IQ, gasto en educación, ingreso promedio y temperatura promedio de varios países. Utiliza Python y las bibliotecas `pandas` y `numpy` para la manipulación y limpieza de datos.

## Estructura del Proyecto

- `IQ_Database/IQ_Database_Limpiar.py`: Script principal para la limpieza de datos.
- `IQ_Database/IQ_level.csv`: Archivo CSV original con los datos sin procesar.
- `IQ_Database/IQ_level_limpio.csv`: Archivo CSV generado con los datos limpios.

## Dependencias

- Python 3.x
- pandas
- numpy

## Uso

1. Asegúrate de que el archivo `IQ_level.csv` esté en el directorio `IQ_Database`.
2. Ejecuta el script de limpieza:
    ```sh
    python IQ_Database_Limpiar.py
    ```
3. El archivo limpio `IQ_level_limpio.csv` se generará en el mismo directorio.

## Explicación del Código

El script `IQ_Database_Limpiar.py` realiza las siguientes operaciones:

1. **Carga de Datos**: Lee el archivo CSV original.
    ```python
    df = pd.read_csv(csv_path)
    ```
2. **Reemplazo de Valores Vacíos**: Reemplaza las celdas vacías con `NaN`.
    ```python
    df.replace("", np.nan, inplace=True)
    ```
3. **Relleno de Valores Nulos**: Rellena los valores nulos en las columnas numéricas con la media de cada columna, redondeada a un decimal.
    ```python
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean().round(1))
    ```
4. **Eliminación de Duplicados**: Elimina las filas duplicadas.
    ```python
    df = df.drop_duplicates()
    ```
5. **Guardado de Datos Limpios**: Guarda el DataFrame limpio en un nuevo archivo CSV.
    ```python
    df.to_csv(output_path, index=False)
    ```

