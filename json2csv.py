import json

def main():
    input_json = json.load(open("photo_id_to_business_id.json"))
    
    # print the header of output csv file
    print 'photo_id,business_id,label'
    
    # for each entry in input json file print one csv row
    for i in xrange(len(input_json)):
        photo_id = input_json[i]['photo_id']
        business_id = input_json[i]['business_id']
        label = input_json[i]['label']
        print photo_id + ',' + business_id + ',' + label

if __name__ == "__main__":
    main()
