class Flight:
    def __init__(self,upTime,downTime,totalup,totaldown):
        self.upTime=totalup
        self.downTime=totaldown
    def calculateFlight(hrsup,minsup,hrsdown,minsdown):
        calculateFlight1=0        
        totaldown=(hrsdown*60)+minsdown
        totalup=(hrsup*60)+minsup
        calculateFlight1=totaldown-totalup
        return calculateFlight1
    hrsup,minsup=input().split(":")
    hrsdown,minsdown=input().split(":")
    hrsup,minsup=int(hrsup),int(minsup)
    hrsdown,minsdown=int(hrsdown),int(minsdown)
    print(calculateFlight(hrsup,minsup,hrsdown,minsdown))

