import json

def main():

    # print the header of output csv file
    print 'business_id,name,city,latitude,longitude'

    # for each entry in input json file print one csv row
    for line in open("data/yelp_academic_dataset_business.json"):
        input_json = json.loads(line)
        business_id = input_json['business_id']
        name = input_json['name'].encode('ascii', 'ignore').replace(',', '').replace('"', '')
        city = input_json['city'].encode('ascii', 'ignore').replace(',', '')
        latitude = str(input_json['latitude'])
        longitude = str(input_json['longitude'])
        print business_id + ',' + name + ',' + city + ',' + latitude + ',' + longitude

if __name__ == "__main__":
    main()
