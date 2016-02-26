import pandas as pd

def main():
    
    # create a directory for selected photos
    print 'mkdir photos_las_vegas_food_drinks'

    # load data about selected photos
    selected_photos_business = pd.read_csv('las_vegas_food_drinks.csv')
    
    # for each photo generate copy command
    for photo_id in selected_photos_business['photo_id']: 
        print 'cp -v photos/' + photo_id + '.jpg photos_las_vegas_food_drinks'

if __name__ == "__main__":
    main()
