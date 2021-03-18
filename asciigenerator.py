from PIL import Image

characters = ['@', '#', 'S', '$', '*', ';', ':', ',', '.','-', '_']

# Resize image
def image_resize(image, new_width = 150):
    width, height = image.size
    ratio = height / width 
    new_height = int(new_width * ratio)
    image_resize = image.resize((new_width, new_height))
    return(image_resize)

# convert each pixel to greyscale
def greyscaled(image):
    greyscaled_image = image.convert('L')
    return(greyscaled_image)

# convert pixels to a string of corresponding of ASCII values
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_char = ''.join([characters[pixel//25] for pixel in pixels])
    return(ascii_char)

def take_image_path(new_width=150):
    # Using User Input
    path = input("Enter a valid path to the image ==>> \n ")
    try:
        image = Image.open(path)
    except Exception as e:
        print(path, "is not a valid image path! Try again.")

    # Convert image to ascii
    new_data = pixels_to_ascii(greyscaled(image_resize(image)))

    # format in our aspect ratio
    pixel_count = len(new_data)
    ascii_image = '\n'.join([new_data[i:(i+new_width)] for i in range( 0, pixel_count, new_width)])

    #print
    print(ascii_image)

    #save output
    with open('asciiimage.txt', 'w') as f:
        f.write(ascii_image)

take_image_path()