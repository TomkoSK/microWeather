from microbit import *
import time

def writeDigit(number, x=1):#Displays a digit on the microbit
    if(x == 1):
        x1, x2 = 0, 1
    elif(x == 2):
        x1, x2 = 1, 2
    elif(x == 3):
        x1, x2 = 3,4
    if(number == '-'):
        display.set_pixel(0, 2, brightness-2)
    elif(number == 0):
        for n in range(0, 5):
            display.set_pixel(x1, n, brightness)
            display.set_pixel(x2, n, brightness)
    elif(number == 1):
        display.set_pixel(x1, 1, brightness)
        for n in range(0, 5):
            display.set_pixel(x2, n, brightness)
    elif(number == 2):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 2, brightness)
        display.set_pixel(x1, 3, brightness)
        display.set_pixel(x1, 4, brightness)
        display.set_pixel(x2, 0, brightness)
        display.set_pixel(x2, 1, brightness)
        display.set_pixel(x2, 2, brightness)
        display.set_pixel(x2, 4, brightness)
    elif(number == 3):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 4, brightness)
        display.set_pixel(x1, 2, brightness)
        for n in range(0, 5):
            display.set_pixel(x2, n, brightness)
    elif(number == 4):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 1, brightness)
        display.set_pixel(x1, 2, brightness)
        for n in range(2, 5):
            display.set_pixel(x2, n, brightness)
    elif(number == 5):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 1, brightness)
        display.set_pixel(x1, 2, brightness)
        display.set_pixel(x1, 4, brightness)
        display.set_pixel(x2, 0, brightness)
        for n in range(2, 5):
            display.set_pixel(x2, n, brightness)
    elif(number == 6):
        for n in range(1, 5):
            display.set_pixel(x1, n, brightness)
        display.set_pixel(x2, 0, brightness)
        display.set_pixel(x2, 3, brightness)
        display.set_pixel(x2, 4, brightness)
    elif(number == 7):
        display.set_pixel(x1, 0, brightness)
        for n in range(0, 5):
            display.set_pixel(x2, n, brightness)
    elif(number == 8):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 1, brightness)
        display.set_pixel(x1, 3, brightness)
        display.set_pixel(x1, 4, brightness)
        display.set_pixel(x2, 0, brightness)
        display.set_pixel(x2, 1, brightness)
        display.set_pixel(x2, 3, brightness)
        display.set_pixel(x2, 4, brightness)
    elif(number == 9):
        display.set_pixel(x1, 0, brightness)
        display.set_pixel(x1, 1, brightness)
        display.set_pixel(x1, 4, brightness)
        for n in range(0, 4):
            display.set_pixel(x2, n, brightness)

def showNumber(number):#Displays any number between -99 and 99 on the microbit
    display.clear()
    numbers = [x for x in str(number)]
    if(numbers[0] == '-'):
        writeDigit('-')
        writeDigit(int(numbers[1]), 2)
        if(len(numbers) == 3):
            writeDigit(int(numbers[2]), 3)
    else:
        writeDigit(int(numbers[0]), 1)
        if(len(numbers) == 2):
            writeDigit(int(numbers[1]), 3)

def showSymbol(symbol):#Shows a symbol of the sun, cloud, or a raindrop
    brightnessLocal = str(brightness)
    if(symbol == 'sun'):
        image = Image(brightnessLocal+"0"+brightnessLocal+"0"+brightnessLocal+"\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0\n"+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+"\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0\n"+brightnessLocal+"0"+brightnessLocal+"0"+brightnessLocal)
    elif(symbol == 'cloud'):
        image = Image("00000\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0\n"+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+"\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0\n"+"00000")
    elif(symbol == 'rain'):
        image = Image("00"+brightnessLocal+"00\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0\n"+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+"\n"+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+brightnessLocal+"\n"+"0"+brightnessLocal+brightnessLocal+brightnessLocal+"0")
    display.show(image)


TEMPERATURE = 0
CONDITION = 1
RAIN = 2

#REPLACELINE
#The line above is replaced by the dictionary made in scraper.py
brightness = 7#The level of brightness the numbers and symbols will be displayed at (1-9)
lowestHour = min(list(weatherDict))
highestHour = 23
mode = TEMPERATURE#Chooses whether to display the temperature, condition, or rain chance
hour = lowestHour#Chooses which hour to display either the temp, condition or rain chance of
showingHour = False#Turns true if the hour is being shown on the display
hourShownTime = 0
buttonPressTime = 0
showNumber(weatherDict[hour][mode])
while(True):
    if(showingHour and time.ticks_ms() - hourShownTime > 1000):#If the number of the hour has been shown for more than a second, it goes back to showing the weather
        showingHour = False
        if(mode == TEMPERATURE):
            showNumber(weatherDict[hour][TEMPERATURE])
        elif(mode == CONDITION):
            if(weatherDict[hour][CONDITION] == 'rain'):
                showSymbol('rain')
            elif(weatherDict[hour][CONDITION] == 'sun'):
                showSymbol('sun')
            elif(weatherDict[hour][CONDITION] == 'cloud'):
                showSymbol('cloud')
        elif(mode == RAIN):
            showNumber(weatherDict[hour][RAIN])
    oldMode = mode
    oldHour = hour
    if(button_a.is_pressed()):
        if(time.ticks_ms() - buttonPressTime > 400):#Button presses only register every half a second
            buttonPressTime = time.ticks_ms()
            if(mode < 2):#Changes the mode between temperature, condition and rain chance
                mode += 1
            else:
                mode = 0
    if(button_b.is_pressed()):
        if(time.ticks_ms() - buttonPressTime > 400):#Button presses only register every half a second
            buttonPressTime = time.ticks_ms()
            if(showingHour):#If the hour is not being shown yet, it will not be changed when the B button is pressed
                if(hour < 23):#changes the hour that will be shown by 1
                    hour += 1
                else:
                    hour = lowestHour
            showNumber(hour)#Shows the hour that has been selected for a second
            showingHour = True
            hourShownTime = time.ticks_ms()
    if(mode != oldMode or hour != oldHour):#If the hour or the mode was changed, the display changes
        if(not showingHour):#If the hour is being shown, display wont change
            if(mode == TEMPERATURE):
                showNumber(weatherDict[hour][TEMPERATURE])
            elif(mode == CONDITION):
                if(weatherDict[hour][CONDITION] == 'rain'):
                    showSymbol('rain')
                elif(weatherDict[hour][CONDITION] == 'sun'):
                    showSymbol('sun')
                elif(weatherDict[hour][CONDITION] == 'cloud'):
                    showSymbol('cloud')
            elif(mode == RAIN):
                showNumber(weatherDict[hour][RAIN])