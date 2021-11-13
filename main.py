import os
import time
import random
import sys
import string
import requests
import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner(colors) :
    os.system("cls")
    if colors == True : 
        print(bcolors.HEADER + "###################################" + bcolors.ENDC)
        print(bcolors.HEADER + "# Random Discord Invite Generator #" + bcolors.ENDC)
        print(bcolors.HEADER + "###################################" + bcolors.ENDC)
    else :
        print("###################################")
        print("# Random Discord Invite Generator #")
        print("###################################")
    print(" ")
    print(" ")
    print(" ")

def write_good_file(dc_invite, today) :
    with open(today+"/good.txt", "a") as c :
        c.write(dc_invite)
        c.write("\n")
        c.close()

def write_bad_file(dc_invite, today) :
    with open(today+"/bad.txt", "a") as c :
        c.write(dc_invite)
        c.write("\n")
        c.close()

def check(invite_str, today, show_bad, write_bad, show_timeout, colors) :
    apilink = "https://discord.com/api/v8/invites/" + invite_str

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}

    resp = requests.get(apilink, headers=headers)
    resp = str(resp)

    if "404" in resp :
        dc_invite = "https://discord.gg/" + invite_str

        if show_bad == True :
            if colors == True :
                print(bcolors.FAIL + "[-] Found an invalid invite..." + bcolors.ENDC)
            else :
                print("[-] Found an invalid invite...")

        if write_bad == True :
            write_bad_file(dc_invite, today)

        generation(today, show_bad, write_bad, show_timeout, colors)

    elif "200" in resp :
        dc_invite = "https://discord.gg/" + invite_str

        if colors == True :
            print(bcolors.OKGREEN + "[+] Found a valid discord invite ! : " + dc_invite + bcolors.ENDC)
        else :
            print("[+] Found a valid discord invite ! : ")

        write_good_file(dc_invite, today)
        generation(today, show_bad, write_bad, show_timeout, colors)
    elif "429" in resp :

        if show_timeout == True :
            if colors == True :
                print(bcolors.WARNING + "[-] Requests limit reached, sleeping for 22.668 secondes..." + bcolors.ENDC)
            else :
                print("[-] Requests limit reached, sleeping for 22.668 secondes...")

        time.sleep(22.668)
        generation(today, show_bad, write_bad, show_timeout, colors)
    else :
        print(resp)
        print(invite_str)
        sys.exit()
        


def generation(today, show_bad, write_bad, show_timeout, colors) :
    a = 0
    invite = [" "," "," "," "," "," "," "]

    while a != 7 :
        choice = random.randint(0,1)

        if choice == 0 :
            invite[a] = random.randint(0,9)
        
        elif choice == 1 :
            invite[a] = random.choice(string.ascii_letters)
        
        a = a + 1
    
    invite_str = ''.join(str(e) for e in invite)
    check(invite_str, today, show_bad, write_bad, show_timeout, colors)


def main() :
    try :
        os.system("cls")
        os.system("title Random Discord Invite Generator")

        colors = input("Do you want to have colored lines ? y/n ")
        if colors == "y" :
            colors = True
        else :
            colors = False

        banner(colors)

        if colors == True :
            show_timeout = input(bcolors.WARNING + "Show a message when sleeping after the requests limit ? y/n ")
        else :
            show_timeout = input("Show a message when sleeping after the requests limit ? y/n ")
        if show_timeout == "y" :
            show_timeout = True
        else :
            show_timeout = False

        show_bad = input("Show a message when an invalid discord invite is found ? y/n ")
        if show_bad == "y" :
            show_bad = True
        else :
            show_bad = False

        write_bad = input("Write the bad invites into bad.txt ? y/n ")
        if write_bad == "y" :
            write_bad = True
        else :
            write_bad = False

        if colors == True :
            enter = input(bcolors.OKGREEN + "Press [ENTER] to start the generation...")
        else :
            enter = input("Press [ENTER] to start the generation...")
        print("Starting in 5 sec...")
        if colors == True :
            print("Press CTRL+C to stop" + bcolors.ENDC)
        else :
            print("Press CTRL+C to stop")
        time.sleep(5)
        banner(colors)
        today = datetime.datetime.now()
        today = str(today)
        today = today.replace(":", "-")
        today = today.replace(" ", "_")
        os.system("mkdir "+today)
        generation(today, show_bad, write_bad, show_timeout, colors)
    except KeyboardInterrupt :
        print(" ")
        if colors == True :
            print(bcolors.WARNING + "Keyboard Interrupt detected !")
            print("See you next time !" + bcolors.ENDC)
        else :
            print("Keyboard Interrupt detected !")
            print("See you next time !")
        os.system("pause")

main()
    
