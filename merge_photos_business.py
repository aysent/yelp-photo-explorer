import pandas as pd

def main():
    
    # load data about photos and businesses
    photos = pd.read_csv("photos.csv")
    business = pd.read_csv("business.csv")

    # merge data about photos and businesses
    photos_business = pd.merge(photos, business, on='business_id')

    # print top 5 cities and photo labels
    print photos_business['city'].value_counts().head()
    print photos_business['label'].value_counts().head()

    # top 5 cities:
    # Las Vegas     92451
    # Phoenix       22578
    # Scottsdale    12530
    # Charlotte      8973
    # Henderson      8401

    # top 5 photo labels:
    # none       120000
    # outside     16000
    # food        16000
    # drink       16000
    # inside      16000

    # for this project select photos of food and drinks from businesses in Las Vegas, NV
    selected_photos_business = photos_business[photos_business['city'] == 'Las Vegas']
    selected_photos_business = selected_photos_business[selected_photos_business['label'].isin(['food', 'drink'])]

    # save selected data
    selected_photos_business.to_csv("las_vegas_food_drinks.csv", index=False)

if __name__ == "__main__":
    main()
