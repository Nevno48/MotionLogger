from PIL import Image, ImageChops
def cameraImageDifference(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    diff = ImageChops.difference(img1, img2)
    if(diff.getbbox()):
        diff.show()

img1 = "./allTimeLapse/2019:12:04:01:31:40.jpg"
img2 = "./allTimeLapse/2019:12:04:01:31:49.jpg"
cameraImageDifference(img1, img2)
