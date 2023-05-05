import matplotlib.pyplot as plt
from skimage import segmentation
import cv2
from skimage import color
from PIL import Image

def Apte(image1,image2):

    fig, ax = plt.subplots(2,1, figsize = (20,30))

    # ax[0].imshow((cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)))
    ax[0].imshow(image2)
    ax[0].axis('off')
    # ax[1].imshow((cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)))
    ax[1].imshow(image1)
    ax[1].axis('off')
    fig.savefig("heelo.png",bbox_inches='tight',facecolor='#ffffff')
