import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2

def show_image(image, faces):
	"""
		Show an image with a face rectangle
	Args:
		image: Image
		faces: a set of x,y,w,h positions for each face detected
	"""
	fig, ax = plt.subplots(1)
	ax.imshow(image)
	for (x, y, w, h) in faces:
		ax.add_patch(patches.Rectangle((x, y), w, h, color='red', fill=False))
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

# The only two valid images must be the 1 and 2. 
for i in range(4):
	print(containsFace('data/' + str(i+1) + '.jpg'))



