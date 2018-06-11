import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import cv2
import os 
import glob

""" 
	Program to create a dataset for a hairstayle image-to-image translation task
"""

def show_face_detection(image, faces):
	"""
		Show an image with a rectangle draw that ecloses the face
	Args:
		image: Image
		faces: a set of x,y,w,h positions for each face detected
	"""
	fig, ax = plt.subplots(1)
	ax.imshow(image)
	for (x, y, w, h) in faces:
		ax.add_patch(patches.Rectangle((x, y), w, h, color='red', fill=False))
	plt.show()

def imageSelected(event, figure):
	"""
		Display on terminal the name of the image which was "clicked"
	Arg:
		figure: The matplot figure object created on PlotGridImages function
	"""
	axlist = figure.axes
	i = 0
	for element in axlist:
		if element == event.inaxes:
			print(img_list_test[i])
		i += 1

def plotGridImages(figures, nrows = 1, ncols=1):
    """
    	Plot a dictionary of figures.

    Args:
    	figures : <title, figure> dictionary
    	ncols : number of columns of subplots wanted in the display
    	nrows : number of rows of subplots wanted in the figure
    """
    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows)
    for ind, title in zip(range(len(figures)), figures):
    	axeslist.ravel()[ind].imshow(figures[title])
    	axeslist.ravel()[ind].set_axis_off() 

    fig.subplots_adjust(wspace=0, top=1., bottom=0, left=0, right=1)
    fig.canvas.mpl_connect("button_press_event", lambda event: imageSelected(event, fig))
    plt.show()


def containsFace(image):
	"""
		Check for valid images, that is, images that contain only one detectable face.
	Args: 
		image: Image path
	"""
	img = cv2.imread(image)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	face_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(gray, 2)
	#print('Number of faces detected:', len(faces))
	show_image(img, faces)
	return len(faces) == 1

def pruneErronousImage(image):
	"""
		Delete a iamge file  
	Args: 
		image: image path
	"""
	os.remove(image)


dirname = './data'
filetype = 'jpg'

images = glob.glob(dirname + '/*.' + filetype)

grid = {}
img_list_test = []
i = 0
for image in images:
	img = cv2.imread(image)
	grid[image] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img_list_test.append(image)
	i += 1

plotGridImages(grid, 6, 7)
