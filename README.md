# imagePreprocessing
Different helpful scripts that I used to preprocess and augment images to train CNN models. This scripts are designed to work with the following organization:

MAIN FOLDER --> SUBFOLDERS (EACH ONE FOR EACH MODEL THAT WE WANT TO TRAIN) --> SUBSUBFOLDERS (REPRESENTING EACH CLASS OF EACH MODEL)

## resizeDataset.py
This script transforms all the images in your MAIN FOLDER to the selected square dimensions without deformations. It preserves the aspect ratio of the images by adding pixels to the smallest dimension before resizing it. The resized images are strored in another folder called "DATASET_resized" which will have the same organization as the original one. It also creates another folder called "DATASET_weird" to take control of those images where the algorithm have problems.

## imaugment.py
This script is thought to work over resized images to make sure that each class has a minimum number of images. It generates images with different zoommings with the desired background color until arrive to the selected minimum number of images per class.
