import bluetooth
import serial
import time

# ターゲットデバイスのMACアドレスとポート
target_address = "00:04:3E:84:12:00"
port = 1  # RFCOMMの一般的なポート番号

# Bluetooth接続
print(f"Connecting to {target_address} on port {port}...")
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))
print("Connected successfully!")

# シリアル通信の設定
serial_port = "/dev/tty.OBDLinkMX93244"
baud_rate = 38400  # 通常のボーレート。デバイスによって異なる場合は調整してください
ser = serial.Serial(serial_port, baud_rate, timeout=50)

# デバイスからデータを読み取り
try:
    while True:
        # Bluetoothからデータを受信
        data = sock.recv(1024)  # 1024バイトまで受信
        if data:
            print(f"Received: {data.decode('utf-8')}")

        # シリアルポートにデータを送信
        ser.write(data)
        print(f"Sent to serial: {data.decode('utf-8')}")

        # シリアルポートからデータを読み取り、Bluetoothに送信
        if ser.in_waiting > 0:
            serial_data = ser.read(ser.in_waiting)
            print(f"Received from serial: {serial_data.decode('utf-8')}")
            sock.send(serial_data)
        
        time.sleep(0.5)  # 短い待機時間を入れる

except KeyboardInterrupt:
    print("Connection closed.")
    sock.close()
    ser.close()
