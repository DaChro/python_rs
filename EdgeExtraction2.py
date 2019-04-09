# This script takes an image file as input and computes an edge extraction on it. Three algorithms are available: gradient, sobel & touzi.
# Needs at least 2 arguments. 
#   argument 1: input image file
#   argument 2: filter to be used
#When using the touzi algorithm, the radius in x and y need to be specified in a third argument (integer).

# Example command 1: Python EdgeExtraction.py inputimage.tif sobel
# Example command 2: Python EdgeExtraction.py inputimage.tif touzi 5 


# Import sys.argv to enable command line arguments for setting parameters in the script
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
#if the touzi filter is used, the filter radius is set using the third command line argument
#this argument is also appended to the output file name
if argv[2] == "touzi":
	EdgeExtraction.SetParameterInt("filter.touzi.xradius", int(argv[3]))
	EdgeExtraction.SetParameterInt("filter.touzi.yradius", int(argv[3]))
	EdgeExtraction.SetParameterString("out", argv[1][:-4] + "_" + argv[2] + argv[3] + ".tif")
else:
	EdgeExtraction.SetParameterString("out", argv[1][:-4] + "_" + argv[2] + ".tif")

	
# Execute the application and write the output to current folder
EdgeExtraction.ExecuteAndWriteOutput()

print "Finished"