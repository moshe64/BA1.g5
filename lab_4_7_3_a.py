from gnuradio import gr
import numpy as np
 
####################################################
##     Plantilla: clase e_add_cc                  ##
####################################################

# Se recomienda que el nombre de la clase finalice con una o dos letras especiales:
# nombre_ff: cuando en el bloque sus entradas y salidas son senales reales y de tipo flotante
# nombre_f: el bloque solo tiene una entrada o una salida y es una senal real de tipo flotante
# En vez de "f" pueden usarse: c (senal compleja),  i (entera), b (binaria), etc.
# Nota: esta plantilla tambien puede ser consultada en la libreria comdig_Lib_Bloques, dentro del bloque b_help
 
# Un bloque puede ser de varios tipos y eso se define en la clase como:
# gr.sync_block: cuando es de tipo sincrono
# gr.top_block: cuando es el flujograma principal
 
# gr.decim_block: cuando hay k muestras en la entrada por cada muestra saliente
# gr.interp_block: cuando hay k muestras en la salida por cada muestra entrante
# gr.hier_block2: cuando el bloque es como un flujograma
# gr.basic_block: otros casos

class e_add_cc(gr.sync_block):  
    """Aqui debes explicar como funciona el bloque, los parametros usados. En este caso particular el proposito es que esta clase sirva como ejemplo o plantilla para otras clase. La idea es que cada vez que vayas a crear una clase para un bloque GNU Radio vuelvas aqui ya que no es facil memorizar todos los detalles para crear un bloque GNU Radio. En todo caso, el ejemplo consiste en un bloque para una suma escalada de dos senales complejas. Por lo tanto hay dos senales de entrada y una de salida. Si escala=0.5 lo que se logra es promediar las dos senales"""

 # Dentro de la funcion __init__(), deben definirse los parametros de configuracion del bloque.
    # A cada parametro se le da un valor por defecto
    # ejemplo 1, solo hay un parametro de configuracion: def __init__(self, amp=1.0)
    # ejemplo 2, hay dos parametros: def __init__(self, amp=1.0, samp_rate= 32000)
    # a continuacion esta el caso de un solo parametro que hemos llamado escala
    def __init__(self, escala=0.5):
    
    
# En la siguiente funcion debes recordar que usaras:
        # sync: cuando tu bloque sea un bloque de tipo sincrono (por cada muestra entrante habra una saliente)
        # decim: cuando es un bloque decimador (por cada muestra saliente hay un numero entero de muestras entrantes)
        # interp: cuando es un bloque interpolador (por cada muestra entrante hay un numero entero de muestras salientes)
        # basic: cuando no hay relacion entre el numero de muestras entrantes y las salientes
        # mas en: https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_Python#3.3.1._Choosing_a_Block_Type
        
        
        gr.sync_block.__init__(
            self,
            # A continuacion se definen los tipos de senales de entrada y salida. Veamos algunos ejemplos:
            # [np.complex64]: cuando se tiene una sola senal y es compleja
            # [np.float32]: cuando se tiene una sola senal y es de tipo real y flotante
            # [np.float32, np.complex64]: cuando hay dos senales: una de tipo real flotante y la otra es compleja
            # otros casos: int8 o byte (entero de 8 bits, que en C++ se conoce como char)
            # No hemos explorado mas casos, pero no es tan sencillo. Uno supondria que otros casos posibles son:
            # int16 (en C++ se conoce como short), int32, int64. Los dos primeros funcionan, pero int64 no.
            # En el siguiente ejemplo hay dos entradas complejas y una salida real.
            in_sig=[np.complex64,np.complex64], 
            out_sig=[np.complex64]
        )
# las variables que entran como parametros del bloque deben ser declaradas nuevamente asi:
        self.escala=escala
 
        # abajo se puede escribir lo que se le antoje al programador, por ejemplo:
        # self.coef=1.0: define la variable global coef y le asigna el valor 1.0
        # self significa que es una variable global, que se puede invocar directamente desde otras funciones.
        # En todo caso, para las cosas que se definan aqui hay que tener en cuenta que:
        # -  esto es parte del constructor de la clase, por lo tanto, por cada bloque que se cree con esta clase
        #    estas cosas se invocaran solo una vez
        # -  Se supone que lo que se cree aqui es para ser usado, de manera que deberia ser usado en work()
        # A continuacion vamos a suponer que necesitamos usar constante  coef=1.0
        self.coef = 1.0
 
    # La funcion work() siempre debe estar presente en un bloque. Es alli donde estara la logica del bloque 
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala/self.coef
        return len(out0)

