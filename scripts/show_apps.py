# Import the otbApplication module. This python module provides access to OTB applications
import otbApplication

# otbApplication.Registry shows available applications
print "Available applications: "
print str( otbApplication.Registry.GetAvailableApplications() )


