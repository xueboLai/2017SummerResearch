#Author: Xuebo Lai
from selenium import webdriver
from depot.manager import DepotManager
import time
import schedule
from datetime import datetime
import os
#multi-armed bandit


def screenshot(website,output):
    depot = DepotManager.get()
    #self.browser = webdriver.Firefox(executable_path='/Users/xuebolai/Downloads/p/bin/phantomjs')
    driver = webdriver.PhantomJS(executable_path="/Users/xuebolai/Downloads/p/bin/phantomjs")
    driver.set_window_size(2000,1000)
    driver.get(website)
    driver.save_screenshot(output)
	driver.quit()
    print("screenshot end, the name is "+output)
    

def iterative_screenshot(time_between,total_time,web1,web2,web3):
    current = 0;
    counter = 0;
    directory = (datetime.today().strftime("%m_%d_%Y"))
    os.makedirs(directory)
    os.chdir(directory)
    os.makedirs("output1")
    os.makedirs("output2")
    os.makedirs("output3")
    while(current<=total_time):
        print("iternation "+str(counter))
        print("current time is "+str(datetime.time(datetime.now())))
        start_time = time.time()
        #output 1
        output1 = "output1/googleMap"+str(count_num)+".png"
        screenshot(web1,output1)
        #output 2
        output2 = "output2/googleMap"+str(count_num)+".png"
        screenshot(web2,output2)
        #output 3
        output3 = "output3/googleMap"+str(count_num)+".png"
        screenshot(web3,output3)
        #end of ouput
        current+=(time_between)
        counter+=1
        print("iteration ended ")
        program_time = time.time()-start_time
        print("program took "+str(program_time)+" to finish\nwaiting for "+str(time_between)+" second now")
        time.sleep((time_between-float(str(program_time))))
        print("wait ends ")
        print("\n\n")

def bridge(web1,web2,web3):
    global count_num
    print("iternation "+str(count_num))
    print("current time is "+str(datetime.time(datetime.now())))
    #output 1
    output1 = "output1/googleMap"+str(count_num)+".png"
    screenshot(web1,output1)
    #output 2
    output2 = "output2/googleMap"+str(count_num)+".png"
    screenshot(web2,output2)
    #output 3
    output3 = "output3/googleMap"+str(count_num)+".png"
    screenshot(web3,output3)
    count_num+=1
    
    

