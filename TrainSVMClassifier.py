#This script takes an image file and a shapefile (containing training data) as input and trains a classifier for supervised classification
#Here, the SVM classifier is used.


# Import sys.argv to retrieve arguments from the command line for setting parameters in the script
from sys import argv

# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication

# Create an instance of the OTBApplication, here the TrainImagesClassifier application
TrainImagesClassifier = otbApplication.Registry.CreateApplication("TrainImagesClassifier")


# Set the application parameters:

#List of input images
TrainImagesClassifier.SetParameterStringList("io.il", [argv[1]])

#Input Shapefile containing the training data
TrainImagesClassifier.SetParameterStringList("io.vd", [argv[2]])

#Name of the field that contains the class identifier (this identifier should be a positive integer)
TrainImagesClassifier.SetParameterString("sample.vfn", argv[3])

#Training method, here SVM
TrainImagesClassifier.SetParameterString("classifier", "libsvm")

#Output model file to be used during classification
TrainImagesClassifier.SetParameterString("io.out", "model.txt")



# Execute the application and write the output to current folder
TrainImagesClassifier.ExecuteAndWriteOutput()

print "Finished"


