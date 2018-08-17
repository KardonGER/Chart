import os
import machine
import dht

d = dht.DHT11()

d.measure()
temp = d.temperature()
hum = d.humidity()

print temp
print hum

sleep(3000)
