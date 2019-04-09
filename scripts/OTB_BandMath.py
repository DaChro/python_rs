#  Example for BandMath creating an NDVI
#  Assumes the input image to have NIR in Band 4 and Red in Band 3
#  command to run: Python BandMath.py inputimagename.tif

# use sys.argv to retrieve arguments from the command line.
from sys import argv


# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication


# create the application with codename "BandMath"
BandMath = otbApplication.Registry.CreateApplication("BandMath")


# set input image list
BandMath.SetParameterStringList("il", [argv[1]])

#set output file 
#[:-4] is used to subset string of the input file name excluding the file ending (last 4 letters) specified with the first argument
BandMath.SetParameterString("out", argv[1][:-4] + "_NDVI" + ".tif")

#define expression, here NDVI
BandMath.SetParameterString("exp", "(im1b4 - im1b3) / (im1b4 + im1b3)")


# Execute the application and write the output to current folder
BandMath.ExecuteAndWriteOutput()

print("Finished")