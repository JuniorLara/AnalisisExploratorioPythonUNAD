class MagicString:
    VALOR_CERO = 0
    PORCENTAJE_TEST = 0.20
    CONFIGURACION_GENERAL_TAMAÑO_FUENTE = 25
    CONFIGURACION_GENERAL_CANTIDAD_REGISTROS = 5
    CONFIGURACION_GENERAL_OPCION_FORMATO = 'display.float_format'
    CONFIGURACION_GENERAL_PANDA_WARGING = 'future.no_silent_downcasting'
    CONFIGURACION_GENERAL_REGULAR_EXPRESION_DIGITOS = '(\d+\.?\d*)'
    CONFIGURACION_GENERAL_SEPARADOR_TEXTO = '======================'

    #Constantes con los MagicString utilizados en el analisis exploratorio del csv de Vehiculos
    VEHICULOS_RUTA = './Datasets/car_details_v3.csv'
    VEHICULOS_HEADER_NAME = 'name'
    VEHICULOS_HEADER_YEAR ='year'
    VEHICULOS_HEADER_SELLING_PRICE = 'selling_price'
    VEHICULOS_HEADER_KM_DRIVEN = 'km_driven'
    VEHICULOS_HEADER_FUEL = 'fuel'
    VEHICULOS_HEADER_SELLER_TYPE = 'seller_type'
    VEHICULOS_HEADER_TRANSMISSION = 'transmission'
    VEHICULOS_HEADER_OWNER = 'owner'
    VEHICULOS_HEADER_MILEAGE = 'mileage'
    VEHICULOS_HEADER_ENGINE = 'engine'
    VEHICULOS_HEADER_MAX_POWER = 'max_power'
    VEHICULOS_HEADER_TORQUE = 'torque'
    VEHICULOS_HEADER_SEATS = 'seats'

    VEHICULOS_VALORES_ENCONTRADOS = 'RESUMEN DE LA INFORMACION ENCONTRADA'
    VEHICULOS_MENSAJE_VALORES_ATIPICOS = 'Identificación de datos faltantes y atípicos( {} )'

    VEHICULOS_VALORES_REMPLAZO_FUEL = {
        'Diesel' : 1,
        'Petrol' : 2,
        'LPG' : 3,
        'CNG' : 4,
    }
    
    VEHICULOS_VALORES_REMPLAZO_TRANSMISSION = {
        'Manual' : 0,
        'Automatic' : 1
    }

    VEHICULOS_VALORES_REMPLAZO_OWNER = {
        'First Owner' : 1, 
        'Second Owner': 2, 
        'Third Owner' : 3, 
        'Fourth & Above Owner' : 4,
        'Test Drive Car' : 5
    }

    VEHICULOS_VALOR_REMPLAZO_MILEAGE = '0 kmpl'
    VEHICULOS_VALOR_REMPLAZO_ENGINE = '0 CC'
    VEHICULOS_VALOR_REMPLAZO_MAX_POWER = '0 bhp'

    VEHICULOS_REGRESION_LINEAL_INTERCEPTO = 'Intercepto BETA 0: {}'
    VEHICULOS_REGRESION_LINEAL_COEFICIENTE = 'Coeficiente BETA 1: {}'

    #Constantes con los MagicString utilizados en el analisis exploratorio del csv de HEART DISEASE
    HEART_RUTA = './Datasets/heart_cleveland_upload.csv'