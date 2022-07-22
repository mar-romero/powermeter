# Powermeter

En la carpeta Ejercicio 2 se encuentra resuelto dicho ejercicio.

Con respecto a la api creada origine vista mas agradables 
para enviar datos, modificar, consultar o actualizar datos gracias a framewokrs rest_framework.decorators

La api comienza el path http://localhost:8000/api/ y para realizar los diferentes pedidos se crearon los siguentes path:
    # save/
    En este path se envia un JSON ({"mediciones": [1, -2, 3.2, 7]}) y este lo guarda en la base de datos sqlite en diferentes objetos dentro de un array.
    Ejemplo:
    [
    {
        "mediciones": 1.0
    },
    {
        "mediciones": -2.0
    },
    {
        "mediciones": 3.2
    },
    {
        "mediciones": 7.0
    }
    ]
    
    # list/
    Es ente path se muestran todas las mediciones
    # max/
    Muestra la maxima medicion que se guardo en la base de datos
    # min/
    Muestra la minima medicion que se guardo en la base de datos
    # avg/
    Muestra el promedio de las mediciones que se guardo en la base de datos
    # api/<int:pk>(el id deseado)
    Indicando el ID de la medicion muestra solamente dicho dato,

