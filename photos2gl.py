import graphlab

def main():

    # load and save photos in graphlab format
    photos = graphlab.image_analysis.load_images('photos_las_vegas_food_drinks')
    photos.save('photos_las_vegas_food_drinks.gl')
    
    # load and save AlexNet model pre-trained and provided by Dato
    deep_learning_model = graphlab.load_model('http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45')
    deep_learning_model.save('imagenet_model_iter45.gl')

if __name__ == "__main__":
    main()
