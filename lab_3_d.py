#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Objetivo 3
# Generated: Thu Sep 13 11:39:57 2018
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import gr
from gnuradio import analog
from gnuradio import blocks
from gnuradio import qtgui
from gnuradio.filter import firdes

from PyQt5 import Qt
import sys, sip
###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class lab_3(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        
        fftsize = 2048
        
        ampl = 1
        
        self.rand = analog.noise_source_f(analog.GR_GAUSSIAN, ampl, 0)
        self.snk = qtgui.sink_f(
            fftsize,
            firdes.WIN_BLACKMAN_hARRIS,
            0,
            32000,
            "",
            True,
            True,
            True,
            True,
        )
        self.connect(self.rand, self.snk)
        
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()
        
        
###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################

def main():
    # Para que lo nuestro sea considerado una aplicación tipo QT GUI
    qapp = Qt.QApplication(sys.argv)
    practica = lab_3()
    practica.start()
    # Para arranque la parte grafica
    qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
            
        
        
