"""
PARTE 1: No es exactamnete el mismo concepto de constantes wue en otros lenuajes de programacion
si no que en Python simplemente es una conencion,ya que realmente no existe el concepto de
constantes en Python tal cual

EL CONCEPTO DE CONSTANTES TIENE QUE VER CON DEFINIR UNA VARIABLE Y QUE NO PODEMOS MODIFICAR SU VALOR
este es el concepto de cualquier lenguaje , EN JAVA ESTE CONCEPTO TIENE UN PESO FUERTE, EN PYTHON
YA NO ES LO MISMO simplemente una convencion ya que realmente no existe el concepto
Una vez que le hemos asignado el valor a esta variable QUE QUEREMOS QUE SEA CONSTANTE,ese consepto tal cual no existe el Python
Asi que en Python a cualquier variable le podemos volver a asignar un valor
Sin embargo existe una convencion para trabajar el concepto de constantes y poder simular este concepto en Python, osea que es
una simulacion la CONSTANTE, simplemente vamos a mostrar que es una constante que nosotros queremos que esa variable sea una constante
pero no es que lo acepta el lenguaje definitivamente, si no que es todo una simulacion en Python

El nombre de la variable debe desribirse en MAYUSCULA.Esto es lo que representa en Python una constante
esto es parte de la CONVENCION y de la SIMULACION
UNA CONSTANTE PARA PODER IDENTIFICARLA EN primer lugar IDENTIFICAMOS el NOMBRE DE LA VARIABLE
ej: en este caso pondremos CONSTANTE
si el NOMBRE DE LA VARIABLE tiene mas de una palabra,entonces si tenemos MI_CONSTANTE ,vamos a separar cada
palabra por guion bajo,ESTO ES PARTE DE LA CONVENCION PARA DEFINIR EL NOMBRE DE UNA CONSTANTE .

PARTE 2: Ahora se acostumbra que estas variables que son CONSTANTES, se definan en un archivo, en un modulo por
separdo y SE UTILCEN FUERA DE ESTE MODULO
VAMOS A CREAR OTRO MODULO

"""
#VAMOS A CREAR UNA CLASE LLAMADA MATEMATICAS

class Matematicas: #dentro de esta clase vamos a crear una CONSTANTE
    PI =3.1416  # ESTA ES UNA VARIABLE DE CLASE CONSTANTE

MI_CONSTANTE = 'Esta es una variable constante '

