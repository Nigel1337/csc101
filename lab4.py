# -*- coding: utf-8 -*-
"""lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7s3aPeOoi_XN57kLM7AqpEIe9e3_8Kw
"""

equation = (input("Enter you equation: "))

a,b,c = equation.split(" ")

a = int(a)
b= b.lower().strip()
c = int(c)

if (b=="*"):
    sum = (a*c)
    print(f"Answer is  {sum}")

elif (b=="+"):
    sum =(a+c)
    print(f"Answer is  {sum}")

elif (b=="-"):
    sum =(a-c)
    print(f"Answer is  {sum}")

elif (b=="/"):
    sum =(a/c)
    print(f"Answer is  {sum}")

else:
      print("Error")

def main():
  time = input("Please enter the time for where you would be: ")
  if time < 8:
    print("Nothing to do")
  elif time >= 8.0 and <=10.0:
    print("Reading lessons")
  elif time >=10.0 and <=12.0:
    print("Math lessons")
  elif time >=12.0 and <= 13.0:
    print("Lunch Time")
  elif time >= 13.0 and <=14.0:
    print("Music Lessons")
  else time > 14:
    print("You are free")

def convert_time(time):
  time = time.replace(":",".")
  time = float(time)
  return time
