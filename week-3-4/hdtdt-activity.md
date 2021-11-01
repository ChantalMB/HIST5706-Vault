# How Did They Do That?

**Selected review**: https://reviewsindh.pubpub.org/pub/distant-viewing-toolkit/release/1

## Conssiderations
- Where are the holes in your knowledge?
- What a priori knowledge seems necessary in order to have made/built/understood the thing being reviewed?
- Pay attention to how the review is constructed. What elements do the reviewers focus on?

## Relevant Notes
-  The toolkit applies state-of-the-art computer vision algorithms to digitized collections of still and moving images in order to automatically create structured data. Features represented in the structured data include dominant colors found in the images, cut-detection, object detection and recognition, face detection and recognition, and image embeddings.
- "distant viewing,” the concept that the challenges of a computational analysis of large visual corpora can be understood in terms of visual semiotics and communication theory
-  In conversation with critical work on computer vision, the toolkit provides access to and control over how and what a user decides to view through computer vision algorithms.
- While the title of the tool might imply objectivity, DVT actually asserts that all visual content and the technologies that are used to produce and analyze them are socially and culturally constructed
- While DVT provides technical tutorials and an API to users in addition to the Github repository, future developments for the project might consider broadening its appeal to teachers.

Happy Turkey Day Eve all 🦃

The project review I decided to check out this week was written by Patrick Sui on the Distant Viewing Toolkit (DVT) library for Python: https://reviewsindh.pubpub.org/pub/distant-viewing-toolkit/release/1

The purpose of this project is to "facilitate the computational analysis of visual culture" (eg film and/or photography archives when discussed in the context of digital humanities) through the development of a Python library intended to simplify the often more complex task of implementing the algorithms required to use computer vision and machine learning methodologies. It allows for users to input their visual corpora then detect and recognize faces, detect and recognize specified objects, find dominant colour patterns and more! Although the review primarily focused on explaining the technical features and contexts of this project, when discussing the humanistic context of DVT Sui honed in on its applications for "distant viewing"-- how, through the generation of structured data that these digital techniques output, these massive copora of images can be translated into more digestible groupings of broader representations that may hold significance to the research being conducted.

I honestly chose this article because I'm interested in doing more with computer vision, and since I've already played around with computer vision methods a bit, I didn't feel while initially reading that there were any holes in my knowledge; but, upon doing a quick re-read of the review, due to the more technical approach taken I can see where there might be some confusion for someone new to ~the digital~ trying to understand what DVT does. Sui is, overall, pretty good at avoiding the assumption of prerequisite knowledge in his review, adding in a number of explanations for technical terms to make them more accessible for those without much experience in programming. Where I noticed this falter a little was when it came to explaining terms specifically related to computer vision; for example, when listing the primary features of DVT, he mentions things like "image embeddings" yet never provides further explanation about what this is and why it may be significant to the individual reading the review to learn more about this project. Further, Sui used the terms "high-level" and "low-level" in their computer science contexts a couple of times, and while he sort of contextualizes them so that one may assume their meaning, no direct explanation is provided. Ultimately though, this may just be a case of "know thy audience"-- those who choose to read this article based on its premise likely already have some skills in computational analytics and are reading to learn more, thus they would have the knowledge to extrapolate meaning from the terms they're unfamiliar with.

- pretty good at avoiding the assumption of prerequisite knowledge (explains all technical terms) which aligns with project mission --> BUT doesn't further explain features list in first paragraph (that I just realized are not common knowledge terms... I have been reading too many tech papers...) use terms "high-level" and "low-level" pretty frequently, but don't explain what this means
