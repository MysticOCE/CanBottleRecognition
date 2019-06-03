from PIL import Image
import os, sys

# pass in some tuple/list of PIL images and we can mass resize them here
def resize_batch(images, reducer):
	for image in images:
		image_resize(image, reducer)
		print("resized an image")
		image.show()
	

# accepts PIL image, reduces image to size/reducer. ie. reducer of 2 halves size of image.
def image_resize(image, reducer):
	size = image.size
	xscale = size[0]
	yscale = size[1]
	print(xscale)
	print(yscale)
	xdown = int(xscale/reducer)
	ydown = int(yscale/reducer)
	print(xdown)
	print(ydown)
	output = image.resize((xdown,ydown), Image.NEAREST)
	return output



im = Image.open("Tristan.png")
im2 = Image.open("Tristan.png")

images = [im, im2]
resize_batch(images,2)

def old():
	im = Image.open("Tristan.png")
	out = im.resize((256,224))
	print(out.size)
	out.show()
	#out.save("Resize1.png")
	out2 = im.resize((512,448))
	print(out2.size)
	out2.show()
	#out2.save("Resize2.png")
	#ratio's are 3:2 and 4:3