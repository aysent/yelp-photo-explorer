import pandas as pd
import pickle

def main():
    
    # load data about photos and businesses
    data = pd.read_csv('las_vegas_food_drinks.csv')

    # dictionary: key = photo index, value = photo name
    d = {}

    # for each photo make an entry in the dictionary
    for index, row in data.iterrows():
        d[int(index)] = row['photo_id']

    # pickle the dictionary
    pickle.dump(d, open('photo_id_name.pickle', 'w'))


if __name__ == "__main__":
    main()

