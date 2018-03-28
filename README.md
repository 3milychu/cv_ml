# Computer and Machine Learning Templates

Included in this repo are go-to templates I've created to work with computer vision and machine learning models.

###api-to-csv.ipynb
This python script can iterate through json objects, building needed api urls and taking the data values you want to work with. This is helpful for instance, if you have a list of object IDs that need to be appended to a base api URL in order to scrape the needed information. 

###opencv
This subdirectory includes scripts working with opencv, an open computer vision library. Examples of usage include identifying image foreground and background to extract foreground and place on transparent background. Helpful when working with large sets of images for image processing in image training sets (for machine learning models) or for data visualization (dynamically retrieving and displaying transformed images in apps)

###algorithmia
This subdirectory includes scripts working with Algorighmia, a machine learning and computer vision resource. You can call APIs that processes inputs and send outputs to your data://algo directory
