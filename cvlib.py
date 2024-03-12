import cv2
import argparse
import matplotlib.pyplot as plt
import numpy as np

def parse_user_data():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image',
                        type=str,
                        required=True,
                        help='Input image to be visualised')
    args = parser.parse_args()

    return args


def close_window():
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


def load_image(filename):

    img = cv2.imread(filename)

    if img is None:
        print(f"ERROR! - Image {filename} could not be read!")
        return -1
    
    return img

def visualise_image ( img , title ):
    cv2.imshow(title,img)
    cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE) 

    return None

def apply_rotation(img):
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    img_rotated = cv2.warpAffine(img, M, (w, h))
    return img_rotated

def apply_reflection ( img ):
    # Modify the following lines so that ' img_reflected ' is a copy of 'img '
    # reflected vertically .

    img_reflected = cv2.flip(img,1)

    # Return reflected image
    return img_reflected

def apply_translation(img):
    # Get the height and width of the image
    altura, ancho = img.shape[:2] #renglon /columna
    
    # Especificar los valores de traslación (tx y ty)
    tx, ty = 50, 50  # Ajustamos tx a 50 para la traslación a la derecha
    
    # Crear la matriz de traslación usando tx y ty
    matriz_traslacion = np.array([
        [1, 0, tx],
        [0, 1, ty]
    ], dtype=np.float32)
    
    # Aplicar la traslación a la imagen
    img_translated = cv2.warpAffine(src=img, M=matriz_traslacion, dsize=(ancho, altura)) #columnas/ renglones
    
    # Return the translated image
    return img_translated
