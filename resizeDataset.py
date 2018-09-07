import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import os
import scipy.misc
from PIL import Image


def Square_Img(image_path, N):

	im = Image.open(image_path)
	img = np.asarray(im.convert('RGB'))
		
	plt.imshow(img)
	plt.show()
	shape = img.shape
	
	if shape[0]==shape[1]:
		new_img = img

	else:
		s = max(shape)
		s_ind = shape.index(s)
		new_img  = np.ones((s,s,3))*255
		diff = np.abs(shape[0]-shape[1])

		ov = np.zeros(2)
		ov[np.abs(s_ind-1)] = int((shape[s_ind]-shape[np.abs(s_ind-1)])/2)
				
		new_img[int(ov[0]):s-int(ov[0]), int(ov[1]):s-int(ov[1]),:] = img

	return cv2.resize(new_img,(int(N),int(N)))

###################################################################################################
###################################################################################################
###################################################################################################


directory = '' # Folder containing the folders of the images to resize, example --> './DATASET/*'
classes = glob.glob(directory)
for subclass in classes:
	print("Processing brand " + subclass)
	items = glob.glob(subclass + "/*")
	for item in items:
		files = glob.glob(item + "/*")

		ref = []
		new = []

		# Delete anything is not an image
		for f in files:
			if f.split('.')[-1] == 'jpg' and f.split('.')[-1] != 'jpeg' and f.split('.')[-1] != 'png' and f.split('.')[-1] != 'JPG' and f.split('.')[-1] != 'jpe'   and f.split('.')[-1] != 'tif':

				#img_res = Square_Img(f, 224)
				try:
					img_res = Square_Img(f, 224)
					f_split = f.split('/')

					directory = './DATASET_resized/' + f_split[2]
					if not os.path.exists(directory):
						os.makedirs(directory)

					directory = directory + '/' + f_split[3]
					if not os.path.exists(directory):
						os.makedirs(directory)

					scipy.misc.imsave(directory + '/' + f_split[4], img_res)

				except:

					f_split = f.split('/')

					directory = './DATASET_weird/' + f_split[2]
					if not os.path.exists(directory):
						os.makedirs(directory)

					directory = directory + '/' + f_split[3]
					if not os.path.exists(directory):
						os.makedirs(directory)


					print("IMAGE " + f + " WEIRD")

				
				






