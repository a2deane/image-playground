from PIL import Image, ImageMath
from pprint import pprint



def encode_image(file):
    image = Image.open(f'{file}')
    pixels = image.load()
    horizontal, vertical = image.size
    image_matrix = []

    # for each horizontal pixel column, encode the vertical pixels under it
    for pix_horizontal in range(horizontal):
        image_matrix.append([])
        for pix_vertical in range(vertical):
            data = pixels[pix_horizontal, pix_vertical]
            
            # Load colour data into matrix
            image_matrix[pix_horizontal].append(data)
            print(f'Encoded pixel {pix_horizontal, pix_vertical}')
    print('image encoded')
    return image_matrix

def decode_image(data, width, height, name):
    img = Image.new('RGB',(width, height))
    pixels = img.load()

    # For each horizontal pixel, fill in the 'column'
    for x in range(width):
        for y in range(height):
            # Gather RGB tuple in current pixel coordinate
            rgb_vect = data[x][y]
            r = rgb_vect[0]
            g = rgb_vect[1]
            b = rgb_vect[2]
            
            pixels[x,y] = (r, g, b)
            print(f'Decoded pixel {x, y}')
    img.save(f'{name}.jpg')
    print('Image decoded successfully!')


data = encode_image('large.jpg')

#decode_image(data, len(data),len(data[0]),'asd')