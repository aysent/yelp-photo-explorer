import graphlab

def main():

    # load selected photos
    photos = graphlab.SFrame('photos_las_vegas_food_drinks.gl')

    # load AlexNet model pre-trained and provided by Dato
    alexnet_model = graphlab.load_model('imagenet_model_iter45.gl')

    # extract and save deep features of selected photos
    photos['deep_features'] = alexnet_model.extract_features(photos)
    photos.save('photos_deep_features.gl')

if __name__ == "__main__":
    main()
