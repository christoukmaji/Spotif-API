#  Spotif-API README  #
## Chris Toukmaji | christoukmaji@gmail.com ##

### Using Program

This program is customized for a U-chained two (64 x 32) LED matrix forming a 64 x 64 panel. However, these parameters can be changed by changing the `--led-cols` and `--led-rows` flags (or whichever flags you would be changing) in the sudo command to the operating system in the `spotif-api.py` file. 

Once all the required hardware has been assembled, and you have ensured that your Raspberry Pi is running Python 3 (you can check with `python3 --version`), enter the Spotify Authorization token that is given [here](https://developer.spotify.com/console/get-users-currently-playing-track/?market=ES&additional_types=). Note: A Spotify account is required to properly run this code.

Then, simply write <pre>$ python3 spotif-api.py</pre>


### Features

- Gives a retro look to your currently playing Spotify song by displaying the album cover on a 64x64 LED Matrix.
- Displays relevant weather, stocks, and news information (est. March 2020)
- See 'Future Features' for all the other upcoming advancements of this project 


### Hardware
- [Raspberry Pi Zero WH ](https://www.adafruit.com/product/3708)
	- Note: This is different that the Raspberry Pi Zero and the Raspberry Pi Zero W. The WH versions comes with built in Wi-Fi and Bluetooth, in addition to soldered GPIO headers, which saves the cluttering of  a USB Wi-Fi adapter and the connections of each individual GPIO pin to a breadboard. 
- [Adafruit RGB Matrix Bonnet](https://www.adafruit.com/product/3211)
	- This allows us to connect our Pi to the matrix with just a ribbon cable: a very clean setup.
- [5V Power Supply ](https://www.amazon.com/ALITOVE-100V-240V-Converter-5-5x2-1mm-Security/dp/B078RXZM4C/ref=sr_1_4?dchild=1&keywords=5v+power&qid=1609984847&sr=8-4)
	- This powers our Pi and the matrix
- LED Boards 
	- Try to aim for either two 32 x 64 boards, or one 64 x 64 board. Anything smaller board wouldn't have enough pixels to make any distinct images. I used two 32 x 64 boards just so that I had the flexibility to switch to a 32 x 128 setup, but if you are set on the 64 x 64 setup, I would highly recommend going for the single board; it will avoid a lot of the wiring mess.
	- [64 x 64 Board](https://www.adafruit.com/product/3649?gclid=EAIaIQobChMI4u-R6N2I7gIVyf7jBx22GgD_EAQYASABEgIOT_D_BwE)
	- [64 x 32 Board](https://www.adafruit.com/product/2277)
	- Note: The size of the pitch is up to you. I used a 5 mm pitch since the board is situated far from my eye-level, but if you are aiming for a closer and more high definition image, I would highly recommend something around a 2-3 mm pitch.  



### References

This project could not have been done without the help of the [Raspberry Pi RGB LED Matrix library by Mr. Henner Zeller](https://github.com/hzeller). 

### Future Features

I am currently working on a voice interface that allows the user to control the matrix remotely. Additionally, I am increasing the project's capabilities to include information such as weather information, daily news, and stock tickers; most of which have already been implemented, but lack a proper method of transition (which is what the voice interface will solve).


### Issues

- Flickering: This is a hardware issue with the Raspberry Pi 0 being underpowered; this issue could be solved by soldering two of the GPIO pins on the Pi itself. More info can be found on Mr. Henner Zeller's documentation.


### Behind The Scenes

This project initially started out as a scrolling news ticker, like something that would be shown at the bottom of your local news channel. I tailored the news to my interests so that I would only be seeing the news that was relevant to me. I then transitioned into making a stock ticker, then a weather ticker, and now, this. I am looking forward to the day when I can incorporate all four projects within one, and develop my own AI digital assistant. 

