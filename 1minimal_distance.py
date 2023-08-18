import pandas as pd
import numpy as np

cities = {
    #DONE
    "Абердин":{
        "Абердин":None,
        "Эдинбург":120,
        "Форт":147,
        "Глазго":142,
        "Инвернесс":107,
        "Перт":81
    },
    #DONE
    "Эдинбург":{
        "Абердин":120,
        "Эдинбург":None,
        "Форт":132,
        "Глазго":42,
        "Инвернесс":157,
        "Перт":45
    },
    #DONE
    "Форт":{
        "Абердин":147,
        "Эдинбург":132,
        "Форт":None,
        "Глазго":108,
        "Инвернесс":66,
        "Перт":105
    },
    #DONE
    "Глазго":{
        "Абердин":142,
        "Эдинбург":42,
        "Форт":108,
        "Глазго":None,
        "Инвернесс":168,
        "Перт":61
    },
    #DONE
    "Инвернесс":{
        "Абердин":107,
        "Эдинбург":157,
        "Форт":66,
        "Глазго":168,
        "Инвернесс":None,
        "Перт":112
    },
    #DONE
    "Перт":{
        "Абердин":81,
        "Эдинбург":45,
        "Форт":105,
        "Глазго":61,
        "Инвернесс":112,
        "Перт":None
    },
}
data_min_distance = {

}

for city_name,y in cities.items():
    #print(f"FOR {city_name}")
    #Set the city name
    min_distance = 0
    last_city_name = ""
    for i in y:
        if (y[i] != None and min_distance == 0):
            min_distance = y[i]
        if (y[i] != None and y[i] < min_distance):
            min_distance = y[i]
            last_city_name = i
        #print(i,y[i])
    data_min_distance[city_name] = {
        last_city_name:min_distance
    }
    #print(city_name,y)
    #print(f"Min dist: ",min_distance)
    #print("____")
    #print("____")
print(data_min_distance)
#TODO: Upload to GitHub Private Disc Math

