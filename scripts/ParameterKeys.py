# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication

# otbApplication.Registry shows available applications
print("Available applications: ")
print(str( otbApplication.Registry.GetAvailableApplications() ))

# create the application with codename "BandMath"
BandMath = otbApplication.Registry.CreateApplication("BandMath")

#show available parameters
print("Available parameters: ")
print(BandMath.GetParametersKeys())




