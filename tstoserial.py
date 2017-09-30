import ts3
import serial
import time

ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)
time.sleep(2) # waits for arduino to boot up
print(ser.readline().decode('ascii')) # gets handshake message from arduino
#time.sleep(2)
with ts3.query.TS3Connection("jewishwarriorsinc.typefrag.com") as ts3conn:
    online_users = []
    ts3conn.use(port=5670)
    ts3conn.login(client_login_name="Admin", client_login_password="xCYqhkr9")
    ts3conn.use(port=5670)
    resp = ts3conn.clientlist()
    for client in resp.parsed:
        if ':' not in client['client_nickname']:
            print(client['client_nickname'])
            mes = client['client_nickname']
            data = bytes(mes, "ascii", errors='ignore')
            ser.write(data + b' ')

    ser.close()
