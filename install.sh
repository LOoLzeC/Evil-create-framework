#!/usr/bin/bash
# -*- coding: utf-8 -*-
#coded by deray
clear
echo "\033[1;37m \033[31m"
echo "   VCRT INSTALLER!"
echo 
echo "\033[31m(1) \033[1;34mkali linux/debian/other"
echo "\033[31m(2) \033[1;34mtermux"
echo "\033[31m(3)\033[1;34m gnuroot debian"
echo "\033[31m(4)\033[1;34m pydroid? hmm"
echo "\033[31m(0)\033[1;34m BYE BITCHH!!"
echo
echo "\033[1;37mChoose your distro \033[1;37m>"
read choose

if [ $choose = "01" ] || [ $choose = "1" ];
then
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
sudo apt-get install git
echo
echo "\033[31m[!]\033[1;37m virus creator was installed!"
sleep 2
python2 vcrt.py
exit

elif [ $choose = "02" ] || [ $choose = "2" ];
then
apt-get update
apt-get upgrade
pkg install python2
pkg install git
echo
echo "\033[31m[!] \033[1;37mvirus creator was installed!"
sleep 2
python2 vcrt.py
exit

elif [ $choose = "03" ] || [ $choose = "3" ];
then
apt-get update
apt-get upgrade
apt-get install python-pip
apt-get install git
echo
echo "\033[31m[!] \033[1;37mvirus creator was installed!"
sleep 2
python2 vcrt.py
exit

elif [ $choose = "04" ] || [ $choose = "4" ];
then
python vcrt.py
exit

elif [ $choose = "00" ] || [ $choose = "0" ];
then
echo
echo "Bye!"
echo
exit

else
echo
echo "[!] Wrong Input..!"
echo
fi
