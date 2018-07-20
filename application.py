import json
import os
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from AxonDeepSeg.testing.segmentation_scoring import *
from time import time

from scipy.misc import imread, imsave

from AxonDeepSeg.apply_model import axon_segmentation

"""
data is a dictionary:
{
	'path_testing': (str)the path to the folder that contains both the file name and the
	'model': (str) either SVM or TEM
	'image_name'=  (str) the name of the string
}
"""

def run(data):
	path_testing = data.get('path_testing')

	if data.get('model') == 'SVM':
		model_name = 'default_SEM_model_v1'
	else:
		model_name = 'default_TEM_model_v1'

	image_name = data.get('image_name')




	path_model  = os.path.join('./AxonDeepSeg/models',model_name)
	path_configfile = os.path.join(path_model,'config_network.json')

	if not os.path.exists(path_model):
	    os.makedirs(path_model)

	with open(path_configfile, 'r') as fd:
	    config_network = json.loads(fd.read())

	prediction = axon_segmentation(path_testing, image_name, path_model, config_network,verbosity_level=0)

	print("all done no errors")


def test_run():

	path_testing = './AxonDeepSeg/data_for_test/test_sem_image/image1_sem'
	model_name = 'SVM'
	image_name = '77.png'

	data = {'path_testing':path_testing, 'model_name': model_name, 'image_name': image_name}

	run(data)


if __name__ == '__main__':
	test_run()
	#run(data = {'path_testing':'/Users/celsloaner/Documents/forDLHUB/firstTrial/axon_myelin/data/test_sem_image/image2_sem', 'model_name': 'SVM', 'image_name': '103.png'})


