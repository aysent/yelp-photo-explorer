# yelp-photo-explorer
Explore new businesses on Yelp using photo similarity

## Getting data

Announcement of the Yelp Dataset Challenge Round 7:

[http://engineeringblog.yelp.com/2016/02/yelp-dataset-challenge-round7-announcement.html](http://engineeringblog.yelp.com/2016/02/yelp-dataset-challenge-round7-announcement.html)

Yelp Dataset Challenge:

[https://www.yelp.com/dataset_challenge](https://www.yelp.com/dataset_challenge)

Get data:

[https://www.yelp.com/dataset_challenge/dataset](https://www.yelp.com/dataset_challenge/dataset)

Download the following two files:

```
yelp_dataset_challenge_academic_dataset.tar
2016_yelp_dataset_challenge_photos.tar
```

Extract files from these archives to 'data' and 'photos' directories:

```
mkdir data
tar xvf yelp_dataset_challenge_academic_dataset.tar -C data
mkdir photos
tar xvf 2016_yelp_dataset_challenge_photos.tar -C photos
```

## Preprocessing data

For each photo extract its name, label, and corresponding business id from json file and save these data in csv format:

```
python json2csv_photos.py > photos.csv
```

For each business extract its id and location (city, latitude, longitude) from json file and save these data in csv format:

```
python json2csv_business.py > business.csv
```

Merge data about photos and corresponding businesses so that we know location of each photo:

```
python merge_photos_business.py
```

For this project we select photos of food and drinks taken in Las Vegas businesses, copy them to a separate directory:

```
python copy_selected_photos.py > copy_selected_photos.sh
source copy_selected_photos.sh
```

In one of the following steps we will extract deep features of selected photos using AlexNet neural network [1] pre-trained and provided by Dato [2]. But before that we resize all photos to 256x256:

```
cd photos_las_vegas_food_drinks
mogrify -resize 256x256\! ./*jpg
cd ..
```

Load and save selected photos and AlexNet model in a format suitable for Dato GraphLab Create [3]:

```
python photos2gl.py
```

## Extracting deep features

Extract deep features of selected photos using AlexNet neural network:

```
python extract_deep_features.py
```

The output dataset is available on Amazon S3 and can be loaded in python script as:

```python
import graphlab

data = graphlab.SFrame('http://yelp-photo-explorer.s3.amazonaws.com/photos_deep_features.gl')
```

## Example of finding similar photos

This repository provides an example ipython notebook that shows how deep features of photos can be used to train a nearest neighbors and query it to find photos similar to any given photo (PDF version of the notebook correctly shows similar photos).


[1] [http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

[2] [http://www.slideshare.net/dato-inc/introduction-to-deep-learning-for-image-analysis-at-strata-nyc-sep-2015](http://www.slideshare.net/dato-inc/introduction-to-deep-learning-for-image-analysis-at-strata-nyc-sep-2015)

[3] [https://dato.com/products/create/](https://dato.com/products/create/)
