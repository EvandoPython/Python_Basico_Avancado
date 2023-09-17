vel = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if vel > RADAR_1:
    print('Velocidade carro passou do radar 1')
 
if local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_1) and vel > RADAR_1:
    print("Carro multado no radar 1")
 
     
    