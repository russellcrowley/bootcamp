#!/usr/bin/env bash

# A script using twint to scrape various things from twitter, download dependencies installer from address below
# https://raw.githubusercontent.com/russellcrowley/bootcamp/main/twint_script_installer.sh

# Credit for menu:
# Written By Acon1tum 2021 as a BASH exercise - Original Menu Unknown and Butchered.


# Setting up your functions

function option1 { 
clear
echo "Option 1 - Search by user"
read -p "Which user would you like to see tweets for?  " user
twint -u $user
}

function option2 { 
clear
echo "Option 2 - Search by a keyword"
read -p "What do you want to search for? " keyword
twint -s $keyword
}

function option3 { 
clear
echo "Option 3 - What does Jack Dorsey think?"
twint -u jack
}

function option4 { 
clear
echo "Option 4"
}

function option5 { 
clear
echo "Option 5"
}

function option6 { 
clear
echo "Option 6"
}

function option7 { 
clear
echo "Option 7"
}

function option8 { 
echo "Option 8"
}

function option9 { 
clear
echo -e "\e[31mQuitting...\e[0m"
echo
sleep 2
clear
exit 1
}
clear


# Setting up title, change however you like it

echo "Welcome to" | lolcat
figlet "TWINT SCRIPT" | lolcat
echo "by Russ" | lolcat
echo
echo



#   Arguments   : list of options, maximum of 256
#                 "opt1" "opt2" ...


#   Return value: selected index (0 for opt1, 1 for opt2 ...)
function select_option {

    # little helpers for terminal print control and key input
    ESC=$( printf "\033")
    cursor_blink_on()  { printf "$ESC[?25h"; }
    cursor_blink_off() { printf "$ESC[?25l"; }
    cursor_to()        { printf "$ESC[$1;${2:-1}H"; }
    print_option()     { printf "   $1 "; }
    print_selected()   { printf "  $ESC[7m $1 $ESC[27m"; }
    get_cursor_row()   { IFS=';' read -sdR -p $'\E[6n' ROW COL; echo ${ROW#*[}; }
    key_input()        { read -s -n3 key 2>/dev/null >&2
                         if [[ $key = $ESC[A ]]; then echo up;    fi
                         if [[ $key = $ESC[B ]]; then echo down;  fi
                         if [[ $key = ""     ]]; then echo enter; fi; }

    # initially print empty new lines (scroll down if at bottom of screen)
    for opt; do printf "\n"; done

    # determine current screen position for overwriting the options
    local lastrow=`get_cursor_row`
    local startrow=$(($lastrow - $#))

    # ensure cursor and input echoing back on upon a ctrl+c during read -s
    trap "cursor_blink_on; stty echo; printf '\n'; exit" 2
    cursor_blink_off

    local selected=0
    while true; do
        # print options by overwriting the last lines
        local idx=0
        for opt; do
            cursor_to $(($startrow + $idx))
            if [ $idx -eq $selected ]; then
                print_selected "$opt"
            else
                print_option "$opt"
            fi
            ((idx++))
        done

        # user key control
        case `key_input` in
            enter) break;;
            up)    ((selected--));
                   if [ $selected -lt 0 ]; then selected=$(($# - 1)); fi;;
            down)  ((selected++));
                   if [ $selected -ge $# ]; then selected=0; fi;;
        esac
    done

    # cursor position back to normal
    cursor_to $lastrow
    printf "\n"
    cursor_blink_on

    return $selected
}


# Telling user what buttons to use to operate the menu - using escape characters 
echo -e "Use \e[91mUP\e[0m and \e[91mDOWN\e[0m arrows and \e[91mENTER\e[0m to confirm:"
echo

# Setting up menu items, change these as you wish
options=("User search" "Keyword search" "What does Jack Dorsey think?" "Option 4" "Option 5" "Option 6" "Option 7" "Option 8" "Exit")

select_option "${options[@]}"
choice=$?

echo "Choosen index = $choice"
echo "        value = ${options[$choice]}"


# Checking choice and firing the function off

if [[ $choice == 0 ]];then
option1

elif [[ $choice == 1 ]];then
option2

elif [[ $choice == 2 ]];then
option3

elif [[ $choice == 3 ]];then
option4

elif [[ $choice == 4 ]];then
option5

elif [[ $choice == 5 ]];then
option6

elif [[ $choice == 6 ]];then
option7

elif [[ $choice == 7 ]];then
option8

elif [[ $choice == 8 ]];then
option9




fi
