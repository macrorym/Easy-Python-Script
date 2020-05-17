from PIL import Image
def get_paths(st:str):
    if '"' in st:
        st = st.replace('"', '')
        paths = st.split(",")
        return paths
    else:
        paths = st.split(",")
        return paths

def Reformat_Image(ImageFilePath):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height

        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        background = background.resize((2048,2048),Image.ANTIALIAS)
        background.save(ImageFilePath.split(".")[0]+"-resize.png")
        print("Image has been resized !")

    else:
        print("Image is already a square, it has not been resized !")

if __name__ == "__main__":
    while True:
        paths = input("Enter images path to be resized (separate paths with ,): ")
        p = get_paths(paths)
        for path in p:
            Reformat_Image(path)
        
