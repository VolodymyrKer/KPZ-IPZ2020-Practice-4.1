from PIL import Image

def cut_image_by_quarter(path):
    if not isinstance(path, str):
        raise Exception("There should be a string")

    image = Image.open(path)
    width = image.size[0]
    heigth = image.size[1]
    new_image = image.resize((int(width*0.75), int(heigth*0.75)))
    path_cropped = "image/cropped/cropped.jpg"
    new_image.convert("L").save(path_cropped)
    return path_cropped

test = Image.open(cut_image_by_quarter("image/original/image.jpg"))
test.show()