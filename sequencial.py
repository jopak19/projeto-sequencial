import time
import requests

URL = "https://dummyjson.com/products"
cenarios = [10, 100, 200, 500, 1000]
resultados = open("resultados-sequencial.csv", "a")
resultados.write("Executions,TimeMillis,Category,Scenery\n")


for cenario in cenarios:
    for teste in range(20):
        startTime = int(time.time() * 1000)
        for req in range(cenario):
            requests.get(URL)
        endTime = int(time.time() * 1000)
        duration = endTime - startTime
        print("cenario: "+ str(cenario) + " teste: " + str(teste) + " duraçao: " + str(duration))        
        resultados.write(str(cenario) + ',' + str(duration) + "," + "sequencial" + "," + str(cenarios.index(cenario)) + "\n")


resultados.close()