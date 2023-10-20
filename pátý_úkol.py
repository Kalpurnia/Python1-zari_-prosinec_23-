teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

average_temp = [(sum(day)/len(day)) for day in teploty]
print (average_temp)

morning_temp = [day[0] for day in teploty]
print (morning_temp)

night_temp = [day[3] for day in teploty]
print (night_temp)

noon_night_temp = [day[1:4:2] for day in teploty]
print (noon_night_temp)

# Bonus 
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

days = [{day[0]: day[1:]} for day in teploty]
print(days)

day_average = [{day[0]:(sum(day[1:])/(len(day)-1))} for day in teploty]
print (day_average)

