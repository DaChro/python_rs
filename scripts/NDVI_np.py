from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np


input_path = 'C:\\Python_in_GIS\\RS-Session\\input.tif'
output_path = 'C:\\Python_in_GIS\\RS-Session\\ndvi.tif'
dataSource = gdal.Open(input_path, GA_ReadOnly)


#print some information about the image, e.g. projection:
print(dataSource.GetProjection())



# read layers 3 and 4 into numpy arrays
visred = dataSource.GetRasterBand(3).ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)
nir = dataSource.GetRasterBand(4).ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

#print the type of the object
print('this is an' ,type(visred).__name__)

# Write the expression to compute ndvi
# make sure the data is interpretated as float, so that the output is also float 
# -> NDVI values range only between -1 and +1
ndvi = (nir.astype(float)-visred.astype(float))/(nir.astype(float)+visred.astype(float))


#Write the result to disk using gdal (this should be similar to what you have already learned)
driver = gdal.GetDriverByName('GTiff')
outDataSet=driver.Create(output_path, dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
outBand = outDataSet.GetRasterBand(1)
outBand.WriteArray(ndvi,0,0)


# set the projection and extent information of the dataset (this should be similar to what you have already learned)
# we simply use the spatial reference info of the input file 
outDataSet.SetProjection(dataSource.GetProjection())
outDataSet.SetGeoTransform(dataSource.GetGeoTransform())

# Save file to disk / release from memory
outBand.FlushCache()
outDataSet.FlushCache()

