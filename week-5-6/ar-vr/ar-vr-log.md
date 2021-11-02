---
tutorial:
date: {{date}}
tags: tag1, tag2, etc
---

# what I was trying to do

Use AR to project my sewing machine model into a tangible space using AR.js

+ [Link to demo](https://chantalmb.github.io/ar-demo/)

## what I did
+ Downloaded model from my sketchfab account
	+ Creating repo with model files and index to be published via github pages
+ Location-based AR
	+ Model won't load... are my coordinates not specific enough?
	+ Reseting coordinates to nearby park to force myself to go on a walk for ~research~ purposes
		+ Still not loading --> going to try marker-based AR instead, less variable than location
+ Marker-based AR
	+ Trying example from AR.js docs --> `a-sphere` appears but `a-entity` does not...
	+ Model appears if I use link! --> serving link to my own model on github using [githack](https://raw.githack.com/)
+ Very neat and easy library to use --> process of creating models is difficult, but this library makes sharing them simple

## challenges 
+ Model will not load using location-based AR
	+ Example model is not showing up either
	+ Honestly there's only so many locations I can go --> going to try marker-based AR so I 100% know where the model should appear
+ Model will not load using marker-based AR
	+ First thing as always, empty Chrome's cache --> still not showing
	+ If I use the link to a model provided in the example a model appears --> if I link to my model (local directory) it does not appear
		+ Could be something wrong with my model so what if I download a copy of the example model and set the local path to that? --> Nope, doesn't work with example model
	+ What if I link to my own model through it's presence as an upload on github? 
		+ Examples use rawgit but that's been depreciated since 2018? --> gitbreak seems to be current alternative
		+ Model appears! but tiny --> scaling up (count: 5x)
	+ Local models might not have appeared due to CORS error? --> can't verify that my model is secure somehow??

## thoughts on where to go next
+  Imagine using this for heritage buildings/house --> Enter somewhere like a heritage house, open webpage on mobile device, and situate the artifacts otherwise on display elsewhere in a museum or glass case in another room in the place where they originally would be in that home (aka make the house look "lived in" by combining photogrammetry and AR)
	+  Marker-based AR would probably be easiest for this, but would the markers detract from the "authenticity" of the experience? --> could markers be something like specific features found on piece of furniture where modelled artifact could be placed?
	+  I need a heritage building to try this in...