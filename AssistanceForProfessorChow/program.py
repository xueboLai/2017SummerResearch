from random import *
import json
import urllib
import json
import urllib.request
import codecs
import time
import signal

def handler(signum, frame):
    print ("do nothing")



def main():
    print("program starts:\n")
    #define the highway locations for North, East, South, West as array
    #For North:(0)
    #start_north_x(y)[0]:40.793164, -73.824123;To South 678
    #end_north_x(y)[0]:40.793551, -73.824226; To North 678
    #start_north_x(y)[1]:40.793994, -73.793477; To South 295
    #end_north_x(y)[1]: 40.794014, -73.793346; to North 295
    start_north_x=[40.793164,40.793994]
    start_north_y=[-73.824123,-73.793477]
    end_north_x=[40.793551,40.794014]
    end_north_y=[-73.824226,-73.793346]
    north = {"direction":"north","x_start":start_north_x,"y_start":start_north_y,"x_end":end_north_x,"y_end":end_north_y}

    #For East:(1)
    #start_east_x(y)[0]:40.760452, -73.732523; to west Long Island Expy;
    #end_east_x(y)[0]:40.760346, -73.732429; to east Long Island Expy;
    #start_east_x(y)[1]:40.752295, -73.725982; to west Grand Central Pkwy
    #end_east_x(y)[1]:40.752161, -73.725848; to east Grand Central Pkwy
    start_east_x=[40.760452,40.752295]
    start_east_y=[-73.732523,-73.725982]
    end_east_x=[40.760346,40.752161]
    end_east_y=[-73.732429,-73.725848]
    east = {"direction":"east","x_start":start_east_x,"y_start":start_east_y,"x_end":end_east_x,"y_end":end_east_y}

    #For South:(2)
    #start_south_x(y)[0]:40.709607, -73.820145; To north Van Wyck Expy
    #end_south_x(y)[0]:40.709601, -73.820420; To South Van Wyck Expy
    #start_south_x(y)[1]:40.719537, -73.726204; to north Cross Island Pkwy
    #end_south_x(y)[1]:40.719579, -73.726351; to south Cross Island Pkwy
    start_south_x=[40.709607,40.719537]
    start_south_y=[-73.820145,-73.726204]
    end_south_x=[40.709601,40.719579]
    end_south_y=[-73.820420,-73.726351]
    south = {"direction":"south","x_start":start_south_x,"y_start":start_south_y,"x_end":end_south_x,"y_end":end_south_y}

    #For West(3)
    #start_west_x(y)[0]:40.768912, -73.910238; to east 278
    #end_west_x(y)[0]:40.769205, -73.910147; to west 278
    #start_west_x(y)[1]:40.725781, -73.900702; to east 495
    #end_west_x(y)[1]:40.725919, -73.900669; to east 495
    start_west_x=[40.768912,40.725781]
    start_west_y=[-73.910238,-73.900702]
    end_west_x=[40.769205,40.725919]
    end_west_y=[-73.910147,-73.900669]
    west = {"direction":"west","x_start":start_west_x,"y_start":start_west_y,"x_end":end_west_x,"y_end":end_west_y}

    #all defined here is fixed for the url
    key = "key=AIzaSyDyZhD_n3gX8tMOOj4_Mk6kZ1eJ8MURgv8"
    prefix = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    mode = "mode=driving&"
    depart_time = "departure_time=now&"
    lang = "language=en&"
    #mode=driving&departure_time=now&language=en&key=AIzaSyDyZhD_n3gX8tMOOj4_Mk6kZ1eJ8MURgv8
    
    #regular.csv stores all the routes' time; while best.cvs only stores the best route
    file_regular = open("regular.csv","w")
    file_best = open("best.csv","w")
    
    #make sure it runs 36 times; 12 times an hour, run for 3 hours
    counter = 0
    signal.signal(signal.SIGINT, handler)
    while(counter<36):#need to set to 36
        signal.signal(signal.SIGINT, handler)
        reader = codecs.getreader("utf-8")
        random_dir1 = randint(0,3)
        random_dir2 = randint(0,3)
        while(random_dir2==random_dir1):
            random_dir2 = randint(0,3)
        #direction list
        dir_lst = [north,east,south, west]
        dir_1 = dir_lst[random_dir1]
        dir_2 = dir_lst[random_dir2]
        #printing out all the output to make sure it's correct
        print("This is "+str(counter)+" iteration")
        print("The random numbers for direction generated is "+str(random_dir1)+" and "+str(random_dir2)+"")
        print("The first direction is "+dir_1["direction"]+"")
        print("The cordinate are ("+str(dir_1["x_start"][0])+","+str(dir_1["y_start"][0])+") "+"("+str(dir_1["x_start"][1])+","+str(dir_1["y_start"][1])+")")
        print("The second direction is "+dir_2["direction"]+"")
        print("The cordinate are ("+str(dir_2["x_end"][0])+","+str(dir_2["y_end"][0])+") "+"("+str(dir_2["x_end"][1])+","+str(dir_2["y_end"][1])+")")
        origin = "origins="+str(dir_1["x_start"][0])+","+str(dir_1["y_start"][0])+"|"+str(dir_1["x_start"][1])+","+str(dir_1["y_start"][1])+"&"
        destination = "destinations="+str(dir_2["x_end"][0])+","+str(dir_2["y_end"][0])+"|"+str(dir_2["x_end"][1])+","+str(dir_2["y_end"][1])+"&"
        #print(origin+"\n"+destination)
        print("start url:")
        merge = prefix+origin+destination+mode+depart_time+lang+key
        print("The url is: "+merge)
        #upload the url and obtain the json format data back
        answer = json.load(reader(urllib.request.urlopen(merge)))
        #writing into the file
        #process destination name to avoid special character
        file_regular.write("This is the "+str(counter)+" run")
        file_regular.write(",")
        dest1=answer["destination_addresses"][0]
        dest2=answer["destination_addresses"][1]
        dest1 = dest1.replace(", ","_")
        dest2 = dest2.replace(", ","_")
        dest1 = dest1.replace(" ","_")
        dest2 = dest2.replace(" ","_")
        file_regular.write(dest1+",")
        file_regular.write(dest2+"\n")
        #provess departure name to avoid special character
        org1=answer["origin_addresses"][0]
        org2=answer["origin_addresses"][1]
        org1 = org1.replace(", ","_")
        org2 = org2.replace(", ","_")
        org1 = org1.replace(" ","_")
        org2 = org2.replace(" ","_")
        file_regular.write(org1+",")
        
        file_regular.write(str(answer["rows"][0]["elements"][0]["duration_in_traffic"]["value"])+",")
        file_regular.write(str(answer["rows"][0]["elements"][1]["duration_in_traffic"]["value"])+"\n")
        file_regular.write(org2+",")
        file_regular.write(str(answer["rows"][1]["elements"][0]["duration_in_traffic"]["value"])+",")
        file_regular.write(str(answer["rows"][1]["elements"][1]["duration_in_traffic"]["value"])+"\n")
        file_regular.write("\n\n")
        
        final_lst = [answer["rows"][0]["elements"][0]["duration_in_traffic"]["value"],answer["rows"][0]["elements"][1]["duration_in_traffic"]["value"],answer["rows"][1]["elements"][0]["duration_in_traffic"]["value"],answer["rows"][1]["elements"][1]["duration_in_traffic"]["value"]]
        minimum = min(final_lst)
        min_index = final_lst.index(min(final_lst))
        
        #output to the best result
        file_best.write("This is the "+str(counter)+" run \n")
        print("\nbest run")
        if min_index<=1:
            print("original_address,"+org1+"\n")
            file_best.write("original_address,"+org1+"\n")
            if min_index==0:
                print("destination_address,"+dest1+"\n")
                file_best.write("destination_address,"+dest1+"\n")
            else:
                print("destination_address,"+dest2+"\n")
                file_best.write("destination_address,"+dest2+"\n")
        else:
            print("original_address,"+org2+"\n")
            file_best.write("original_address,"+org2+"\n")
            if min_index==2:
                print("destination_address,"+dest1+"\n")
                file_best.write("destination_address,"+dest1+"\n")
            else:
                print("destination_address,"+dest2+"\n")
                file_best.write("destination_address,"+dest2+"\n")
        print("time(in second),"+str(minimum)+"\n")
        file_best.write("time(in second),"+str(minimum)+"\n")
        file_best.write("\n\n")

        print("\n\n\n")
        counter = counter+1
        time.sleep(300)
        
        #another way of reading json file
        #data = access_web.read()
        #encoding = access_web.info().get_content_charset('utf-8')
        #answer = json.loads(data.decode(encoding))
        #print(answer)
        
main()        
        
        
    
    

    
    
    
    
    
    
    
    
