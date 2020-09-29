import wget
import time
startTime = time.time()
while(1):
    info_all = time.ctime(time.time()).split(" ")
    info = [info_all[2],info_all[1], info_all[3]]
    filename = "_".join(info)
    directory = './sourdough/' + filename  + '.jpg'
    url = 'http://10.0.0.27/test.jpg'
    print str((startTime - time.time())/60) + " minutes elapsed"
    wget.download(url, directory)
    time.sleep(5*60)



