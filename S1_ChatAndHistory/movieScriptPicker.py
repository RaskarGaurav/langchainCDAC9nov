import random
def actor_picker():
    actors = ("Tom Hanks","Brad Pitt","Tom Cruise","Shahrukh Khan","Pankaj Tripathi","Jackie Chan")
    return random.choice(actors)

def location_picker():
    locations = ("India","London","Moon","Pacific Ocean","Sahara Desert","Tokyo","Hawaii","Kashmir","Alpes Mountains")
    return random.choice(locations)

def theme_picker():
    themes = ("Adventure","Romantic","Spy","Sci-Fi","Action","Drama","Horror","Comedy","Crime","Comedy","Thriller")
    return random.choice(themes)