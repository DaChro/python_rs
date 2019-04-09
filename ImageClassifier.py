# This script takes an input image and a model file (created by the TrainSVMClassifier) and conduct classification on the image


# Import sys.argv to retrieve arguments from the command line for setting parameters in the script
from sys import argv

# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication

# Create an instance of the OTBApplication, here the ImageClassifier application
ImageClassifier = otbApplication.Registry.CreateApplication("ImageClassifier")

# Set the parameters of the application:

#Input image 
ImageClassifier.SetParameterString("in", argv[1])


#Model file to be used during classification (output of TrainSVMClassifier)
ImageClassifier.SetParameterString("model", "model.txt")

#the output file name consists of the input file name and "_NDVIDiff"
#[:-4] is used to subset string of the input file name excluding the file ending (last 4 letters) specified with the first argument
ImageClassifier.SetParameterString("out", argv[1][:-4] + "SVM.tif")

# Execute the application and write the output to current folder
ImageClassifier.ExecuteAndWriteOutput()

print "Finished"

