import imageio.v3 as img
filenames = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
images = []
for filename in filenames:
    images.append(img.imread(filename))
img.imwrite('idiot.gif', images, duration=500, loop = 0)   # duration in seconds per frame