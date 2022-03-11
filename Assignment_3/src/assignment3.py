from random import randrange
import pandas as pd
import urllib.request
import os
os.environ["HDF5_USE_FILE_LOCKING"]='FALSE'
import sys
import h5py
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from random import randrange



from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import matplotlib.patches as patches
from display import get_cmap


def download_file(url):
    os.system(f'wget {url}')

def download_model():
    if not os.path.exists("./mse_model.h5?dl=0"):
        download_file("https://www.dropbox.com/s/95vmmlci5x3acar/mse_model.h5?dl=0")

download_model()

mse_file  = './mse_model.h5?dl=0'
mse_model = tf.keras.models.load_model(mse_file,compile=False,custom_objects={"tf": tf})

from nowcast_reader import read_data
x_test,y_test = read_data('./nowcast_testing.h5',end=50)

norm = {'scale':47.54,'shift':33.44}
hmf_colors = np.array( [ [82,82,82], [252,141,89],[255,255,191],[145,191,219]])/255

# models = [mse_model]
y_preds= []
# for i,m in enumerate(models):
#         yp = m.predict(x_test)
#         if isinstance(yp,(list,)):
#             yp=yp[0]
#         y_preds.append(yp*norm['scale']+norm['shift'])



locations = ['South Dakota','Nebraska','Kentucky','Vermont','Oregon']
def get_id(location):
    if location == locations[0]:
        return randrange(10)
    elif location == locations[1]:
        return randrange(10,20)
    elif location == locations[2]:
        return randrange(20,30)
    elif location == locations[3]:
        return randrange(30,40)
    elif location == locations[4]:
        return randrange(40,50)
    else:
        return None

def predict(location):
    id = get_id(location)
    if id == None:
        return None
    # if  y_preds.size==0:
    yp = mse_model.predict(x_test)
    if isinstance(yp,(list,)):
        yp=yp[0]
    y_preds.append(yp*norm['scale']+norm['shift'])
    
    file = save_images(id,y_preds)
    return file

def save_images(id,y_preds):
    y_preds = np.asarray(y_preds)
    y_preds = y_preds[0]
    for i in range(12):
        data_y = y_preds[id,:,:,i]
        filepath = "./images/"
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        plt.imsave(f"./images/{i}.jpg",data_y)
    return filepath


# for i in range(12):
#   data_y = y_preds[1,:,:,i]
#   plt.imshow(data_y, interpolation='nearest')
#   if not os.path.isdir("./images"):
#     os.mkdir("./images")
#   plt.imsave(f"./images/{i}.jpg",data_y)
#   plt.show()

