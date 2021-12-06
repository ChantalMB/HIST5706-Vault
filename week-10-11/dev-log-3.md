- Options to browse:
	- PixPlot clusters
	- By printer/publisher 
	- On a timeline
	- False detections that aren't just back-of-page transfers
	- Groupings of same images

- Making notebook
	- Everything installed alright
	- Will link my data as sample data --> okay but how do you download a folder from github?
		- According to google, [subversion](https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo)
		- Have to install via `apt install subversion`
		- And it works! Download success!
	- hm now when I try running the model training code I get `AttributeError: 'str' object has no attribute 'decode'` from keras
		- Earlier when installing I was getting error `tensorflow 2.7.0 requires keras<2.8,>=2.7.0rc0, but you have keras 2.3.1 which is incompatible.` but I figured that was some weird google colab thing because when I check the tf version being used it correctly returned 1.15... 
		- [Perhaps I need to downgrade CUDA version?](https://stackoverflow.com/questions/51888118/how-to-downgrade-tensorflow-version-in-colab) --> didn't work :(
		- Confusing since I'm installing exactly how I did when doing this locally... --> let me check my conda env to see if I forgot to note anything?
			- I have now exported my conda env --> time to figure out a way to install the contents of a conda env into google colab
		- Okay so apparently you can just install conda in google colab --> might this solve all my colab suffering?
			- NICE a library made for doing just this: [`condacolab`](https://github.com/conda-incubator/condacolab)
				- Initial install running correctly --> after forced refresh the file browser refuses to reconnect...
					- Just colab file browser being its slow self --> manually refresh web page makes file browser reappear
			- `environment.yml` seems to be installing correctly
				- Check `python --version` and tensorflow both return versions from env!
			- *Sigh* it can never be that easy --> `ModuleNotFound` error running first import statement
				- `conda list` confirms that it IS installed in the base conda environment
				- Checking the [setup notebook](https://colab.research.google.com/drive/1c_RGCgQeLHVXlF44LyOFjfUW32CmG6BP) provided by the library creators --> installs fine but same error when importing so maybe this ISN'T actually a me issue and rather colab did a messy update
			- [Opened issue on github](https://github.com/conda-incubator/condacolab/issues) --> temporarily on the back burner until I get a response


- Seems like the [clustering algorithim used by pixplot](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html) already transforms the images when clustering them --> no need to run my own modifications on images to clear/sharpen them?
-Does metadata affect pixplot clustering?

## Pixplot with no metadata
- Running with: `pixplot --images "/home/cbrou/Desktop/YODH-project/pixplot-nm/chapbook-illustrations/*.jpg"`
- hm installing pixplot installs tensorflow but not CUDA dependencies so you get the "could not load dynamic library..." error --> have to also install for tensorflow + gpu to work together properly:
  - `conda install -c anaconda cudatoolkit`
  - `conda install -c conda-forge cudnn`
- Analysing output
  - Clusters tend to draw from elements of image composition and page layout
    - I wonder what would happen if I cropped each page to just the image?
  - Cluster #3 seems to be focused on illustrations with human figures --> occasional boat lol
  - Cluster #9 is comprised of images that have the most detail --> I initially assumed this was due to resolution but there are some very detailed yet poorly preserved images included in this collection
  - Cluster #8 dedicated to song books --> is there some similarity among illustrations or is it picking up on the word "song" somehow
  - Definitely want to run this with metadata now --> how much of clustering speaks to the style of certain printers? or what era the chapbook was printed in??


## Adding metadata
- Okay so I concat the two dataframes of the og metadata and my pages and it returns NONE as being similar?
  - Oh the chapbook_ids are two different data types --> pandas has [astype](https://stackoverflow.com/questions/22005911/convert-columns-to-string-in-pandas) function that can convert data type of entire column
  - Of course this fixes it --> python data types strike again!
- Now lets check how many of these pages still have metadata due to having just their chapbook_id in the og metadata
