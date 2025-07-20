import json 

# open data.json file
with open('data.json', 'r') as file:
    data = json.load(file)
    # data -> getAccommodationDetails -> accommodationDetails[0] -> contactDetails
    hotel_name = data['data']['getAccommodationDetails']['accommodationDetails'][0]['translatedName']['value']
    hotel_email = data['data']['getAccommodationDetails']['accommodationDetails'][0]['contactDetails']['email']
    hotel_phone = data['data']['getAccommodationDetails']['accommodationDetails'][0]['contactDetails']['phone']
    hotel_website = data['data']['getAccommodationDetails']['accommodationDetails'][0]['contactDetails']['website']
    print(hotel_name)
    print(hotel_email)
    print(hotel_phone)
    print(hotel_website)