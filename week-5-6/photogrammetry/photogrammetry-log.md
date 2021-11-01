---
tutorial:
date: {{date}}
tags: tag1, tag2, etc
---

# what I was trying to do
+ Create a model of an object in my house
+ [Link to best model](https://skfb.ly/oqyMU)

## how it might connect to other research I'm doing
+ How can the presence of something in a form more tangible than photos affect impact?
+ Ethics of preservation --> how can material history be taught without negative impact on the culture it derives from and on the object itself?

## what I did
- Object chosen for this: Vintage Bernina sewing machine
	- Closest thing I have to an artifact in my home
- PHOTO SET #1: Just regular lighting and DSLR
	-  Used me olde Canon EOS 20D for taking pictures to hopefully get less motion blur then my phone camera --> if it doesn't work out... I wonder if there's an app for this? 
		- Took photos in office/craft room thinking I could just upload the pictures to my PC as I went and also avoid injuring myself via having to haul my hunk-of-metal sewing machine somewhere else in the house
			- LEARNING MOMENT: There is not EOS Utility for Linux computers --> you have to basically hack your camera using `gphoto2`
	- Image processing
		- Removed the occasionally blurry pic but kept everything that was in focus
		- Depth of field may be issue --> used macro lense...
	- Meshing
		- Wow the final model looks like my sewing machine is melted??? --> Nightmare realm version of my office yikes
		- No errors with images
		- I think the appearence might be the result of my machine being shiny --> reduce shine?
- PHOTO SET #2: Controlled lighting, a lazy susan, and DSLR
	- This time using a lazy susan so I don't have to try and do an obstacle course to take pics around my office --> covered lazy susan in various fabrics so Meshroom can hopefully use this as a reference to indicate my object is indeed rotating (insteada of using background like it did previously)
	- Camera on tripod --> adjusting depth of field means longer shutter speed
	- Waited til dark and diffused light of lamp with light-weight white curtain 
	-  Image processing
		- Removed the occasionally blurry pic but kept everything that was in focus
			- Much fewer blurry pics and more consistent angles thanks to tripod
		- Very oranged toned thanks to my lamp but hopefully this won't affect anything
	- Meshing
		- My Lazy Susan Method has failed me --> despite various fabrics, the only side of the model sufficiently constructed was the one which the camera was facing
		- Controlled lighting didn't seem to change the meltiness despite dulling the shine...
- PHOTO SET #3: Dots, and my phone camera!
	- Testing how my phone does for this just for funsies
		- First photoset done with regular lighting just like how I did the first photoset to compare
		- Second photoset I add various small doodles to sewing machine body to see if I can offset the shine --> used whiteboard marker and waited for doodles to dry matte
	-  Image processing
		- Removed the occasionally blurry pic but kept everything that was in focus
			- Phone did result in more motion blur
		- Phone camera worse at correcting/lightening shadows --> brighter reflective surfaces and darker shadows
		- Doodles are visible even in reflection --> hopefully less melting?
	- Meshing
		- Both models still pretty melty :(
		- Where the phone camera really caught a reflection at the base of my machine resulted in an actual void in the final models --> forgot to add doodle there oops
		- I think the doodled machine photos did create a bit more of a fleshed out model where the doodles are present? 
	
## challenges 
- Getting Meshroom to work
	- Running in Colab --> 5th try: my runtime session keeps ending before Meshroom finishes the DepthMap step :'(
		- Will try running on Kaggle --> Kaggle has some weird GPU/CPU set up that's throwing an error when attempting to run Meshroom 
	- Downloading GUI app on Desktop (Pop!_OS)
		- Worried my GPU may cause issue (8gb of RAM recommended but I only have 6gb)
		- Downloaded no problem --> dragging and dropping images also seems to not cause issue
		- GUI is a win! --> images and metadata all successfully processed, just got to DepthMap with no issues
## thoughts on where to go next
- I came into this activity with an interest in using photogrammetry as a method of "preserving" objects in a digital space --> after performing this myself for just one object, I wonder how possible this is due to resources and even modifications to the item required
- Many items in museum collections are just as shiny as my sewing machine
	- Adding dots was somewhat effective at mitigating this, but the ideal to create models of shiny objects is chalk dusting --> there is a lack of destructive ways to photograph artifacts for photogrammetric purposes
- The act of just taking the photographs was quite time consuming and intensive even with the recommend type of camera and a tripod --> there is technology specifically designed for photogrammetry, but it costs a significant amount of money and also has a time cost associated with it as one has to learn the required skills needed to use this equipment
	- What archives and museums have the time and/or monetary resources to use photogrammetry practically? 
	- If a museum did choose to use photogrammetry to preserve certain objects, does this create an unintentional (or intentional...) hierarchy with in that archive, placing the items selected to be preserved in this manner at a higher value then the rest of the collection?
	- Have any museums or archives tried this? I'd be interested in finding out how it went/how it's going