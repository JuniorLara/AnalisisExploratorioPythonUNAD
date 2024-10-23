"""
Importo las librerias sys y os para tener un mejor control de las rutas de los directorios
Esto debido a que cree un archivo de constantes con las rutas de los archivos csv 
para aplicar buenas practicas de desarrollo y no declarar Magic Strings en el codigo. 
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))

#Importo mi Clase con las constantes declaradas con las rutas y algunos mensajes que utilizare 
from constantes import ConstantesMagicString

#Importo las librerias necesarias para el desarrollo del analisis exploratorio(pandas,numpy,seaborn,matplotlib)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Importo las funcionalidades necesarias para realizar la implementacion de los modelos de ciencia de datos
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix

class BusinessRules:

    def leer_datos_csv(ruta : str):
        pd.set_option(ConstantesMagicString.CONFIGURACION_GENERAL_OPCION_FORMATO, '{:.0f}'.format)
        return pd.read_csv(ConstantesMagicString.VEHICULOS_RUTA)
    
    def realizar_lectura_datos_analisis(datos : pd.DataFrame, cantidad_registros : int):
        return datos.head(cantidad_registros)

    def describir_datos_csv(datos: pd.DataFrame):
        return datos.describe()

    def generar_graficas_datos_obtenidos(datos: pd.DataFrame, header: str, mensaje: str):
        plt.figure(figsize=(6,9))
        sns.boxplot(x=datos[header])

        #Formateo los valores de notacion cientifica a un valor mas entendible para el usuario.
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

        #Muestro el resultado de nuestra grafica.
        plt.title(mensaje, fontsize=ConstantesMagicString.CONFIGURACION_GENERAL_TAMAÑO_FUENTE)

    def revision_datos_atipicos(datos : pd.DataFrame):
        print('Cantidad de autos con asientos mayor o igual a 10',(datos['seats'] >= 10).sum())
        # print(datos[(datos['selling_price'] > 400000) & (datos['year'] < 2015)])
        