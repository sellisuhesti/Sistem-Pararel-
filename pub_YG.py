# import paho mqtt
import paho.mqtt.client as mqtt
# import datetime untuk mendapatkan waktu dan tanggal
from datetime import datetime, date
# import time untuk sleep()
import time

# definisikan nama broker yang akan digunakan
broker_address="192.168.43.22"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("YG")
# koneksi ke broker
print("connecting to broker")
client.connect(broker_address,port=3333)

# mulai loop client
client.loop_start()

print("publish something")
for i in range(20):
    # sleep 1.5 detik
    time.sleep(1.5)
    #Publish jadwal konser pada tanggal 21 bulan September tahun 2020
    #pada waktu 19.00 PM
    dt="21/9/20 19:00";
    #SM mempublish jadwal konser bertema "girl band"
    client.publish("girlband",dt)

#stop loop
client.loop_stop()
