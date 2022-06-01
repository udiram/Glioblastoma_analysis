import slideio as slideio
from matplotlib import pyplot as plt

image_path = '../data/TCGA-02-0333-01Z-00-DX2.2163628B-0639-46D6-9587-060955EF1031.svs'

slide = slideio.open_slide(image_path,'SVS')
num_scenes = slide.num_scenes
scene = slide.get_scene(0)
print(num_scenes, scene.name, scene.rect, scene.num_channels)

slide = slideio.open_slide(image_path,"SVS")
raw_string = slide.raw_metadata
raw_string.split("|")
print(raw_string)

image = scene.read_block((5000, 5000, 5000, 5000), size=(500,0))
plt.imshow(image)
plt.show()