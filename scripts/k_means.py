# This script takes an image file as input and conducts an unsupervised k-means clustering. 
# Needs 2 arguments. 
#   argument 1: input image file
#   argument 2: number of classes


# Import sys.argv to enable command line arguments for setting parameters in the script
from sys import argv


# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication


# create the application with codename "kmeans"
kmeans = otbApplication.Registry.CreateApplication("KMeansClassification")

#set parameters

kmeans.SetParameterString("in", argv[1])
kmeans.SetParameterInt("nc", int(argv[2]))
#[:-4] is used to subset string of the input file name excluding the file ending (last 4 letters) specified with the first argument
kmeans.SetParameterString("out", argv[1][:-4]+ "_kmeans" + ".tif")


kmeans.ExecuteAndWriteOutput()

print("Finished")




