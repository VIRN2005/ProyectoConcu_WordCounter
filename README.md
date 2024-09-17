# Proyecto Concurrencia y Sistemas Distribuidos 
# Tokenizer WordCount Using Hadoop 

## Enlaces y Archivos Necesarios

- **Link Dataset Original**: Busca el archivo `linkDataset.txt` para encontrar el enlace.

  > **Nota**: Es obligatorio utilizar `datasetCompleto.txt` para el desarrollo del proyecto. Si solo tienes `datasetCompleto.csv`, conviértelo a `.txt` utilizando el script `preparingDataset.py`.

## Preparación del Entorno

1. **Preparación de Archivos**:
   - Descarga el archivo `datasetCompleto.csv` y guarda en la misma carpeta que `preparingDataset.py`.
   - Ejecuta el script `preparingDataset.py` para convertir el archivo CSV a TXT.

2. **Ubicación del Archivo**:
   - Coloca `datasetCompleto.txt` en el directorio `workingFiles`.

3. **Diccionario**:
   - Encuentra el diccionario en `workingFiles` con el nombre `Dictionary.txt`.

## Preprocesamiento

1. **Compilación**:
   - Compila el archivo Java para el preprocesamiento:
     ```bash
     javac preProcesamiento.java
     ```

2. **Ejecución**:
   - Ejecuta el archivo `.class` generado:
     ```bash
     java preProcesamiento
     ```

   - Esto generará `datasetProcesado.txt` en el directorio `workingFiles`.

   > **Nota**: Un archivo `datasetProcesado.txt` ya disponible en el drive (ver `linkDataset.txt`).

## Análisis de Frecuencia con Hadoop

### Configuración de Hadoop

1. **Instalación**:
   - Asegúrate de tener Hadoop instalado.

2. **Crear Carpeta de Input**:
   - Crea una carpeta en Hadoop para el dataset procesado:
     ```bash
     hdfs dfs -mkdir /ruta_de_la_carpeta_input/
     ```

3. **Subir Dataset**:
   - Sube `datasetProcesado.txt` a Hadoop:
     ```bash
     hdfs dfs -put /ruta_del_dataset/ /ruta_de_la_carpeta_input/
     ```

### Análisis de Frecuencia de 1 Palabra

1. **Ejecución del Jar**:
   - Navega a la carpeta `Frequency1` del repositorio.
   - Ejecuta el JAR para análisis de 1 palabra:
     ```bash
     hadoop jar wordcount.jar WordCount /ruta_de_carpeta_input_en_hadoop/ /ruta_destino_dentro_de_hadoop/
     ```

   - La carpeta de destino se creará automáticamente.

2. **Descargar Resultados**:
   - Obtén el archivo `part-r-00000` de Hadoop:
     ```bash
     hdfs dfs -get /ruta_del_part-r-00000_en_hadoop/ .
     ```

   - Guarda el archivo en la carpeta `Frequency1` del repositorio.

3. **Procesar Resultados**:
   - En `Frequency1`, ejecuta el script de Python para analizar los resultados:
     ```bash
     python freq-analysis.py
     ```

   - Esto generará `freq-results-sorted.txt`.

### Análisis de Frecuencia de 2 Palabras

1. **Ejecución del Jar**:
   - Navega a la carpeta `Frequency2` del repositorio.
   - Ejecuta el JAR para análisis de 2 palabras:
     ```bash
     hadoop jar wordcount2.jar WordCount2 /ruta_de_carpeta_input/ /ruta_destino_dentro_de_hadoop/
     ```

   - La carpeta de destino se creará automáticamente.

2. **Descargar Resultados**:
   - Obtén el archivo `part-r-00000` de Hadoop:
     ```bash
     hdfs dfs -get /ruta_del_part-r-00000_en_hadoop/ .
     ```

   - Guarda el archivo en la carpeta `Frequency2` del repositorio.

3. **Procesar Resultados**:
   - En `Frequency2`, ejecuta el script de Python para analizar los resultados:
     ```bash
     python freq-analysis2.py
     ```

   - Esto generará `freq-results-sorted.txt`.

## Recursos Adicionales

- **Archivos Generados**:
  - Los archivos generados se encuentran en los folders correspondientes en `linkDataset.txt`.
