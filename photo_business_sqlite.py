import pandas as pd
import sqlite3

def main():
    
    # load data about photos and businesses
    data = pd.read_csv('las_vegas_food_drinks.csv')

    # sqlite database
    conn = sqlite3.connect('photo_business.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE photos (photo_name PRIMARY KEY, business_name, latitude, longitude)')

    # for each photo make an entry in the database
    for index, row in data.iterrows():
        photo_name = row['photo_id']
        business_name = row['name']
        latitude = str(row['latitude'])
        longitude = str(row['longitude'])
        print 'INSERT INTO photos VALUES ("' + '", "'.join([photo_name, business_name, latitude, longitude]) + '")'
        c.execute('INSERT INTO photos VALUES ("' + '", "'.join([photo_name, business_name, latitude, longitude]) + '")')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

