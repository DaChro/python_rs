# This script takes an image file as input and computes an edge extraction on it. Three algorithms are available: gradient, sobel & touzi.
# Needs 2 arguments. 
#   argument 1: input image file
#   argument 2: filter to be used



# Import sys.argv to retrieve arguments from the command line for setting parameters in the script
from sys import argv

# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication


# Create an instance of the OTBApplication, here the EdgeExtraction
EdgeExtraction = otbApplication.Registry.CreateApplication("EdgeExtraction")


# Set the parameters of the application:

#input image
EdgeExtraction.SetParameterString("in", argv[1])

#filter for edge extraction
EdgeExtraction.SetParameterString("filter", argv[2])

#band of the input image to be used in the edge extraction
EdgeExtraction.SetParameterInt("channel", 1)


#the output file name consists of the input file name and the name of the applied filter
#[:-4] is used to subset string of the input file name excluding the file ending (last 4 letters) specified with the first argument
EdgeExtraction.SetParameterString("out", argv[1][:-4] + "_" + argv[2] + ".tif")

	
# Execute the application and write the output to current folder
EdgeExtraction.ExecuteAndWriteOutput()

print("Finished")

