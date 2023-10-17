from rembg import remove
from PIL import Image
import numpy as np
import io

input_path='img3.jpg'
output_path='removed_bg3.png'

inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
output.show()
