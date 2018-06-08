import json
import urllib.request
import turtle

# address of web service that has data about astronauts in space
url_astros = 'http://api.open-notify.org/astros.json'
# store the retrieved json data
response_astros = urllib.request.urlopen(url_astros)
# put json data in a python dict
result_astros = json.loads(response_astros.read())

# separate some data into proper variables(optional)
num_people = result_astros['number']
people = result_astros['people']

print("Total people in space:", num_people)
print("Those are their names and where they are:")
for p in people:
    print("{} - {}".format(p['name'], p['craft']))

print("")
print("--------------------------------------------------------------------------")
print("")

# address that has that data about ISS location
url_iss = 'http://api.open-notify.org/iss-now.json'
response_iss = urllib.request.urlopen(url_iss)
result_iss = json.loads(response_iss.read())

location = result_iss['iss_position']
# had to convert from string to float in order to use the Turtle library
latitude = float(location['latitude'])
longitude = float(location['longitude'])
#print(type(longitude))
print("Let's show the ISS coordinates: ")
print("Latitude:", latitude)
print("Longitude:", longitude)

print("")
print("--------------------------------------------------------------------------")
print("")

# Here we are going to generate a screen with a flat world map and a space station small 
# image(representing ISS) placed above the coordinates of the ISS.

print("How about to see it in a map?")
# create object Turtle
screen = turtle.Screen()
# Set screen size to match world map image size
screen.setup(720, 360)
# set world coordinates in the map
screen.setworldcoordinates(-180, -90, 180, 90)
# set the image we want to use
screen.bgpic('map.gif')

# register the space station image on our screen
screen.register_shape('iss2.gif')
# create space station object
iss = turtle.Turtle()
# set the imagem
iss.shape('iss2.gif')
# set the initial position
iss.setheading(90)

# no drawing while moving image
iss.penup()
# move to an absolute location(in this case, ISS latitude and longitude)
iss.goto(longitude, latitude)
# keeps the screen open until a click happens
screen.exitonclick()
