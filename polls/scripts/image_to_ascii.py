from PIL import Image
import numpy as np
import math

def read_image(path:str, scale: float = 1) -> Image.Image:
    image = Image.open(path)
    image = image.convert("RGB")
    image = image.resize((math.ceil(image.size[0]*scale), math.ceil(image.size[1]*scale)))
    return image

def get_pixels(image:Image.Image) -> np.array:
    data = np.array(image)
    return data

def convert_pixels_to_number(data: np.array, colors: int = 10) -> np.array:
    new_data = np.zeros(data.shape[:2], dtype="i")
    for row in range(len(data)):
        for pixel in range(len(data[row])):
            new_data[row][pixel] = sum(data[row][pixel])//3//(255/colors)-1
    return new_data

def to_zero(number:int) -> int:
    return 0

def zip_number_array(data: np.array, scale: int) -> np.array:
    new_data = np.zeros((data.shape[0]//scale, data.shape[1]), dtype="i")
    buffer = np.zeros((data.shape[1]), dtype="i")
    for row in range(data.shape[0]):
        if (row+1) % scale  != 0 :
            buffer += data[row]
        else:
            new_data[row//scale] = (data[row] + buffer)//scale
            buffer = to_zero(buffer)
    return new_data

def convert_number_to_char(data: np.array, palette: list) -> np.array:
    new_data = np.empty_like(data, dtype="U")
    for row in range(len(data)):
        for pixel in range(len(data[row])):
            new_data[row][pixel] = palette[data[row][pixel]]
    return new_data

def write_file(path: str, data: np.array) -> None:
    with open(path, "w") as file:
        for row in range(data.shape[0]):
            file.write("".join(data[row])+"\n") 
    return