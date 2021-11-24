---
task: Your Own Digital History
date: {{11-21-21}}
tags: tag1, tag2, etc
---

# Dev Log 2

## Objective
+ OF *COURSE* someone's already beat me to my project idea --> was lazy so I searched "nls chapbook open data" to take me to the repository webpage and instead the first result was [this](https://gitlab.com/vgg/nls-chapbooks-illustrations/) published only 4 months ago
	+ [Reading the paper](https://gitlab.com/vgg/nls-chapbooks-illustrations/-/blob/master/doc/dutta2021visual.pdf) --> not actually much of an actual analysis of the visual contents, but rather an analysis of how the visual content can be extracted
		+ Introduces very promisng tool for quick creation of image-based search engine from given corpus --> [VISE](https://www.robots.ox.ac.uk/~vgg/software/vise/)
		+ They train a pre-trained object detection model (EfficientDet) on ~300 annotated images
		  + Does achieve ~95% accuracy but I do wonder if this process could have been simplified with similar results by using a basic CV library like [ImageAI](https://github.com/OlafenwaMoses/ImageAI)?
			  + Honestly the creator gives [a simple guide on training an object detection model](https://medium.com/deepquestai/train-object-detection-ai-with-6-lines-of-code-6d087063f6ff) using his library... --> I am absolutely about to attempt this	
+ Paper's workflow for model training:
	+ Manually annotate 337 illustrations
	+ Train EfficientDet model
	+ From the results of this, manually review then annotate 1728 more illustrations
	+ Train EfficientDet model again
	+ Manually review these final results
+ Going to replicate their process, but simplified and more accessible
	+ Implement it via existing Python libraries designed for CV training --> easier to modify
	+ Going to use YOLOv3 as base model --> direct competitor for EfficientDet and tends to work better on smaller datasets 
	+ Images will be annotated using [LabelImg](https://github.com/tzutalin/labelImg) --> more common open source annotation tool with lots of available support

## Annotating data
+ Essentially all the tools used in the paper including the tool they used to annotate their images, LISA, are developed by University of Oxford's Visual Geometry Group --> shocking, it's almost like that paper was written by them or something
      + LISA only outputs annotations in Microsoft's [COCO](https://cocodataset.org/#home) format --> ImageAI asks for PASCAL VOC
  + LabelImg launches from command line like Jupyter Notebook with command `labelImg`
   + First have to copy all images into one folder to pull from
      + Initial command `cp "nls-data-chapbooks"/*/image/* all-pages` results in `bash: /usr/bin/cp: Argument list too long` --> too many files to do without iteration lol
		  + Using loop to go over each file like so works: `for pathname in "nls-data-chapbooks"/*/image/*; do cp "$pathname" all-pages; done`
    + The tutorial says you need min 200 annotations so I will start by trying the minimum --> if it really doesn't work w 200 imgs then I'll just run the paper's code to grab the imgs
    + Needed to install PyQt5 dev tools to launch LabelImg oop --> `sudo apt-get install pyqt5-dev-tools`
    + Clicking through all of these pics really makes you think about all the interesting things you could analyse from this kind of document
		+ Train a model to identify page ornamentations and pictures --> see if printers could be IDed based on ornamentation used and text/image placement
      	+ Train an image classifier with chapbooks of different years to automatically identify date of creation based on print styling  
      	+ There's so many instances of hand-written notes presumably form the person who owned the chapbook --> train model to detect pages with scribbles to analyze how people *literally* used cheap literature like this for purposes other than entertainment
      	+  If OCR was easier with these --> analyze word associations with images (esp the repeat/reused woodblocks)
    + Oop just put on an episode of *The X-Files* and went at it for the duration of the episode and now I have 203 annotated images --> just gonna keep the bonus 3
		+ Evident by this, LabelImg worked flawlessly

## Training model
+ Wrote a python script to generate list of needed file names from the xml output of annotations from LabelImg
	+ Moving annotated training data `for file in $(cat /home/cbrou/Desktop/YODH-project/data/train/annotations/xml_list.txt); do cp "$file" /home/cbrou/Desktop/YODH-project/data/train/annotations; done`
	+ Moving corresponding images: `for file in $(cat /home/cbrou/Desktop/YODH-project/data/train/images/img_list.txt); do cp "$file" /home/cbrou/Desktop/YODH-project/data/train/images; done`
	+ Moving annotated validation data: `for file in $(cat /home/cbrou/Desktop/YODH-project/data/validation/annotations/xml_list.txt); do cp "$file" /home/cbrou/Desktop/YODH-project/data/validation/annotations; done`
	+ Moving corresponding images: `for file in $(cat /home/cbrou/Desktop/YODH-project/data/validation/images/img_list.txt); do cp "$file" /home/cbrou/Desktop/YODH-project/data/validation/images; done`
+ Running the traing code works but seems to be underutilizing my GPU --> tensorflow not detecting GPU correctly?
	+ As typical, ImageAI recently got an "upgrade" to tensorflow 2.x and [now it's causing problems](https://github.com/OlafenwaMoses/ImageAI/issues/689)
	+ **FIX**: Literally just installing the version of ImageAI before 2.x compatability was added --> `pip install imageai==2.1.5`
		+ *Associated dependencies*:
		+ Conda environment created using Python 3.6
		+ `pip install tensorflow-gpu==1.15.3`
		+ `pip install cudatoolkit`
		+ `conda install -c conda-forge cudnn`

## Using model
+ Evaluation of the model --> in the final model produced there was a ~97%  accurate identification and a loss of only 1.8
	+ Seems kinda unrealistic but okay... --> evaluation of model isn't showing anything suspicious
+ Let's start by testing this model on just a couple of images
	+ Not predicting anything :( 
		+ Oh **nvm** the `minimum_percentage_probability` just had to be lowered from 50% to 5% --> this dictates how certain the model is that it's detecting the object it was trained to find
		+ Considering it was only trained using 200 images this lower percentage probability checks out 
	+ Tested w 3 pgs from training set and 3 pgs of just text
		+ Consistently detected all images!
		+ Did not detect any images on the text pages! 
+ Time to run this on alllll 47329 pages of this set --> **commentary from future self**: Did I forget in this moment that in the paper I'm referencing they ran this model on a different batch of images for each of their 3 step processing as oppose to running it on the whole dataset at once? yes. Would doing it like they did actually have made the process easier? not actually sure, they seem to have to sift through about the same amount of data I did in the end.
	+ Watching the output --> getting the exact same issues they described in the article where my model detects "phantom" images that show through on the pages after it bc of thin paper
		+ Bumping `minimum_percentage_probability` up to 10% fixes this but I'm paranoid that I'll somehow miss some of the very faded illustrations so I'll just divide the illustrated pages into a 'main' folder and then a separate folder for those with percentages < 10% for easy final clean up/review
	+ Division a good choice --> only took about 20mins to grab any stragglers from the "low probability" folder
		+ Caught faded images but ALSO a specific kind of "single person on cover page" image --> likely underrepresented in my small amount of training data
+ Going through the main folder, any "bleed through" from image flipside is still occasionally being detected as image when it is especially strong (like strong enough to where even I think it's the original printed side at first glance) --> also happens if multiple layers of text transfer to form a "blob"
+ Honestly? Just this first round of training has reduced the images to the point where it's realistic to manually clean over ~2hrs --> going to forgo 2nd round of training for now to give my poor computer a break
	+ If you REALLY wanted this process to be fully automated you could grab some illustrated pages that are now easily findable due to this round of training and annotate them, then retrain your model using a larger dataset for increased accuracy (aka "step 2" in the article's outlined process)
+ Properly manually reviewing the images...
	+ Keeping any page that has some form of graphical element that is not just a fancy line --> this seems to be the same criteria followed in the paper
	+ Oh neat 108500073.3.jpg has a fingerprint
	+ lol the hate message in 108556221.3.jpg
	+ 5978 --> 3735 --> 3744 (after fixing one of my "moving things" commands when sorting out the final images oops)
		+ Considering I just checked the paper and *oh my god they could have had to review almost 16000 images in their step 2* I think I got off pretty easy here geez
	+ After the final step outlined in the paper, upon manual review by a subject expert, they apparently finished with 3629 pages total
+ SO lets test their implementation to see what I kept vs what they didn't/see if I missed anything
	+ Really not universal nor clear install instructions for their illustration detector
		+ They also forgot to tell you to install `matplotlib`
	+ Okay so EfficientDet outputs the detected image but also *literally every single page even if it doesn't have a detection* --> how did they sort through this?? sounds like LISA perhaps has some type of sorting feature for annotations?
	+ Well that was a fun moment, just going to use their sqlite database for their VISE app to compare with my files I guess
  	+ Opening the database they used for VISE using [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) --> `SELECT filename FROM 'file_metadata'` to c/p list of their files into txt file
		+ Actually might build on to this db for my own work --> they obtained more metadata than just that available through the NLS website according to article
	+ There is apparently a difference of 27 pages between out datasets
		+  Oh interesting so these pages are all pages my model detected but I omitted upon manual review because... there's no images on these pages (same problem as usual-- seethrough pages and ink splotches/wear-and-tear) --> did they not do a final manual review outside of the subject expert?
	+  TO DO: Totally forgot to compare and see what I kept and they didn't --> DIY subject expert lol

## Thoughts on where to go next
+ Slap this all into a Colab notebook to make it accessible
+ Reallyyyyy tempted to train a model to detect handwriting so I can find all of the little notes and such hidden in these scans
+ Put current output into PixPlot and go from where the clustering algorithim takes me --> very curious to see how these images will be classified
	+ May want to run the most faded images through some sort of enhancement process first tho

