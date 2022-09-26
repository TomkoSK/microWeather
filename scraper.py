import requests
from bs4 import BeautifulSoup
import uflash
import os

rainList = ['Rain', 'Scattered Showers', 'Heavy Rain']
sunList = []
cloudList = ['Foggy', 'Cloudy', 'Mostly Cloudy Night']
TEMPERATURE = 1
RAIN = 2
CONDITION = 3
temperatureClass = "DetailsSummary--tempValue--1K4ka"
rainClass = "DetailsSummary--precip--1ecIJ"
conditionClass = "DetailsSummary--condition--24gQw"
timeClass = "DetailsSummary--daypartName--2FBp2"
url = 'https://weather.com/en-GB/weather/hourbyhour/l/3f32091e89434bd939d19c94aaf7979f6e8da5103246f430d237749302731bfd'
soup = None

def getTimeDict():
    firstIndex = soup.find(id='detailIndex0')
    firstIndexTimeString = firstIndex.find(class_=timeClass).text
    index = firstIndexTimeString.index(':')
    firstIndexTime = int(firstIndexTimeString[:index])
    indexDict = {}
    detailIndex = 0
    if(firstIndexTime == 0):
        for time in range(0, 24):
            indexDict[time]=f'detailIndex{detailIndex}'
            detailIndex += 1
    else:
        for time in range(firstIndexTime, 24):
            indexDict[time]=f'detailIndex{detailIndex}'
            detailIndex += 1
    return indexDict

def getData(hour, type):
    timeDict = getTimeDict()
    detailIndex = soup.find(id=timeDict[hour])
    if(type == TEMPERATURE):
        return detailIndex.find(class_=temperatureClass).text
    elif(type == CONDITION):
        return detailIndex.find(class_=conditionClass).title.text
    elif(type == RAIN):
        return detailIndex.find(class_=rainClass).text

def getWeatherDict():#Gets a dictionary of the temperature, condition and rain chance for every hour of the day
    dictionary = getTimeDict()
    weatherDict = {}
    for hour in dictionary:
        dataList = []
        temp = getData(hour, TEMPERATURE)
        temp = temp.replace('°', '')
        temp = int(temp)
        dataList.append(temp)
        condition = getData(hour, CONDITION)
        if(condition in rainList):
            condition = 'rain'
        elif(condition in cloudList):
            condition = 'cloud'
        elif(condition in sunList):
            condition = 'sun'
        dataList.append(condition)
        weatherDict[hour] = dataList
        rain = getData(hour, RAIN)
        rain = rain.replace('Rain', '')
        rain = rain.replace('%', '')
        rain = int(rain)
        dataList.append(rain)
    return weatherDict

def updateSoup():
    global soup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

def main():
    updateSoup()#Scrapes the website
    weatherDict = getWeatherDict()
    print(weatherDict)
    with open('mainTemplate.py', 'r') as file:#replaces the '#REPLACELINE' with the weather dictionary
        content = file.read()
    content = content.replace('#REPLACELINE', f'weatherDict = {weatherDict}')
    with open('main.py', 'a') as file:#makes a new main.py file, and flashes it onto the microbit
        file.write(content)
    uflash.flash('main.py')
    os.remove('main.py')

if(__name__ == '__main__'):
    main()