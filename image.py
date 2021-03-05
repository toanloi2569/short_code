# read img cv2 
import cv2
image = cv2.imread(input_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# numpy image to base64
from PIL import Image
from io import BytesIO
import base64
rotated_image = Image.fromarray(rotated_image, 'RGB')
rotated_image.save(buffered, format="JPEG")
image_base64 = base64.b64encode(buffered.getvalue()).decode("ascii")
