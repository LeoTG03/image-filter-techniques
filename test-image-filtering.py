import cv2 as cv
import argparse
import numpy as np
from matplotlib import pyplot as plt
import cvlib


def run_pipeline(): #Funcion principal

    args = cvlib.parse_user_data() #Funciones de cvlib para mostrar la imagen
    img = cvlib.load_image(args.input_image)

    if img is None:
        print('No hay imagen para cargar')
        return
    
    blur = cv.blur(img,(5,5))       #Filtros de OpenCV
    blur2 = cv.GaussianBlur(img,(5,5),0)
    median = cv.medianBlur(img,5)

    cvlib.visualise_image(img,"Imagen original")
    cvlib.visualise_image(blur, "Average Filter") #Exponer las imagenes con los titulos pertinetes
    cvlib.visualise_image(blur2, "Gaussian Filter")
    cvlib.visualise_image(median, "Median Filter")

    cvlib.close_window()

    print('Program finished! \n') #Finalizar el programa

if __name__ == '__main__': #ejecutar la funcion principal
    run_pipeline() 
