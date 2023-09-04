# Bosswerk MI300

The [official Website](https://www.bosswerk.de/mikrowechselrichter/) of the Inverter

# Most data protection friendly setup

## German / Deutsch
Auf das Webinterface kann direkt zugegriffen werden ohne dafür die App SolarWorls installieren zu müssen.

1. Seriennummer (SN) XXXXXXXXXX auf der Rückseite des Wechselrichters notieren
2. Seriennummer an die Zeichen `AP_` zur SSID des WLANS zusammensetzen, woraus sich `AP_XXXXXXXXXX` ergibt
3. In den Wlan einstellungen eines Gerätes eine neue Verbindung hinzufügen, bestehtend aus SSID und Passwort=12345678
4. Im Browser http://10.10.100.254 aufrufen um das Webinterface zu erreichen. Nutzer=`admin`, Password=`admin` 


## WLAN Verbindung auf Gerät konfigurieren
### Windows

Settings > WIFI > Manage known networks > add a new Network

SSID und Password eingeben, Security Type = `WPA2-Personal AES`