import requests

url = "https://trips-48955.firebaseio.com/trips/3.json"


initial_data = {
    "trip1": {
        "description": "The city in itself is an epic adventure, but the journey to the top...",
        "imagePath": "https://www.bookmundi.com/blog/wp-content/uploads/2016/07/Machu-Picchu.jpg",
        "name": "Exploring Machu Picchu, Peru"
    },
    "trip2": {
        "description": "It is the largest coral reef system on the planet...",
        "imagePath": "https://www.wur.nl/upload_mm/4/f/1/e40f0bf1-2d66-4454-93d8-128e205f9df6_coral_b2ed0640_490x330.jpg",
        "name": "Diving, Great Barrier Reef, Australia"
    },
    "trip3": {
        "description": "Dominated by the iconic Mt. Everest, Himalayan adventures...",
        "imagePath": "https://www.bookmundi.com/blog/wp-content/uploads/2016/07/Hiker-trekking-in-the-mountains-of-Nepal.jpg",
        "name": "Trekking in The Himalayas"
    }
}
new_trip_data = {
    "description": "October-November and February-March are the best times to see the northern lights.",
    "imagePath": "https://www.aurora-nights.co.uk/wp-content/uploads/2019/07/norway-northern-lights-1500x587_c.jpg",
    "name": "Capture the Northern Lights on camera"
}

response = requests.delete(url, json=new_trip_data)

if response.status_code == 200:
    print(response.json())
else:
    print("Mistake:", response.status_code)