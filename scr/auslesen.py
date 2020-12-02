

class auslesen(): 
    def config():
        gesamt = open("config.txt","r")
        sammler =gesamt.readlines()
        gesamt.close()

        lesen = []

        for i in sammler:
            i = i.split("=")
            lesen.append(i[-1])        
        delay = int(lesen[1])
        spielenx = int(lesen[3])



        return delay, spielenx