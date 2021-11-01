---
tutorial:
date: {{date}}
tags: tag1, tag2, etc
---

# what I was trying to do

+ Using PixPlot to analyze photos of 19th century fashion from [Met collections](https://www.metmuseum.org/art/collection/search) to see if it can identify trends amongst Victorian dresses

+ link to PixPlot output: `[19th Century Dresses of the Western World](https://chantalmb.github.io/pixplot-viz/)`

## how it might connect to other research I'm doing
+ Would like to see if PixPlot could somehow be used to successsfully cluster images thematically

## what I did
+ Based on the results in my [[img-classifier-log]] indicating thaat the classifier possibly picked up more on how fashion was influenced by other nations rather identifying distinct style for each nation, I wonder what patterns of similarity PixPlot might find? --> will this unintentionally cluster the images by decade based on current style? Reveal how trends circulated between France, UK, and US?
	+ Going to lump all images into one big folder to use
+ Installed and ran `pixplot` package with no error
	+ Process took a good 35mins --> could this be accelerated using GPU?
+ Results: I got too excited and made the classic mistake of overestimating a computer's intelligence
	+ Why did I assume the computer would first try to cluster by style rather than by the easiest category, colour?
	+ The hotspot clusters seem to mostly focus on instances where there are multiple shots of one dress
		+ Only one hotspot cluster notes a group of dresses with shared stylistic features --> heavy cape-like watteau-style trains
	+ When looking at clusters macroscopically via the dimensionality reduction viewer, there are larger clusters that were not noted as hotspots --> these actually do group by silhouette!
		+ These images do reference the dresses' profile, but there are a diverse number of dress profiles and the grouping isn't relying on metrics as simple as just "left facing side profile"

## challenges 
+ PixPlot documentation is a bit unclear/confusing
	+ After making a plain default python environment with `conda`, the instructions are:
		```
		pip uninstall pixplot
		pip install https://github.com/yaledhlab/pix-plot/archive/master.zip
		```
		+ Why am I being told to uninstall something I have yet to install? --> I assume this is a typo and these are meant to be two `pixplot` installation options, but for someone just starting out this could be a point of confusion
	+ I was wondering if thiss process could be sped up via GPU acceleration --> [issue was raised about this](https://github.com/YaleDHLab/pix-plot/issues/241) a month ago
		+ Response indicates that there is info about CUDA acceleration in the project `README` but in reality there is nothing discussing this --> forgot to update file?
	
## thoughts on where to go next
+ Would like to try this with duplicate images removed to see how the hotspots would change --> currently, many of the hotspots are just a handful of one or two photos (that are the same shot, just with different lighting)
	+ But then there's the question of which photo do we keep/which photo most truthfully represents the item being studied?
+ Would PixPlot group more by aesthetic if all photos were made b&w?
+ Wish the Met API offered a straightfoward way to get metadata for image sets --> this would be so much more informative if I could add the image metadata so I could analyze the image clusters with more background information 