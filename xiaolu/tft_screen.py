#!/usr/bin/python3
# coding=utf-8
'''
扫地机显示系统
功能：
1.系统开机后，现实欢迎界面，5秒后进入系统界面，显示系统默认状态，包括时间，当前运行状态（stopped）
2.用户按运行按钮，系统进入运行状态，此时，屏幕可以应该显示更多信息，包括实时的四个点位的避障数据、当前运行状态Runing,,启动运行的时长，后期再增加实时的PM10数值
3.用户按停止按钮，系统进入开机待运行状态，此时，屏幕回到1.
'''

from PIL import Image,ImageDraw,ImageFont
import time
import BHack_ILI9225 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi configuration.
RS = 27
RST = 17
SPI_PORT = 0
SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ILI9225(RS, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

# Load an image.
print('Loading image...')
image = Image.open('/home/pi/app/XiaoLu/file/background.png')
image = image.rotate(90).resize((176, 220))
disp.display(image)
time.sleep(5)

draw = disp.draw()

# Load default font.
font = ImageFont.load_default()

def __draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
	# Get rendered font width and height.
	draw = ImageDraw.Draw(image)
	width, height = draw.textsize(text, font=font)
	# Create a new image with transparent background to store the text.
	textimage = Image.new('RGBA', (width, height), (0,0,0,0))
	# Render the text.
	textdraw = ImageDraw.Draw(textimage)
	textdraw.text((0,0), text, font=font, fill=fill)
	# Rotate the text image.
	rotated = textimage.rotate(angle, expand=1)
	# Paste the text into the image, using it as a mask for transparency.
	image.paste(rotated, position, rotated)

def display(_1553b):
    while True:
        disp.clear((0, 255, 0))
        # draw format
        draw.line([(40, 0), (40, 220)], fill=(255, 255, 255), width=1)
        draw.line([(40, 60), (176, 60)], fill=(255, 255, 255), width=1)
        if '0x02_0x04' in _1553b and _1553b['0x02_0x04'].get('data') is not None:
            print(_1553b['0x02_0x04'].get('data'))
            __draw_rotated_text(disp.buffer, 'A:' + _1553b['0x02_0x04'].get('data')[0], (10, 20), 90, font, fill=(255, 255, 255))
            __draw_rotated_text(disp.buffer, 'B:' + _1553b['0x02_0x04'].get('data')[1], (10, 40), 90, font, fill=(255, 255, 255))
            __draw_rotated_text(disp.buffer, 'C:' + _1553b['0x02_0x04'].get('data')[2], (10, 60), 90, font, fill=(255, 255, 255))
            __draw_rotated_text(disp.buffer, 'D:' + _1553b['0x02_0x04'].get('data')[3], (10, 80), 90, font, fill=(255, 255, 255))
        __draw_rotated_text(disp.buffer, ">> " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()), (60, 80), 90, font,
                          fill=(255, 255, 255))
        __draw_rotated_text(disp.buffer, ">> " + 'Runing', (80, 80), 90, font, fill=(0, 255, 0))
        disp.display()
        time.sleep(1)