def main():
    #time.sleep(3.5)
    global count_num
    count_num=0
    web1 = "https://www.google.com/maps/dir/Times+Square,+Manhattan,+NY/John+F.+Kennedy+International+Airport/@40.7120539,-73.9010844,12z/data=!4m69!4m68!1m60!1m1!1s0x89c25855c6480299:0x55194ec5a1ae072e!2m2!1d-73.985131!2d40.758895!3m4!1m2!1d-73.9864397!2d40.7558224!3s0x89c25854d200669b:0x7f42170059ececdf!3m4!1m2!1d-73.9808766!2d40.7534847!3s0x89c2590038a9c50b:0x44cf32e120ce0598!3m4!1m2!1d-73.9734128!2d40.7481999!3s0x89c259049abe9147:0x42cfc5178231973b!3m4!1m2!1d-73.9736246!2d40.7457584!3s0x89c25905054cf853:0x9d5dc04c3b521bad!3m4!1m2!1d-73.9433668!2d40.7400844!3s0x89c2592fd19a3775:0xce854cff8c963c52!3m4!1m2!1d-73.9281232!2d40.7364055!3s0x89c25ece3fc9b01b:0xf8114e768d5586bd!3m4!1m2!1d-73.9170186!2d40.7312327!3s0x89c25ec409bce11d:0x2668e1902cee8b95!3m4!1m2!1d-73.8879406!2d40.7273407!3s0x89c25e58ae0e363d:0xd73853baa75dfcda!3m4!1m2!1d-73.8634306!2d40.7342127!3s0x89c25e35b6254d19:0x3a6e34284161f14!3m4!1m2!1d-73.8362831!2d40.722823!3s0x89c2609c9eea6785:0x4481e294e6b22354!3m4!1m2!1d-73.8080731!2d40.6872121!3s0x89c2673242d034d1:0x8fd23d5e555fd116!1m5!1m1!1s0x89c26650d5404947:0xec4fb213489f11f0!2m2!1d-73.7781391!2d40.6413111!3e0?hl=en&authuser=0"
    web2 = "https://www.google.com/maps/dir/Times+Square,+Manhattan,+NY/John+F.+Kennedy+International+Airport+(JFK),+Queens,+NY+11430/@40.7064812,-73.9525828,12z/data=!3m1!4b1!4m59!4m58!1m50!1m1!1s0x89c25855c6480299:0x55194ec5a1ae072e!2m2!1d-73.985131!2d40.758895!3m4!1m2!1d-73.9734633!2d40.750354!3s0x89c2590308fffd17:0xffa8bd45d36e4f23!3m4!1m2!1d-73.9736107!2d40.7479306!3s0x89c259049abe9147:0x42cfc5178231973b!3m4!1m2!1d-73.9451672!2d40.740724!3s0x89c2592fd19a3775:0xce854cff8c963c52!3m4!1m2!1d-73.9176724!2d40.7352815!3s0x89c25ec359bb705f:0xe434f159a0bf63c5!3m4!1m2!1d-73.8987564!2d40.7597248!3s0x89c25f0dc1c1f071:0xfabf229c30537412!3m4!1m2!1d-73.870657!2d40.7712999!3s0x89c25f8e80be7757:0x28ccd3d86f307ebe!3m4!1m2!1d-73.8532245!2d40.7555381!3s0x89c25fdd520f3ee7:0xfa304b5b47ec1cd6!3m4!1m2!1d-73.8402667!2d40.729433!3s0x89c26081fa599105:0x45dade361663ace3!3m4!1m2!1d-73.8092772!2d40.6893551!3s0x89c267332c5db3a7:0x1048c1ecdee7683a!1m5!1m1!1s0x89c26650d5404947:0xec4fb213489f11f0!2m2!1d-73.7781391!2d40.6413111!3e0?hl=en&authuser=0"
    web3 = "https://www.google.com/maps/dir/Times+Square,+Manhattan,+NY/John+F.+Kennedy+International+Airport/@40.7420911,-73.9312307,11z/data=!4m59!4m58!1m50!1m1!1s0x89c25855c6480299:0x55194ec5a1ae072e!2m2!1d-73.985131!2d40.758895!3m4!1m2!1d-73.9734!2d40.7536802!3s0x89c25902829bd291:0x5b376b4f3a6295af!3m4!1m2!1d-73.9627392!2d40.7541223!3s0x89c258e1ad937c7d:0xb2a13c43aa454ef8!3m4!1m2!1d-73.9400043!2d40.7854193!3s0x89c258aa814495db:0x72a34ace0159d3b0!3m4!1m2!1d-73.9255476!2d40.791177!3s0x89c2f5fa1b666e4f:0x8f7179f80a3d58c4!3m4!1m2!1d-73.9182795!2d40.7710935!3s0x89c25f440ee21991:0xf502860a95dcdd74!3m4!1m2!1d-73.8824711!2d40.768555!3s0x89c25f9b7dd7f5c9:0x3679483fdd449cd3!3m4!1m2!1d-73.860086!2d40.762212!3s0x89c25fec0ede6dd5:0x548615591dc7024c!3m4!1m2!1d-73.8472357!2d40.744474!3s0x89c25fda0120111b:0x402084433d61d355!3m4!1m2!1d-73.8371843!2d40.7242374!3s0x89c2609cb0f81955:0x1c667cfadeed9602!1m5!1m1!1s0x89c26650d5404947:0xec4fb213489f11f0!2m2!1d-73.7781391!2d40.6413111!3e0?hl=en&authuser=0"
    schedule.every().day.at("08:00").do(iterative_screenshot,300,43200,web1,web2,web3)
    #iterative_screenshot(300,1200,web1,web2,web3)
    #time.sleep()
    while True:
        schedule.run_pending()
        #time.sleep(1)
main()
