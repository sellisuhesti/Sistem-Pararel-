# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time
from datetime import datetime,date

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # print tema konser yang dipilih
    print("Tema Konser =",message.topic)
    data = message.payload.decode("utf-8")
    #mengubah string data menjadi tipe data datetime
    dt = datetime.strptime(data,"%d/%m/%y %H:%M")
    #print tanggal konser berupa hari, tanggal, bulan, tahun 
    print("tanggal :",dt.strftime("%A %d %B %Y"))
    #print waktu konser
    print("waktu   :",dt.strftime("%H:%M"))
    
    
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address="192.168.43.22"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("Antonio")

# kaitkan callback on_message ke client
client.on_message=on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
print("Subscribing to topic")
#client subscribe topik girlband
client.subscribe("girlband")
#client subscribe topi korean ballad
client.subscribe("Korean Ballad")
time.sleep(1)
#stop loop
client.loop_stop()
