#!/bin/bash

sleep 10

function wifi_detect() {
	SSID=$(iwgetid -r)

	if [ "$SSID" == "RedNN" ]; then
		/home/user/Desktop/Proyecto1/ejecutor.sh
		echo "en el script" >> ~/Desktop/pruebasisi.txt
	fi
}

while true; do
	SSID_Actual=$(iwgetid -r)

	sleep 5

	SSID_Nueva=$(iwgetid -r)

	if [ "$SSID_Actual" != "$SSID_Nueva" ]; then
		wifi_detect
	fi
done