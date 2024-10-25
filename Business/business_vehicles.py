from Business.constantes import MagicString
from Business.business_logic_general import General

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

pd.set_option(MagicString.CONFIGURACION_GENERAL_PANDA_WARGING, True)

class Vehicles:
    def ver_detalles_columnas_texto(datos : pd.DataFrame):
        print(datos[MagicString.VEHICULOS_HEADER_FUEL].unique())
        print(MagicString.CONFIGURACION_GENERAL_SEPARADOR_TEXTO)
        print(datos[MagicString.VEHICULOS_HEADER_TRANSMISSION].unique())
        print(MagicString.CONFIGURACION_GENERAL_SEPARADOR_TEXTO)
        print(datos[MagicString.VEHICULOS_HEADER_OWNER].unique())
        print(MagicString.CONFIGURACION_GENERAL_SEPARADOR_TEXTO)
        print(datos[MagicString.VEHICULOS_HEADER_MAX_POWER].unique())
        print(MagicString.CONFIGURACION_GENERAL_SEPARADOR_TEXTO)
        print(datos[MagicString.VEHICULOS_HEADER_SELLER_TYPE].unique())
    
    def realizar_ajustes_en_datos(datos : pd.DataFrame):
        datos[MagicString.VEHICULOS_HEADER_NAME] = datos[MagicString.VEHICULOS_HEADER_NAME].str.split().str[MagicString.VALOR_CERO]

        datos[MagicString.VEHICULOS_HEADER_FUEL] = datos[MagicString.VEHICULOS_HEADER_FUEL].replace(MagicString.VEHICULOS_VALORES_REMPLAZO_FUEL)
        datos[MagicString.VEHICULOS_HEADER_FUEL] = datos[MagicString.VEHICULOS_HEADER_FUEL].astype(int)

        datos[MagicString.VEHICULOS_HEADER_TRANSMISSION] = datos[MagicString.VEHICULOS_HEADER_TRANSMISSION].replace(MagicString.VEHICULOS_VALORES_REMPLAZO_TRANSMISSION)
        datos[MagicString.VEHICULOS_HEADER_TRANSMISSION] = datos[MagicString.VEHICULOS_HEADER_TRANSMISSION].astype(int)
        
        datos[MagicString.VEHICULOS_HEADER_OWNER] = datos[MagicString.VEHICULOS_HEADER_OWNER].replace(MagicString.VEHICULOS_VALORES_REMPLAZO_OWNER)
        datos[MagicString.VEHICULOS_HEADER_OWNER] = datos[MagicString.VEHICULOS_HEADER_OWNER].astype(int)

        #Obtengo el valor entero de la columna y remplazo los valores 0 por la media MILEAGE.
        datos[MagicString.VEHICULOS_HEADER_MILEAGE] = datos[MagicString.VEHICULOS_HEADER_MILEAGE].fillna(MagicString.VEHICULOS_VALOR_REMPLAZO_MILEAGE)
        datos[MagicString.VEHICULOS_HEADER_MILEAGE] = datos[MagicString.VEHICULOS_HEADER_MILEAGE].str.extract(MagicString.CONFIGURACION_GENERAL_REGULAR_EXPRESION_DIGITOS).astype(float)
        datos[MagicString.VEHICULOS_HEADER_MILEAGE] = datos[MagicString.VEHICULOS_HEADER_MILEAGE].replace(MagicString.VALOR_CERO,datos[MagicString.VEHICULOS_HEADER_MILEAGE].mean())  
        
        #Remplazo los valores NULO por un valor por defecto(0 CC), obtengo la parte entera y remplazo los valores 0 por la media.
        datos[MagicString.VEHICULOS_HEADER_ENGINE] = datos[MagicString.VEHICULOS_HEADER_ENGINE].fillna(MagicString.VEHICULOS_VALOR_REMPLAZO_ENGINE)
        datos[MagicString.VEHICULOS_HEADER_ENGINE] = datos[MagicString.VEHICULOS_HEADER_ENGINE].str.extract(MagicString.CONFIGURACION_GENERAL_REGULAR_EXPRESION_DIGITOS).astype(int)
        datos[MagicString.VEHICULOS_HEADER_ENGINE] = datos[MagicString.VEHICULOS_HEADER_ENGINE].replace(MagicString.VALOR_CERO,datos[MagicString.VEHICULOS_HEADER_ENGINE].mean())
        datos[MagicString.VEHICULOS_HEADER_ENGINE] = datos[MagicString.VEHICULOS_HEADER_ENGINE].astype(int)

        datos[MagicString.VEHICULOS_HEADER_MAX_POWER] = datos[MagicString.VEHICULOS_HEADER_MAX_POWER].fillna(MagicString.VEHICULOS_VALOR_REMPLAZO_MAX_POWER)
        datos[MagicString.VEHICULOS_HEADER_MAX_POWER] = datos[MagicString.VEHICULOS_HEADER_MAX_POWER].str.extract(MagicString.CONFIGURACION_GENERAL_REGULAR_EXPRESION_DIGITOS).astype(float)
        datos[MagicString.VEHICULOS_HEADER_MAX_POWER] = datos[MagicString.VEHICULOS_HEADER_MAX_POWER].replace(MagicString.VALOR_CERO, datos[MagicString.VEHICULOS_HEADER_MAX_POWER].mean())
        datos[MagicString.VEHICULOS_HEADER_MAX_POWER] = datos[MagicString.VEHICULOS_HEADER_MAX_POWER].replace('nan',datos[MagicString.VEHICULOS_HEADER_MAX_POWER].mean())
        datos[MagicString.VEHICULOS_HEADER_MAX_POWER] = datos[MagicString.VEHICULOS_HEADER_MAX_POWER].replace(' bhp',datos[MagicString.VEHICULOS_HEADER_MAX_POWER].mean())

        datos[MagicString.VEHICULOS_HEADER_SEATS] = datos[MagicString.VEHICULOS_HEADER_SEATS].fillna(MagicString.VALOR_CERO)
        datos[MagicString.VEHICULOS_HEADER_SEATS] = datos[MagicString.VEHICULOS_HEADER_SEATS].replace(MagicString.VALOR_CERO, datos[MagicString.VEHICULOS_HEADER_SEATS].mean())
        datos[MagicString.VEHICULOS_HEADER_SEATS] = datos[MagicString.VEHICULOS_HEADER_SEATS].astype(int)

        # Remuevo registros que puedan estar nulos
        datos.dropna(inplace=True)

        return datos