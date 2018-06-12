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
		Show an image with a rectangle draw that encloses the face
	Args:
		image: A loaded image 
		faces: 1D array list with four entries that specifies the bounding box of the detected face
	"""
	fig, ax = plt.subplots(1)
	ax.imshow(image)
	for (x, y, w, h) in faces:
		ax.add_patch(patches.Rectangle((x, y), w, h, color='red', fill=False))
	plt.show()

def image_selected(event, figure):
	"""
		Display on terminal the name of the image which was "clicked"
	Arg:
		figure: The matplot figure object created on PlotGridImages function
	"""
	axlist = figure.axes
	for i in range(len(axlist)):
		if axlist[i] == event.inaxes:
			print(img_list[i])

def plot_grid(figures, nrows = 1, ncols=1, fullsize=False):
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

    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.02)
    fig.canvas.mpl_connect("button_press_event", lambda event: image_selected(event, fig))
    if fullsize:
    	mng = plt.get_current_fig_manager()
    	mng.resize(*mng.window.maxsize())
    plt.show()


def detect_face(image):
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

def delete_erroneous_image(image):
	"""
		Delete an image from your data directory 
	Args: 
		image: image path
	"""
	os.remove(image)

def get_set_images(dirname, imgtype, nimages):
	"""
	Create a grid of nimages and a list with their names. 
	Args:
		dirname: dir path where the images are 
		imgtype: image type e.g png, jpg, jpeg. }
		nimages: number of images 

	"""
	images = glob.glob(dirname + '/*.' + imgtype)
	grid = {}

	if len(images) < nimages:
		print("There are not enough images, only: ", len(images), " are available.")
		exit()

	for i in range(nimages):
		image = images[i]
		#if detect_face(image):
		img = cv2.imread(image)
		try:
			grid[image] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		except:
			delete_erroneous_image(image)
	return images[:nimages], grid

img_list, grid = get_set_images(dirname='./data', imgtype='jpg', nimages=72)
plot_grid(grid, 10, 10, True)
