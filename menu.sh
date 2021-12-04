#!/bin/bash

figlet "Amazing Menu"
echo
read -p "Select a number between 1 and 3   " number 
echo $number
echo
if [ $number -eq 1 ]; then
	echo "You have pressed 1"
elif [ $number -eq "2" ]; then
	echo "You have pressed 2"
elif [ $number -eq "3" ]; then
	figlet "You have pressed 3"
else
	echo "You did not enter a number between 1 and 3. You have failed the test";
fi
