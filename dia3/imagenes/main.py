from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def get_image(image_file):
    image = Image.open(image_file)
    print(image.size)
    print(image.mode)
    print(image.format)
    image_blackwhite = image.convert('L')
    #image.show()
    #image_blackwhite.show()
    
    width = image.size[0]
    height = image.size[1]
    
    new_width = width // 5
    new_height = height // 5
    
    image_short = image.resize((new_width,new_height))
    #image_short.show()
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype('Roboto-Bold.ttf',120)
    
    draw.text(
        (10,0),
        "MATRIX PARA CODIGO G24",
        (255,255,255),
        font
    )
    image.show()
    
    
if __name__ == '__main__':
    get_image('matrix.jpg')