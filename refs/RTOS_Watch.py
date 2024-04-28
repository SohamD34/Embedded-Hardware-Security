from time import strftime
from tkinter.ttk import *
from tkinter import *
import keyboard
import threading
import time
import json
from urllib.request import urlopen
import haversine as hs
from haversine import Unit
import datetime
import math
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time


# following function determines the temperature of the user, with the help of the sensor.
def temp_sensor():
    sensor = W1ThermSensor()
    while True:
        temperature = sensor.get_temperature()
        print("The temperature is %s celsius" % temperature)
        time.sleep(1)

# This function is necessary for creating the analog watch face
def ana_watch():
    class WatchFace:
        def __init__(self, master):
            self.master = master
            self.create_widgets()

        def create_widgets(self):
            self.clock = tk.Canvas(self.master, width=200, height=200)
            self.clock.pack(fill='both', expand=True)
            self.clock.create_oval(10, 10, 190, 190, width=2)
            for i in range(12):
                angle = i * math.pi / 6
                x1 = 100 + 80 * math.cos(angle)
                y1 = 100 - 80 * math.sin(angle)
                x2 = 100 + 90 * math.cos(angle)
                y2 = 100 - 90 * math.sin(angle)
                self.clock.create_line(x1, y1, x2, y2, width=2)
            self.hour_hand = self.clock.create_line(100, 100, 100, 60, width=4)
            self.minute_hand = self.clock.create_line(
                100, 100, 100, 20, width=2)

        def update_watch_face(self):
            now = time.localtime()
            hour_angle = (now.tm_hour % 12 + now.tm_min / 60) * math.pi / 6
            hour_x = 100 + 50 * math.sin(hour_angle)
            hour_y = 100 - 50 * math.cos(hour_angle)
            self.clock.coords(self.hour_hand, 100, 100, hour_x, hour_y)

            minute_angle = now.tm_min * math.pi / 30
            minute_x = 100 + 70 * math.sin(minute_angle)
            minute_y = 100 - 70 * math.cos(minute_angle)
            self.clock.coords(self.minute_hand, 100, 100, minute_x, minute_y)
            self.master.after(1000, self.update_watch_face)

    root = tk.Tk()
    root.title("Watch Face")
    watch_face = WatchFace(root)
    watch_face.update_watch_face()
    root.mainloop()


def clock():
    root = Tk()
    root.title('Clock')

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    # Styling the label widget so that clock will look more attractive
    lbl = Label(root, font=('calibri', 40, 'bold'),
                background='black',
                foreground='white')

    # Placing clock at the centre of the tkinter window
    lbl.pack(anchor='center')
    time()

    mainloop()


def gps():
    urlopen("http://ipinfo.io/json")
    data = json.load(urlopen("http://ipinfo.io/json"))
    lat = data['loc'].split(',')[0]
    lon = data['loc'].split(',')[1]
    return lat, lon, data


heart_rate = 72  # at resting
def hr_monitor():
    while True:
        if heart_rate > 130:
            exer = input("are you exercising ? y , n \n")
            if exer == "y":
                print("heart rate is :", heart_rate)
                break
            else:
                print("your heart rate is too high!! ", heart_rate, "\n")
                sos = input("SOS y , n ? \n")
                if sos == "y":
                    print("alerting emergency contacts ... ")
                    break
        elif heart_rate < 40:
            print("your heart rate is too low!! ", heart_rate, "\n")
            sos = input("SOS y , n \n")
            if sos == "y":
                print("alerting emergency contacts ... ")
                break
            break
        else:
            print("your heart rate is: ", heart_rate)
            break


begi_speed = 60  # assuming this speed in kmph

def acc_monitor(curr_speed):
    # let the current speed become 0 when the car is crashed, and time required for deceleration is assumed to be 0.5 seconds.

    crash_time = 0.5
    deceleration = 0
    while True:
        if deceleration >= (begi_speed - curr_speed)/crash_time:
            cra = input("did you experience a car crash ? y , n \n")
            if cra == "y":
                sos = input("SOS y , n ? \n")
                if sos == "y":
                    print("alerting emergency contacts ... ")
                    break
            else:
                break
        elif curr_speed < 10:
            print("crash not detected/not high deceleration for a crash")
            print("your current speed is: ", curr_speed)
            break


