import graphlab
import sqlite3

def main():
    
    # load photos with their deep features
    photos = graphlab.SFrame('photos_deep_features.gl')

    # train a nearest neighbors model on deep features of photos
    nn_model = graphlab.nearest_neighbors.create(photos, features=['deep_features'], label='path')

    # sqlite database: key = photo name (p), value = list of names of 12 similar photos (p0, ..., p11)
    conn = sqlite3.connect('yelp-photo-explorer.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE photos (p, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)')

    # for each photo make an entry in the database
    for i in xrange(100):
        if i % 100 == 0: print 'processed ' + str(i) + ' out of ' + str(len(photos)) + '...'
        query = nn_model.query(photos[i:i+1], k=13, verbose=False)
        similar = []
        for s in query['reference_label']: similar.append(s[55:])
        c.execute('INSERT INTO photos VALUES ("' + '", "'.join(similar) + '")')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
