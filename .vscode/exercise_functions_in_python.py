# Define and Implement Functions
def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow!")

def green_light():
    print("Green light - Go!")

# Create a Function to Control the Traffic Light and Handle Invalid States
def traffic_light(state):
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
        print("Invalid traffic light state! Please enter 'red', 'yellow', or 'green'.")

traffic_light("red")
traffic_light("yellow")
traffic_light("green")
traffic_light("black")


# alternate example
def sunny():
    print("It's sunny! Wear sunglasses and apply sunscreen.")

def rainy():
    print("It's rainy! Don't forget your umbrella.")

def snowy():
    print("It's snowy! Dress warmly and watch for ice.")

def weather_report(condition):
    if condition == "sunny":
        sunny()
    elif condition == "rainy":
        rainy()
    elif condition == "snowy":
        snowy()
    else:
        print("Unknown weather condition. Please enter 'sunny', 'rainy', or 'snowy'.")

weather_report("sunny")
weather_report("rainy")
weather_report("snowy")
weather_report("cloudy") 





