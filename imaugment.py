# -*- coding: utf-8 -*-
import glob
import numpy as np
from PIL import Image, ImageOps

directory = ''#example --> './DATASET_resized/*'
brands = glob.glob(directory)
a, b = None # [min margin pixels, max margin pixels], example --> 10, 50
background_color = 'white'

for brand in brands:
	classes = glob.glob(brand + "/*")

	for cl in classes:
		images = glob.glob(cl + "/*")

		num_images = len(images)
		min_num_of_images = None # Select the minimum of images that you want in each class, example --> 4
		
		if num_images<min_num_of_images:
			for i in range(np.abs(num_images-min_num_of_images)):
				selected_image = int((num_images) * np.random.random_sample())
				image = images[selected_image]
				img = Image.open(image)
				border = int((b - a) * np.random.random_sample() + a)
				bimg = ImageOps.expand(img, border=border, fill=background_color).resize((img.size[0],img.size[1]))
				bimg.save('.' + image.split('.')[1] + '_' + str(border) + '.jpg')
