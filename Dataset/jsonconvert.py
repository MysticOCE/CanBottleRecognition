from pascal_voc_writer import Writer
import json

with open("Renders2/labels.json", "r") as read_file:
    data = json.load(read_file)

for dictionary in data:
	# x-yy-zp.png
	imageName = dictionary.get("image")
	# x-yy-zp
	fileName = imageName[:-4]
	writer = Writer('Renders2/'+imageName, 600, 400)
	for objects in dictionary.get("labels"):
		xmin = dictionary.get("labels").get(objects).get("x1")
		ymin = dictionary.get("labels").get(objects).get("y2")
		xmax = dictionary.get("labels").get(objects).get("x2")
		ymax = dictionary.get("labels").get(objects).get("y1")
		if (objects=='Can1') or (objects=="Can2"):
			oName = 'can'
		else:
			oName = 'bottle'
		writer.addObject(oName, xmin, ymin, xmax, ymax)
	writer.save('Renders2/'+fileName+'.xml')
# # writer = Writer('path/to/img.jpg', 800, 400)

# writer.addObject(name, xmin, ymin, xmax, ymax)

# # writer.addObject('bottle', 100, 100, 200, 200)

# # ::save(path)

# writer.save('Renders1/img.xml')