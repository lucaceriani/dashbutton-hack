import time
try:
	from scapy.all import *
except ImportError:
	raise ImportError("You have to install scapy module.")

class dashButton:
		
	def __init__(self, macAddress, execFunction):
		self.__macAddress=macAddress
		self.__execFunction=execFunction
		self.__lastExecution=0

	def startListening(self):
		sniff(prn=self.__arp_display, filter="arp", store=0, count=0)

	def __arp_display(self, pkt):
		if (pkt[ARP].op==1) and (pkt[ARP].hwsrc == self.__macAddress):
			# controllo per non eseguire una funzione 4/5 volte di seguito
			if int(time.time())-self.__lastExecution > 2:
				# se sono passati almeno due secondi dall'ultima esecuzione
				self.__execFunction(self)
				self.__lastExecution=int(time.time())
	
	def getMacAddress(self):
		return self.__macAddress
