import json
import os
from tqdm import tqdm

# ann_path = "data/1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg.json"
# img_path = "data/1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg"
#
# img_name = "1-18564-TA 98-5000-A-S9 _28_04_2023_11_44_45.jpg"


OUTPUT_FOLDER = r"C:\Users\tristan_cotte\PycharmProjects\Supervisely2Labelme\Output"
INPUT_FOLDER = r"C:\Users\tristan_cotte\PycharmProjects\Supervisely2Labelme\sly_dataset\ann"
extension = ".jpg"

for json_name in tqdm(os.listdir(INPUT_FOLDER)):
    img_name = json_name.split(".")[0]
    ann_path = os.path.join(INPUT_FOLDER, json_name)

    # Opening JSON file
    f = open(ann_path)
    data = json.load(f)

    objects = data["objects"]

    labelme_shapes = []

    for obj in objects:
        labelme_shapes.append({
            'label': 'germ',
            'points': obj["points"]["exterior"],
            'group_id': None,
            'shape_type': 'rectangle',
            'flags': {}
        })

    annotation = {
        "version": "4.2.5",
        "flags": {},
        "shapes": labelme_shapes,
        "imagePath": img_name + extension,
        "imageData": None,
        "imageHeight": data["size"]["height"],
        "imageWidth": data["size"]["width"]
    }

    with open(os.path.join(OUTPUT_FOLDER, img_name + '.json'), 'w') as outfile:
        json.dump(annotation, outfile)
