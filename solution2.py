from math import floor
from random import randint
from bs4 import BeautifulSoup
from pyparsing import col
import requests
import csv 
import psycopg2

# conn = psycopg2.connect(
#     database = "testbb",
#     user = "kiishi",
#     password = "kiishi",
#     host = "localhost",
#     port = "5432"
# )

# cur = conn.cursor()

# cur.execute("""/
#     CREATE TABLE IF NOT EXISTS `colors` (
#   `color_id` int(11) NOT NULL AUTO_INCREMENT,
#   `color` varchar(255) NOT NULL,
#   `No_of_colors`int(11) NOT NULL,
  
# ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

# """)

HTMLFileToBeOpened = open("python_class_question.html", "r")
  
contents = HTMLFileToBeOpened.read()
soup = BeautifulSoup(contents, 'html.parser')

file = open("data.csv", "w")
writer = csv.writer(file)

quotes = soup.findAll("td")
color = []
day = []
colorDay = []
print('hello')
for quote in quotes:
    if(quotes.index(quote) % 2 != 0 or quotes.index(quote) == 1 ):
        color.append([quote.text])
        # print(color)
    else:
        day.append(quote.text)
    

    
def removeComma  (elx):
    y =",".join(elx).split()
    c = []
    for x in y:
        if(x[-1] == ","):
            x = x[:-1]
        c.append(x)
    return c

for el in range(len(color)):
    color[el] = removeComma(color[el])

# print(color)
def DataObj ():
    obj = []
    for data in color:
        obj.extend(data)

    return obj

data = DataObj()

# print(data)

def DataCount (data):


    newDays = []
    days = []
    visited = []
    for x in data:
        
        if(x in visited):
            continue
        visited.append(x)
        colorObj = {
            f"{x}": data.count(x),
            }
    
        newDays.append(colorObj)
    
    return newDays

colorTotal = DataCount(data)
# print(colorTotal, len(data))

# def insertToDB ():
#     for c in colorTotal:
#         cur.execute(f"INSERT INTO colors(color_id, color, No_of_colors) values ({colorTotal.index(c)}, {list(c.keys())[0]}, {list(c.values())[0]})")
    
def findMean ( colors):
    count = 0
    for c in colors:
        num = list(c.values())[0]
        # print(num)
        count += num

    mean = count/len(color)  
    return mean      

mean = findMean(colorTotal)

print(f"Mean = {mean}")

def findMode (colors):
    numList = []
    for c in colors:
        num = list(c.values())[0]
        numList.append(num)
    
    maxNum = max(numList)
    # print(maxNum)
    objIndex = numList.index(maxNum)
    obj = colors[objIndex]
    modeColor = list(obj.keys())[0]
    return modeColor


mode = findMode(colorTotal)

print(f"Color worn mostly throughout the week(Mode) = {mode}")

def findMedian(data):
    median = data[int(mean)]
    return median

median = findMedian(data)

print(f"Color thst is median = {median}")

def findVariance (colors):
    sumV = 0
    for c in colors:
        sumV += (abs(list(c.values())[0] - mean)**2)
    v = (sumV)/(len(colors) - 1)
    return v

var = findVariance(colorTotal)
print(f"Variance of colors {var}")


def randBinary (): 
    ranNums = f""
    for x in range(4):
        num = randint(0, 1)
        ranNums += f"{num}"
    
    print(f"Number in Binary {ranNums}")
    print(f"Number in Decimal {int(ranNums, 2)}")
    return (int(ranNums, 2))

    
randBinary()

def fibSequenc(x):
    if x < 0:
        raise ValueError("Argument has to be a nonnegative integer")
    if x == 0:
        return []
    if x == 1:
        return [0]
    result = [0, 1]
    for _ in range(x-2, 0, -1):
        result.append(result[-1] + result[-2])
    return result

print(f"First 50 Fibonacci Sequence {fibSequenc(50)}")


def searchNum (y, l, r, x):
    
    y = sorted(y)
    print(f"Sorted Array {y}")
    if r >= l:
        mid = l + (r - l) 
        if y[mid] == x:
            return mid
        elif y[mid] > x:
            return searchNum(y, l, mid-1, x)
        else:
            return searchNum(y, mid + 1, r, x)
    else:
        return -1
        
arr = [3, 67 , 8, 2, 6 , 4, 5, 2, 6, 9]
num = 5
print(f"search Num {5} in array {arr} index is {searchNum(arr, arr[0], len(arr) - 1, num)} after sorting")