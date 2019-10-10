#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: If Else
# Generated: Thu Sep 13 11:39:57 2018
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import gr
from gnuradio import audio
from gnuradio import analog
from gnuradio import blocks
from gnuradio import qtgui
from gnuradio.filter import firdes

from PyQt4 import Qt
import sys, sip


#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class lab_3(gr.top_block):        # hereda de gr.top_block
     def __init__(self):
         gr.top_block.__init__(self)     # otra vez la herencia	
		
         sample_rate = 32000
         ampl = 10
	 fftsize = 2048
 
         self.sin0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 150, ampl)
         self.sin1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 100, ampl)
         play = audio.sink(sample_rate, "")
	 
	 self.add = blocks.add_ff()
	 self.thr = blocks.throttle(4, sample_rate, True)	
	 self.snk = qtgui.sink_f(
 	    fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
	 )
	 
         self.connect(self.sin0, (play, 0))
         self.connect(self.sin1, (play, 1))
  	 self.connect(self.sin0, (self.add, 0))
         self.connect(self.sin1, (self.add, 1))
         self.connect(self.add, self.thr, self.snk)

	 self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
	 self.pyobj.show()

#######################################################
# EL CÓDIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################
def main():
    # Para que lo nuestro sea considerado una aplicación tipo QT GUI
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = lab_3()
    simulador_de_la_envolvente_compleja.start()
    # Para arranque la parte grafica
    qapp.exec_()
 
# como el main lo hemos puesto como una funcion, ahora hay que llamarla
# podriamos escibir simplemete main(), pero es mas profesional asi:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass


