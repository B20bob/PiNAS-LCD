# Import LCD library
from RPLCD import i2c

# Import sleep library
from time import sleep

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)


#### Beginning of my code ####

import psutil


def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

# Input source of disk usage read
total = psutil.disk_usage('/pinas').free


# BEGINNING OF PRINT STATEMENTS


# Print Server name on top row
lcd.write_string('PiServer1')

lcd.crlf()

# Print IP address
lcd.write_string('IP: 192.168.0.198')

lcd.crlf()

# print free disk space (output)
print(bytes2human(total))

lcd.write_string('PiNas | Free Space:')

lcd.crlf()


lcd.write_string(bytes2human(total))

sleep(30)
#lcd.backlight_enabled = False
lcd.close(clear=True)
sleep(0.1)







## Write a string on first line and move to next line
 #lcd.write_string('Hello world')
 #lcd.crlf()
 #lcd.write_string('IoT with Vincy')
 #lcd.crlf()
 #lcd.write_string('Phppot')
 #sleep(5)

## Switch off backlight
#lcd.backlight_enabled = False 

## Clear the LCD screen
#lcd.close(clear=True)
