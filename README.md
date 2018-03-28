# Computer and Machine Learning Templates

Included in this repo are go-to templates I've created to work with computer vision and machine learning models.

## api-to-csv.py
This python script can iterate through json objects, building needed api urls and taking the data values you want to work with. This is helpful for instance, if you have a list of object IDs that need to be appended to a base api URL in order to scrape the needed information. 

## opencv
This subdirectory includes scripts working with opencv, an open computer vision library. Examples of usage include identifying image foreground and background to extract foreground and place on transparent background. Helpful when working with large sets of images for image processing in image training sets (for machine learning models) or for data visualization (dynamically retrieving and displaying transformed images in apps)

## algorithmia
This subdirectory includes scripts working with Algorighmia, a machine learning and computer vision resource. You can call APIs that processes inputs and send outputs to your data://algo directory

## scikit-image
This subdirectory includes scripts working with scikit-image image processing techniques, i.e. edge detection. This is helpful for example, in starting to create a training set of images for object identification.

## scikit-learn
This subdirectory includes scripts working with scikit-learn basic functions to explore a dataset and run fits using basic models such as linear, logistic regression and stochastic gradient descent.

## concepts
This subdirectory includes concepts for building machine learning models for health and lifestyle applications.
