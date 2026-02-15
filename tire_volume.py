"""
W01 Project: Tire Volume
Enhancement:
After calculating the tire volume, the program asks the user if they want
to buy tires. If yes, it collects their phone number and stores it in the log.
"""

import math
from datetime import datetime


def main():
    
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

   
    volume = (math.pi * width**2 * aspect_ratio *
              (width * aspect_ratio + 2540 * diameter)) / 10000000000

   
    print(f"The approximate volume is {volume:.2f} liters")

    
    current_date = datetime.now()

   
    buy = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

    phone = ""
    if buy == "yes":
        phone = input("Enter your phone number: ")

    
    with open("volumes.txt", "at") as file:
        if phone:
            print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}",
                  file=file)
        else:
            print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}",
                  file=file)


if __name__ == "__main__":
    main()
