---
tutorial: Build an Image Classifier
date: {{10-19-2021}}
tags: images, tutorial, image classification
---

# what I was trying to do

+ Train image classsifier on actual photos of historical fashion from [Met collections](https://www.metmuseum.org/art/collection/search), then see if the classifier can correctly identify fashion plates

## how it might connect to other research I'm doing
+ I wonder if an image classifier could be used to sort large image-based datasets
	+ Or perhaps, I wonder if *how* the computer classifies things could point to new observations about the data

## what I did
+ Grabbing Victorians dresses from the UK, US, and France
	+ [Using Met collections API](https://metmuseum.github.io/)
		+ Query: `https://collectionapi.metmuseum.org/public/collection/v1/search?dateBegin=1830&dateEnd=1900&hasImages=true&departmentId=8&geoLocation=United%20Kingdom&q=dress`
			+ Swap out geolocation for each country
		+ Write Python script to grab full metadata for each object using `objectIDs`
			+ For each object grab the URLs found under `primaryImage` and `additionalImages` --> write each URL to txt file
		+ Run `wget` command on each outputted text file to get the images
			+ `wget -w 2 -i uk-dress-objects.json-img.txt`
			+ God this is a lot of pics this classifier better be super smart
+ Find fashion plates from each place to test with
	+ Will use fashion plates from late Victorian era (1880s+) to "even" the playing field
	+ Less direct than finding actual pictures for training data --> Met seems to only have French fashion plates digitized
		+ [US img src](https://digitalcollections.nypl.org/items/736152f0-f05a-0133-4223-00505686a51c#/?uuid=90dab250-f05a-0133-1f05-00505686a51c)
		+ [France img src](https://libmma.contentdm.oclc.org/digital/collection/p15324coll12/id/9217/rec/31)
		+ [UK img src](http://dbooks.bodleian.ox.ac.uk/books/PDFs/555043805.pdf) --> shockingly difficult to find, probably because of how much the UK referenced France for fashion
+ FIRST RUN:
	+ Results
		+ France fashion plate was IDed as being from US
		+  US fashion plate was IDed as being from UK
		+  UK fashion plate was IDed as being from UK!
+   SECOND RUN: Realized I never checked the ratio of images in each training folder --> if one has more than the others, results may be skewed, 
	+  Now going to balance training data and retrain with equal number of images
	+  UK folder has fewest images at 461 --> figure out command to randomly delete files in each folder until there is only 450
		+ Command used to do this: `find /Users/homebase/Desktop/HIST5706/week-5-6/image-classifier/image-classifier/tf_files/gallery/us-mod -type f | sort -R | tail -n +451 | xargs rm`
		+ Threw errors when it came across files that had spaces in their name but there wasn't enough to make a signifcant impact on dataset so I'm leaving it
	+ Results:
		+ France fashion plate was IDed as being from US but a little bit UK
		+  US fashion plate was IDed as being from UK but a little bit US!
		+  UK fashion plate was IDed as being from UK!
+ ULTIMATELY: Results inaccurate but I think the way this image classifier classifies can still point us to ideas about influence
	+ France was the fashion centre of the world in 19th century so it makes sense that French fashion was IDed by the computer as being from the US and UK --> both cultures heavily referenced France when developing fashion trends
	+ US fashion was most influenced by UK --> the upper-middle class in US were typically either from the UK or of UK ancestry
	+ When trying to find UK fashion plate, I noted that the UK tended to have the most distinct manner of daily dress in the 1880s-90s despite influence from France, thus it being the only fashion plate correctly IDed checks out

## challenges 
+ Met API does not consistently return a valid JSON object
	+ Fixed using Flask method `flask.jsonify([text/html obj])` 
		+ Seems to randomly glitch out sometimes and stop working (throws `NameError` or `RuntimeError`) --> fix was creating a new conda environment and reinstalling the library
+ So many institutions use [whatever this platform is](https://libmma.contentdm.oclc.org/digital/collection/p15324coll12/search) to host their digital archives
	+ No ability to refine searches by place/time period
	+ Actual search bar only looks for 100% matches
	
## thoughts on where to go next
+ Would be interesting to see if you could train the classifier to identify fashion at a decade-level along with location 
	+ Victorian era fashion was very changeable so perhaps this would result in more accurate identification