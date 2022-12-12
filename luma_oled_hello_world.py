from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
from pyowm import OWM
from pathlib import Path
from PIL import Image

import smbus
import time
import time
import RPi.GPIO as GPIO

owm = OWM('b43fb795ce8da35cf9c0f4c4fe4a23ae')

reg = owm.city_id_registry()
list_of_tuples = BE = reg.ids_for('Bellevue', country='US')
id_of_be_city = list_of_tuples[0][0]
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Bellevue,US')

w = observation.weather
w_temperature = w.temperature('celsius')
w_temperature_present = w_temperature['temp']
w_status = w.detailed_status
w_status_uppercase = w_status.upper()
#print("Temperature =  ",w_temperature_present)
#print(w_status_uppercase)

serial = i2c(port=1, address=0x3C)

oled_1 = ssd1306(i2c(port=1, address=0x3C))
oled_2 = ssd1306(i2c(port=5, address=0x3C))
oled_3 = ssd1306(i2c(port=6, address=0x3C))


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

with canvas(oled_1) as draw:
	draw.text((30, 40), str(w_temperature_present) + " C", fill = "white")
	draw.text((30, 20), str(w_status_uppercase), fill = "white")
	#draw.rectangle(oled_1.bounding_box, outline="white", fill="black")
	#draw.text((30, 40), "First Screen", fill="white")

posn = ((oled_3.width - oled_3.width) // 2 + 17, -18)
	
with canvas(oled_3) as draw:
	img_path = str(Path(__file__).resolve().parent.joinpath('weather_images', 'broken_clouds.png'))
	logo = Image.open(img_path).convert("RGBA")
	fff = Image.new(logo.mode, logo.size, (255,) * 4)

	background = Image.new("RGBA", oled_2.size, "white")
	posn = ((oled_3.width - oled_3.width) // 2 + 17, -18)
	
	# draw.rectangle(oled_3.bounding_box, outline="white", fill="black")
	# draw.text((30, 40), "Third Screen", fill="white")

count = 0
prev_state = GPIO.input(10)
curr_state = GPIO.input(10)

while True:
	prev_state = curr_state
	curr_state = GPIO.input(10)
	
	if prev_state != curr_state:
		if prev_state == GPIO.LOW and curr_state == GPIO.HIGH:
			count += 1
			with canvas(oled_2) as draw:
				draw.rectangle(oled_2.bounding_box, outline="white", fill="black")
				draw.text((60, 30), str(count), fill="white")
			
	for angle in range(0, 2, 2):
		rot = logo.rotate(angle, resample=Image.BILINEAR)
		img = Image.composite(rot, fff, rot)
		background.paste(img, posn)
		oled_3.display(background.convert(oled_3.mode))
	time.sleep(1)
