#Importo mi Clase con las constantes declaradas con las rutas y algunos mensajes que utilizare 
from Business.constantes import MagicString

#Importo las librerias necesarias para el desarrollo del analisis exploratorio(pandas,numpy,seaborn,matplotlib)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Importo las funcionalidades necesarias para realizar la implementacion de los modelos de ciencia de datos
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, average_precision_score, RocCurveDisplay

class General:

    def leer_datos_csv(ruta : str):
        pd.set_option(MagicString.CONFIGURACION_GENERAL_OPCION_FORMATO, '{:.0f}'.format)
        Datos = pd.read_csv(MagicString.VEHICULOS_RUTA)

        # Remuevo registros que puedan estar duplicados
        Datos.drop_duplicates(inplace=True)

        return Datos
    
    def realizar_lectura_datos_analisis(datos : pd.DataFrame, cantidad_registros : int):
        return datos.head(cantidad_registros)

    def describir_datos_csv(datos: pd.DataFrame):
        return datos.describe()

    def generar_grafica_datos_obtenidos(datos: pd.DataFrame, header: str, mensaje: str):
        plt.figure(figsize=(6,9))
        sns.boxplot(x=datos[header])

        #Formateo los valores de notacion cientifica a un valor mas entendible para el usuario.
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

        #Muestro el resultado de nuestra grafica.
        plt.title(mensaje, fontsize=MagicString.CONFIGURACION_GENERAL_TAMAÑO_FUENTE)
    
    def dividir_registros_train_y_test(datos : pd.DataFrame, header : str, state):
        X = datos.drop(header, axis=1)
        Y = datos[header]

        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=state)

        return x_train, x_test, y_train, y_test

    def evaluar_desempeño_modelo_presicion(modelo, y_test):
        print(classification_report(y_test, modelo,zero_division=0))

    def entrenar_modelo_regresion_logistica(x_train, y_train, x_test):
        regresion_logistica_modelo = LogisticRegression(solver='liblinear')
        regresion_logistica_modelo.fit(x_train, y_train)

        return regresion_logistica_modelo.predict(x_test)
    
    def matriz_de_confusion(y_test, prediccion):
        # Generar grafica matriz de confusion
        matriz_confusion = confusion_matrix(y_test, prediccion)
        disp = metrics.ConfusionMatrixDisplay(confusion_matrix = matriz_confusion)

        return disp.plot()

    def curva_de_precision_modelo(y_test, prediccion, title):
        RocCurveDisplay.from_predictions(y_test, prediccion)
        plt.title(title, fontsize=MagicString.CONFIGURACION_GENERAL_TAMAÑO_FUENTE)
        plt.show()

    def realizar_imputacion_de_datos_para_datos_atipicos(datos : pd.DataFrame, nombre_columna: str) -> pd.DataFrame:
        # Calculo el Quartile 1 y Quartile 3
        Q1 = datos[nombre_columna].quantile(0.25)
        Q3 = datos[nombre_columna].quantile(0.75)
        IQR = Q3 - Q1

        #defino los limites de mis datos.
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        # Calcular la mediana
        mediana = datos[nombre_columna].median()

        # Imputar outliers con la mediana
        return  datos[nombre_columna].mask((datos[nombre_columna] < limite_inferior) | (datos[nombre_columna] > limite_superior), mediana)

    def regresion_lineal_obtener_intercepto_coeficiente(datos : pd.DataFrame, columna_x, columna_y):
        X = datos[[columna_x]]
        Y = datos[columna_y]

        regresion_lineal_modelo = LinearRegression()
        regresion_lineal_modelo.fit(X, Y)

        intercepto = regresion_lineal_modelo.intercept_
        coeficiente = regresion_lineal_modelo.coef_

        print(MagicString.VEHICULOS_REGRESION_LINEAL_INTERCEPTO.format(intercepto))
        print(MagicString.VEHICULOS_REGRESION_LINEAL_COEFICIENTE.format(coeficiente))

        #Visualizar Regresion Lineal.
        plt.scatter(datos[columna_x], Y, color='blue', label='Datos Reales')
        plt.plot(datos[columna_x], regresion_lineal_modelo.predict(X), color='red', label='Linea de Regresion')
        plt.title('Regresion Lineal: Kilometraje vs Precio')
        plt.xlabel('Km')
        plt.ylabel('Valor (USD)')
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        plt.legend()
        plt.show()

        km = [[32478],[47852],[61203],[84756],[122222]]
        precio_prediccion = regresion_lineal_modelo.predict(km)

        for i, item in enumerate(km):
            print(f'Kilometraje predicho para un carro con kilometraje {item[0]} = {precio_prediccion[i]}')

    def arbol_de_decision(predictor : pd.DataFrame, target : pd.DataFrame):
        print('hola')

