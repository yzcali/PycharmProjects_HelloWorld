# question2
# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70),
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

def speed(s):
    d = 0
    if s <= 70:
        return "ok"
    if s >= 130 or d >= 12:
        return "License suspended"
    if s >= 75 and s % 5 == 0:
        d += ((s - 75) / 5) + 1
        return f"Points: {d}"


print(speed(185))
