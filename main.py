import json

ann_path = "data/1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg.json"
img_path = "data/1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg"

img_name = "1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg"

# Opening JSON file
f = open(ann_path)
data = json.load(f)

objects = data["objects"]

labelme_shapes = []

for obj in objects:
    d = {
        'label': 'germ',
        'points': obj["points"]["exterior"],
        'group_id': None,
        'shape_type': 'rectangle',
        'flags': {}
    }
    labelme_shapes.append(d)

annotation = {
    "version": "4.2.5",
    "flags": {},
    "shapes": labelme_shapes,
    "imagePath": img_name,
    "imageData": None,
    "imageHeight": data["size"]["height"],
    "imageWidth": data["size"]["width"]
}


with open(img_name+'.json', 'w') as outfile:
    json.dump(annotation, outfile)