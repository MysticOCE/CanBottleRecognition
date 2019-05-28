from PIL import Image
import os, sys

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