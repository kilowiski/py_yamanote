# use this
# https://github.com/piuccio/open-data-jp-railway-stations.git
import json

class Station:
    def __init__(self, name, num_code):
        self.name = name
        self.num_code = num_code

with open('/home/kilohotel/open-data-jp-railway-stations/stations.json', 'r') as f:
  data = json.load(f)

#create empty variable
yamanote=[]

for i in data:
    if "JR-East.Yamanote" in i["line_codes"]:
        name = i["name_kanji"]
        for k in i["stations"]:
            if "JR-East.Yamanote" in k["line_code"]:
                short_code = k["short_code"]
                num_short_code = int(short_code.replace("JY",""))
                stationObject = Station(name,num_short_code)
                yamanote.append(stationObject)


def check_station(station1,station2):
    variabelCidok = 5
    if station1 in yamanote and station2 in yamanote:
        return True
    else:
        return False

def disuruhCidok(station1,station2):
    idx_station1=99
    idx_station2=99

    if(station1 == station2):
        print("乗らなくてもいいよ")
        return

    for k in yamanote:
        if k.name == station1:
            idx_station1 = yamanote.index(k)
        if k.name == station2:
            idx_station2 = yamanote.index(k)

    if(idx_station1 == 99) or (idx_station2==99):
        print("エラー")
        return

    clockwise = idx_station2-idx_station1
    counterclockwise =idx_station1-idx_station2

    clockwise=int(clockwise)
    counterclockwise=int(counterclockwise)

    yamanotelen=len(yamanote)

    if counterclockwise < 0:
        counterclockwise=yamanotelen+counterclockwise
    elif clockwise<0 :
        clockwise=yamanotelen+clockwise

    print("内回り",clockwise*2," ,　外回り",counterclockwise*2)

def takenum(elem):
    return elem.num_code

def main():
    #initialize the stations
    #initializeStation()
    global yamanote

    takanawa=Station("高輪", 26)
    yamanote.append(takanawa)

    yamanote.sort(key=takenum)

    for i in yamanote:
        print(i.num_code," ",i.name)

    #1 check if the stations are valid
    station1= input("出発駅を入力してください　＝　")
    station2= input("到着駅を入力してください　＝　")

    #2 calculate the time between station
    disuruhCidok(station1, station2)

    #this is using an array, not very good but ok

if __name__ == "__main__":
    main()
