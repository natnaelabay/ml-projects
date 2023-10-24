import io
import torch
import torch.nn as nn
from torchvision import datasets, transforms
from PIL import Image

class NeuralNet(nn.Module):
  def __init__(self,input_size,hidden_size,num_classes):
    super(NeuralNet,self).__init__()
    self.l1 = nn.Linear(input_size,hidden_size)
    self.relu = nn.ReLU()
    self.l2 = nn.Linear(hidden_size,num_classes)
  
  def forward(self,x):
    out = self.l1(x)
    out = self.relu(out)
    return self.l2(out) 

input_size = 224 * 224 * 3
hidden_size = 500
num_classes = 3
model = NeuralNet(input_size,hidden_size,num_classes)


PATH = "model.pth"
model.load_state_dict(torch.load(PATH))


#change image to tensor
def transform_image(image_bytes):
    transform = transforms.Compose([                                
                                transforms.Resize(255),
                                transforms.CenterCrop(224),
                                transforms.ToTensor()
                               ])
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)


#predict the image
def get_prediction(image_tensor):
    # print(image_tensor.shape)
    images = image_tensor.reshape(-1, input_size)#.to(device)    
    # return
    outputs = model(images)    
    _, predicted = torch.max(outputs.data, 1)
    return predicted


