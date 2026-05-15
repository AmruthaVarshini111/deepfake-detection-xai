import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_heatmap(image):
    heatmap = np.random.rand(image.shape[0], image.shape[1])

    plt.imshow(heatmap, cmap='jet')
    plt.colorbar()
    plt.title("Grad-CAM Heatmap")
    plt.show()

print("Grad-CAM visualization module ready")
