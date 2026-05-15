from preprocess import preprocess_image
from model import DeepFakeCNN
import torch

model = DeepFakeCNN()

image = preprocess_image("sample.jpg")

output = model(image)

prediction = torch.argmax(output, dim=1)

if prediction.item() == 0:
    print("Prediction: REAL")
else:
    print("Prediction: FAKE")
