import json
import urllib
import json
import urllib.request
import codecs
import time
#def geo(address,geo_args):


def open_file(fileName):
    li_x = []
    file = open(fileName,"r")
    for line in file:
        lst = line.split(",")
        li_x.append(lst[2])
        li_x.append(lst[1])
    file.close()
    return li_x

#def read_file()


def main():
    print("converting to cvs file")
    lst = open_file("zip_summary.csv")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    #key = "AIzaSyDyZhD_n3gX8tMOOj4_Mk6kZ1eJ8MURgv8"
    key = "AIzaSyDV-aAQfBxSi4Emh0j6UWaqf-tbBrqhSIs"
    #origin = "origins="+str(x1)+','+str(y1)+"|"+str(x3)+','+str(y3)
    #destination = "destinations="+str(x2)+","+str(y2)+"|"+str(x4)+","+str(y4)
    origin = "origins="
    destination = "destinations="
    between=""
    outputFile = open("output2.csv","a")
    for index in range(0,200):#change to 200 in future
        one_row = []
        actual_index = index*2
        origin_local = origin+lst[actual_index]+","+lst[(actual_index+1)]
        #print (origin_local)
        counter = 0;
        for index2 in range(0,20):#chagne to 20 in future
            destination_local = destination
            for index3 in range(0,10):# every 10 elements in row:
                if index3 < 9:
                    real_index = counter*2
                    destination_local += lst[real_index]+","+lst[(real_index+1)]+"|"
                    counter+=1
                else:
                    real_index = counter*2
                    destination_local += lst[real_index]+","+lst[(real_index+1)]
                    counter+=1
            final = url+origin_local+"&"+destination_local+"&"+"departure_time=1494000027&"+"key="+key
            reader = codecs.getreader("utf-8")
            #obj = json.load(reader(response))
            time.sleep(0.8)
            answer = json.load(reader(urllib.request.urlopen(final)))
            for i in range(len(answer["rows"][0]['elements'])):
                one_row.append(answer["rows"][0]['elements'][i]["duration"]["value"])
        print(one_row)
        for j in one_row:
            outputFile.write((str(j)+","));
        outputFile.write(("\n"));
    outputFile.close()
    print("finished")
                #print(answer["rows"][0]['elements'][0]["duration"]["value"])
        
        


    '''    for index in range(len(lst)-2):
        if(index%2)==0:
            between += lst[index]+","
        else:
            between +=lst[index]+"|"
    between+=lst[len(lst)-2]+","+lst[len(lst)-1]
    origin+=between
    destination+=between
    #encodedX = urllib.urlencode(geo_args)
    final = url+origin+"&"+destination+"&"+"departure_time=1494000027&"+"key="+key
    print(final)
    reader = codecs.getreader("utf-8")
    #obj = json.load(reader(response))
    answer = json.load(reader(urllib.request.urlopen(final)))
    #print (json.dumps([s['formatted_address'] for s in answer['results']], indent=2))
    print(answer["rows"][0]['elements'][0]["duration"]["value"])'''
    
    
    

    
    
    
    
main()
