#This is an editeded implementation AxonDeepSeg

Original Link: https://github.com/neuropoly/axondeepseg/tree/5078fc9019520f619fb75f62c863faab19239af5
Docs: http://axondeepseg.readthedocs.io/en/stable/documentation.html#

Input:
data is a dictionary:
{
	'path_testing': (str)the path to the folder that contains both the file name and the
	'model': (str) either SVM or TEM
	'image_name'=  (str) the name of the string
}

Output:
Saves three new images in same location as path_testing
---image_name_seg-axonmyelin.png---
---image_name_seg-axon.png---
---image_name_seg-myelin.png---