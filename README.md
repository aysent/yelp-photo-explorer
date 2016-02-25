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

Extract files from these archives:

```
tar xvf yelp_dataset_challenge_academic_dataset.tar
tar xvf 2016_yelp_dataset_challenge_photos.tar
```

Move photos to a separate directory:

```
mkdir photos
for f in ./*jpg; mv -v $f photos; done
```

One needs to use './' in front of '\*jpg' since filenames of some photos start with dash. 
In addition, one can't move photos just using 'mv ./*jpg photos' since there are too many (200,000) photos for mv command (see, for example, [http://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands](http://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands)).
