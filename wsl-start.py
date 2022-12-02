import os
import time

print("""
                   __                          __        __                 
                  /  |                        /  |      /  |                
  ______         _$$ |_     ______    ______  $$ |      $$ |____   __    __ 
 /      \       / $$   |   /      \  /      \ $$ |      $$      \ /  |  /  |
 $$$$$$  |      $$$$$$/   /$$$$$$  |/$$$$$$  |$$ |      $$$$$$$  |$$ |  $$ |
 /    $$ |        $$ | __ $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |
/$$$$$$$ |        $$ |/  |$$ \__$$ |$$ \__$$ |$$ |      $$ |__$$ |$$ \__$$ |
$$    $$ |        $$  $$/ $$    $$/ $$    $$/ $$ |      $$    $$/ $$    $$ |
 $$$$$$$/          $$$$/   $$$$$$/   $$$$$$/  $$/       $$$$$$$/   $$$$$$$ |
                                                                  /  \__$$ |
                                                                  $$    $$/ 
                                                                   $$$$$$/  
 __       __    __     ______    ______    ______                           
/  \     /  | _/  |   /      \  /      \  /      \                          
$$  \   /$$ |/ $$ |  /$$$$$$  |/$$$$$$  |/$$$$$$  |                         
$$$  \ /$$$ |$$$$ |  $$$  \$$ |$$$  \$$ |$$$  \$$ |                         
$$$$  /$$$$ |  $$ |  $$$$  $$ |$$$$  $$ |$$$$  $$ |                         
$$ $$ $$/$$ |  $$ |  $$ $$ $$ |$$ $$ $$ |$$ $$ $$ |                         
$$ |$$$/ $$ | _$$ |_ $$ \$$$$ |$$ \$$$$ |$$ \$$$$ |                         
$$ | $/  $$ |/ $$   |$$   $$$/ $$   $$$/ $$   $$$/                          
$$/      $$/ $$$$$$/  $$$$$$/   $$$$$$/   $$$$$$/
""")
time.sleep(2)
print("Terminal cleaning.")
time.sleep(0.3)
print("Terminal cleaning..")
time.sleep(0.3)
print("Terminal cleaning...")
time.sleep(1)
os.system("clear")
print("Changing nameserver.")
time.sleep(0.2)
print("Changing nameserver..")
time.sleep(0.2)
print("Changing nameserver...")
time.sleep(0.7)
os.system('echo "nameserver 8.8.8.8" | tee /etc/resolv.conf')
print("Nameserver has successfull changed")
time.sleep(1)
os.system("clear")
os.system("cd /home/kali/")
print("You are now")
os.system("whoami")
print("Happy Hacking!")
os.system("sudo su")
