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
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, RocCurveDisplay
from sklearn.preprocessing import label_binarize
from sklearn.tree import DecisionTreeClassifier, plot_tree

class General:

    def leer_datos_csv(ruta : str):
        pd.set_option(MagicString.CONFIGURACION_GENERAL_OPCION_FORMATO, '{:.0f}'.format)
        Datos = pd.read_csv(ruta)

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
    

    def genera_grafica_de_correlacion(datos : pd.DataFrame):
        plt.figure(figsize=(10,10))
        sns.heatmap(datos.corr(), annot=True, cmap='coolwarm')
        plt.title(MagicString.MATRIZ_CORRELACION_TITLE)
        plt.show()


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
    
    
    def graficar_curva_precision_recall(train_x, train_y, test_x, test_y):
        # Entrenar el modelo
        modelo = LogisticRegression(multi_class='ovr', max_iter=5000)
        modelo.fit(train_x, train_y)

        # Predecir las probabilidades para el conjunto de prueba
        y_scores = modelo.predict_proba(test_x)

        # Binarizar las clases (si son múltiples clases)
        y_test_binarized = label_binarize(test_y, classes=np.unique(train_y))

        # Calcular precisión y recall para cada clase
        precision = {}
        recall = {}
        for i in range(y_scores.shape[1]):
            precision[i], recall[i], _ = precision_recall_curve(y_test_binarized[:, i], y_scores[:, i])

        # Graficar
        plt.figure(figsize=(10, 6))
        for i in range(y_scores.shape[1]):
            plt.plot(recall[i], precision[i], label=f'Clase {i}')

        plt.xlabel(MagicString.CONFIGURACION_GENERAL_X_RECALL)
        plt.ylabel(MagicString.CONFIGURACION_GENERAL_Y_RECALL)
        plt.title(MagicString.CONFIGURACION_GENERAL_TITLE_RECALL)
        plt.legend()
        plt.grid()
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
        x_train, x_test, y_train, y_test = General.dividir_registros_train_y_test(datos, columna_y, 0)

        X = x_test[[columna_x]]
        Y = y_test

        regresion_lineal_modelo = LinearRegression()
        regresion_lineal_modelo.fit(x_train[[columna_x]], y_train)

        intercepto = regresion_lineal_modelo.intercept_
        coeficiente = regresion_lineal_modelo.coef_

        print(MagicString.VEHICULOS_REGRESION_LINEAL_INTERCEPTO.format(intercepto))
        print(MagicString.VEHICULOS_REGRESION_LINEAL_COEFICIENTE.format(coeficiente))

        #Visualizar Regresion Lineal.
        plt.scatter(x_test[columna_x], Y, color='blue', label='Datos Reales')
        plt.plot(x_test[columna_x], regresion_lineal_modelo.predict(X), color='red', label='Linea de Regresion')
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
            print(f'Precio predicho para un carro con kilometraje {item[0]} = $ {precio_prediccion[i]}')

    def generar_arbol_de_decision(x_train, y_train, x_test, y_test):
        tree = DecisionTreeClassifier()
        tree.fit(x_train, y_train)
        modelo = tree.predict(x_test)
        
        General.evaluar_desempeño_modelo_presicion(modelo, y_test)

        plot_tree(tree)

