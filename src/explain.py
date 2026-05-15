from preprocess import preprocess_image
from gradcam import generate_heatmap
import cv2

image_path = "sample.jpg"

image = preprocess_image(image_path)

generate_heatmap(image)

print("Explanation generated")
