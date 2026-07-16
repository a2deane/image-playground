#matrix = [[(56, 41, 56), (56, 41, 56), (56, 41, 56), (40, 30, 40), (106, 106, 106), (106, 106, 106), (40, 30, 40), (40, 30, 40), (40, 30, 40), (40, 30, 40)], [(74, 55, 74), (56, 41, 56), (106, 106, 106), (106, 106, 106), (106, 106, 106), (106, 106, 106), (106, 106, 106), (106, 106, 106), (40, 30, 40), (40, 30, 40)], [(56, 41, 56), (106, 106, 106), (106, 106, 106), (106, 106, 106), (190, 158, 175), (190, 158, 175), (106, 106, 106), (106, 106, 106), (106, 106, 106), (40, 30, 40)], [(56, 41, 56), (106, 106, 106), (106, 106, 106), (106, 106, 106), (190, 158, 175), (190, 158, 175), (190, 158, 175), (106, 106, 106), (106, 106, 106), (40, 30, 40)], [(106, 106, 106), (106, 106, 106), (190, 158, 175), (190, 158, 175), (171, 131, 152), (171, 131, 152), (190, 158, 175), (92, 92, 92), (106, 106, 106), (92, 92, 92)], [(106, 106, 106), (106, 106, 106), (190, 158, 175), (171, 131, 152), (171, 131, 152), (171, 131, 152), (171, 131, 152), (92, 92, 92), (106, 106, 106), (92, 92, 92)], [(56, 41, 56), (106, 106, 106), (106, 106, 106), (171, 131, 152), (171, 131, 152), (171, 131, 152), (171, 131, 152), (92, 92, 92), (92, 92, 92), (40, 30, 40)], [(56, 41, 56), (106, 106, 106), (106, 106, 106), (106, 106, 106), (92, 92, 92), (92, 92, 92), (92, 92, 92), (106, 106, 106), (92, 92, 92), (56, 41, 56)], [(40, 30, 40), (56, 41, 56), (106, 106, 106), (106, 106, 106), (106, 106, 106), (106, 106, 106), (92, 92, 92), (92, 92, 92), (56, 41, 56), (56, 41, 56)], [(40, 30, 40), (40, 30, 40), (56, 41, 56), (56, 41, 56), (92, 92, 92), (92, 92, 92), (56, 41, 56), (56, 41, 56), (74, 55, 74), (56, 41, 56)]]

from PIL import Image
from time import sleep as wait
im = Image.open('bean.png')

pixels = im.load()

horizontal, vertical = im.size

image_matrix = []

## Image Encoding

# Organize RGB vectors into matrix

# Get horizontal pixel coordinate
for pix_horizontal in range(horizontal):
    # create new row in the matrix
    image_matrix.append([])
    # get vertical pixel coordinate for each horizontal pixel coordinate
    for pix_vertical in range(vertical):
        # get RGB vectors for each pixel
        data = pixels[pix_horizontal, pix_vertical]        
        # append RGB vectors to respective horizontal row
        image_matrix[pix_horizontal].append(data)



## Image Decoding

# Assign appropriate values for width, height
width, height = len(image_matrix),len(image_matrix[0])
img = Image.new('RGB', (width, height))
pixels = img.load()

# For each pixel coordinate in width
for x in range(width):

    # for each pixel coordinate in height
    for y in range(height):
        # assign the RGB vector (tuple) to the current x, y pixel coordinates
        rgb_vect = image_matrix[x][y] 
        r = rgb_vect[0]
        g = rgb_vect[1]
        b = rgb_vect[2]
        # create pixel with image data
        pixels[x,y] = (r,g,b)
        print(f'loaded pixel {x, y}')

        img.save('test.jpg')








def encode_image(file):
    image = Image.open(f'{file}')
    horizontal, vertical = image.size
    image_matrix = []

    for pix_horizontal in range(horizontal):
        image_matrix.append([])
        for pix_vertical in range(vertical):
            data = pixels[pix_horizontal, pix_vertical]
            image_matrix[pix_horizontal].append(data)
    print('image decoded')

def decode_image(data, width, height, name):
    img = Image.new('RGB',(width, height))
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            rgb_vect = image_matrix[x][y]
            r = rgb_vect[0]
            g = rgb_vect[1]
            b = rgb_vect[2]
            
            pixels[x,y] = (r, g, b)
            print(f'loaded pixel {x, y}')
    img.save(f'{name}.jpg')

data = encode_image('bean.jpg')

print(data)