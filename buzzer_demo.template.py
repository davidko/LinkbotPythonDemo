import linkbot
import time

my_linkbot = linkbot.Linkbot('$SERIAL_ID')
my_linkbot.set_buzzer_frequency($frequency)
time.sleep(1)
my_linkbot.set_buzzer_frequency(0)

