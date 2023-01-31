import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import psutil
import socket

# OLED display setup
# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128) # Change rows & cols values depending on your display dimensions.
led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)

# IP address
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# CPU usage
def get_cpu_usage():
    return psutil.cpu_percent()

# CPU Temp
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return round(float(cpu_temp)/1000, 2)

# Calculate memory information
memory = psutil.virtual_memory()
# Convert Bytes to MB (Bytes -> KB -> MB)
used = round(memory.used/1024.0/1024.0,)
total = round(memory.total/1024.0/1024.0,)
mem_info = 'Mem:' + str(used) + '/' + str(total) + 'MB (' + str(memory.percent) + '%)'

# Calculate disk information
disk = psutil.disk_usage('/')
# Convert Bytes to GB (Bytes -> KB -> MB -> GB)
used = round(disk.used/1024.0/1024.0/1024.0,1)
total = round(disk.total/1024.0/1024.0/1024.0,)
disk_info = 'Disk:' + str(used) + '/' + str(total) + 'GB (' + str(disk.percent) + '%)'

# Display data
def display_stats():
    led.clear_display()
    led.draw_text2(0,0,'IP: ',1)
    led.draw_text2(18,0,get_ip_address(),1)
    led.draw_text2(0,8,'CPU: ',1)
    led.draw_text2(26,8,str(get_cpu_usage()) + '%',1)
    led.draw_text2(90,8,str(get_cpu_temp()) + 'C',1)
    led.draw_text2(0,16,mem_info,1)
    led.draw_text2(0,24,disk_info,1)
    led.display()

# Run the display loop
while True:
    display_stats()
    time.sleep(1)
