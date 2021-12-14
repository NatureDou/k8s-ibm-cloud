import json
import requests
import numpy as np
from PIL import Image
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
	description='Testing the flask app for MNIST inference.'
    	)
    parser.add_argument('--address', default='http://0.0.0.0:5000/inference')
    args = parser.parse_args()
    address = args.address
    
    image = Image.open('test_image.jpg')
    pixels = np.array(image)
    data = {'images':pixels.tolist()}
    
    headers = {'Content-Type':'application/json'}
    
    result = requests.post(address, data=json.dumps(data), headers=headers)
    print(str(result.content, encoding='utf-8')) 