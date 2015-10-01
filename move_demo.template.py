import linkbot
import math

my_linkbot = linkbot.Linkbot('$SERIAL_ID')

distance = $distance # Distance to travel
radius = $radius     # Radius of the wheel
speed = $speed       # How fast to travel (in/sec)

radians = distance/radius
degrees = radians * 180 / math.pi

radians_per_second = speed/radius
degrees_per_second = radians_per_second * 180 / math.pi

my_linkbot.set_joint_speeds(degrees_per_second, 
                            degrees_per_second, 
                            degrees_per_second)
my_linkbot.move(degrees, degrees, -degrees)