begi_lat, begi_lon, begi_data = gps()
begi_time = datetime.datetime.now()
print("starting smartwatch")
print("current location: ", begi_data["city"])
print("time of beginning: ", begi_time)

# here we are starting a thread so that the time can be displayed in a infinite loop.
# this is performed so that the watch can show time, while perfoming other functions.
watch = input(
    "would you like an analogue watch face or a digital watch? type 0 for analogue, 1 for digital \n")
if watch == "1":
    th = threading.Thread(target=clock)
    th.start()
elif watch == "0":
    th = threading.Thread(target=ana_watch)
    th.start()


print("\nplease select from the following mapping of features and buttons: \n g-> GPS \n d-> distance and related features \n s-> speed \n h-> heart rate monitor \n a-> accident detection \n c-> calculator \n t-> location temperature \n e-> to end the program.")
print("please remember to turn off the capslock")

while True:
    try:
        if keyboard.is_pressed('g'):
            time.sleep(0.5)
            print('You pressed the g key!')
            print("\nGPS")
            lat, lon, data = gps()
            print("the co-ordinates are as follows")
            print("latitude =", lat, " longitude = ", lon)
            print("current location: ", data["city"])
            print("\npress any other feature button")

        if keyboard.is_pressed('e'):
            time.sleep(0.5)
            # th_hr.join()
            print('\nYou pressed the e key!')
            print("ending simulation...")
            print("please close the watch tab")
            th.join()
            break

        if keyboard.is_pressed('d'):
            print('You pressed the d key!')
            print("\ndistance")
            lat, lon, data = gps()
            loc1 = (float(begi_lat), float(begi_lon))
            loc2 = (float(lat), float(lon))
            dist = hs.haversine(loc1, loc2, unit=Unit.METERS)
            print("the distance travelled: ", dist, " meters")
            step = dist/0.36576
            print("you average number of steps are :", step)
            print("number of calories burned is : ", 0.04*step)
            print("\npress any other feature button")

        if keyboard.is_pressed('s'):
            time.sleep(0.5)
            print('You pressed the s key!')
            print("\nspeed ")
            lat, lon, data = gps()
            loc1 = (float(begi_lat), float(begi_lon))
            loc2 = (float(lat), float(lon))
            dist = hs.haversine(loc1, loc2, unit=Unit.METERS)
            curr_time = datetime.datetime.now()
            speed = dist/((curr_time-begi_time).total_seconds())
            print("the speed is: ", speed, " meters per second")
            print("\npress any other feature button")

        if keyboard.is_pressed('h'):
            time.sleep(0.5)
            print('You pressed the h key!')
            hr_monitor()
            print("\npress any other feature button")

        if keyboard.is_pressed('a'):
            time.sleep(0.5)
            print('You pressed the a key!')
            print("\naccident detection")
            lat, lon, data = gps()
            loc1 = (float(begi_lat), float(begi_lon))
            loc2 = (float(lat), float(lon))
            dist = hs.haversine(loc1, loc2, unit=Unit.METERS)
            curr_time = datetime.datetime.now()
            speed = dist/((curr_time-begi_time).total_seconds())
            acc_monitor(speed)
            print("\npress any other feature button")

        if keyboard.is_pressed('c'):
            time.sleep(0.5)
            print('You pressed the c key!')
            print("\nCalculator")
            choice = input("Enter the expression : ")
            print(eval(choice))
            print("\npress any other feature button")

        if keyboard.is_pressed('t'):
            time.sleep(0.5)
            print('You pressed the t key!')
            print("\nTemperature")
            place = input("Enter the name of location : ")
            search = f"Weather in {place}"
            url = f"https://www.google.com/search?q={search}&oq={search}"

            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            update = soup.find("div", class_="BNeawe").text
            print(f"Temperature in {place} is {update}")
            print("\npress any other feature button")

    except:
        break

