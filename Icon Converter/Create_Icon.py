from PIL import Image

def create_icon(file, save_as):
    img = Image.open(file)
    width, height = img.size

    if width != height:
        print(r"Image Dimensions Don't Match, Cropping...")
        print(r"Dimensions (w, h): ", (width, height))

        if width > height:
            left, right, top, bottom = (width-height)/2, (width-height)/2 + height, 0, height
        else:
            left, right, top, bottom = 0, width, (height-width)/2, (height-width)/2 + width

        img = img.crop((left, top, right, bottom))
        print(r"New Image Size (w, h): ", (img.size[0], img.size[1]))

    img.resize((256, 256))
    img.save(save_as)
    img.close()
    print("Image Saved: ", save_as)
