"""
In this script, we first simulated an image of the sky by adding a number of
Gaussian stars. Then we look for the brightest star in the field and extract
the measured flux. We compare the measured flux as a function of aperture size.
"""
import matplotlib.pyplot as plt
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG) # Default level is WARNING

#-- input parameters ----------------------------------------------------------
np.random.seed(1000)
image_size = 1000,1200
number_of_stars = 50
bias = 100.
noise = 1.
#------------------------------------------------------------------------------

def star_image(image_coords, star_coords, sigma=1.0, peak_brightness=1.0):
    """
    Definition of the Gaussian PSF of a star. 
    """
    X,Y = image_coords
    star_x,star_y = star_coords
    starshape = peak_brightness * np.exp( -0.5*((X-star_x)**2 + (Y-star_y)**2) / sigma**2)
    logging.info(f"Added star at {star_coords} (sigma={sigma:.2f}, peak={peak_brightness:.2f})")
    return starshape


#--------------- GENERATE SIMULATED IMAGE -------------------------------------

#-- start with a bias image
image = bias*np.ones(image_size)
#-- create a coordinate grid of the image to easily compute distances etc.
X,Y = np.mgrid[0:image_size[0]:1,0:image_size[1]:1]
#-- create a set of random parameters to characterize the input stars.
#   This table consists of 'number_of_star' rows and 4 columns:
#       Column 1: X coordinate of star
#       Column 2: Y coordinate of star
#       Column 3: width of star
#       Column 4: star brightness
stars = np.random.uniform(low=np.array([0,0,5.2,5]),
                          high=np.array([image_size[0],image_size[1],5.5,100]),
                          size=(number_of_stars,4))
#-- See where the brightest star is located and what its total flux is.
brightest_star_input = np.argmax(stars[:,-1])
predicted_flux = 2*np.pi*stars[brightest_star_input,-2]**2*stars[brightest_star_input,-1]

#-- now add all the input stars to the image
for star in stars:
    image += star_image((X,Y),star[:2],sigma=star[2],peak_brightness=star[3])

#-- and add some random noise the image
image += np.random.normal(size=image.shape,scale=noise)
#------------------------------------------------------------------------------

#--------------- EXTRACT BRIGHTEST STAR FROM SIMULATED IMAGE ------------------

#-- first determine the bias
bias_meas = np.median(np.ravel(image))

#-- get the location of the brightest star
Xc,Yc = np.unravel_index(image.argmax(),image.shape)
logging.info (f"Location of brightest star: {Xc}, {Yc}")

#-- determine the distance from each pixel to the brightest star: we want to 
#   sum up all flux inside a region around the brightest stars (an aperture).
#   We will use different aperture sizes to see how the measured flux is
#   dependent on it
distance = np.sqrt( (X-Xc)**2 + (Y-Yc)**2)
apertures = np.linspace(0.5,5,10)*stars[:,-2].mean()

#-- prepare an array to collect the measured fluxes as a function of aperture
measured_fluxes = np.zeros_like(apertures)

#-- now sum up the flux inside each aperture. Therefore, copy the original
#   image into a new array, and set all the flux outside the aperture to zero.
#   Then, subtract the bias and sum the whole
for i,aperture in enumerate(apertures):
    brightest_star = distance<=aperture
    extracted = image+0.
    extracted[~brightest_star] = 0
    extracted[brightest_star] -= bias_meas
    measured_fluxes[i] = extracted.sum()
    logging.info(f"Aperture {aperture}: flux = {measured_fluxes[i]} (real = {predicted_flux}")

#------------------------------------------------------------------------------
#-- make a plot of the measured/predicted fluxes
plt.figure()
plt.plot(apertures,measured_fluxes,'ko-')
plt.plot(apertures,np.ones_like(apertures)*predicted_flux,'r-')

#-- make a plot of the image itself and the extracted region
plt.figure()
plt.imshow(image,cmap=plt.cm.hot)
plt.plot(Yc,Xc,'gx',ms=20,mew=2)
plt.colorbar()
plt.xlim(0,image_size[1])
plt.ylim(0,image_size[0])

plt.figure()
#-- don't plot the flux outside the extracted region
extracted[~brightest_star] = np.nan
plt.imshow(extracted,cmap=plt.cm.hot)
plt.colorbar()
plt.xlim(0,image_size[1])
plt.ylim(0,image_size[0])
plt.show()
