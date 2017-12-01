try:
	from scapy.all import *
except ImportError:
	raise ImportError("You have to install scapy module.")

class dashButton:
	def __init__(self, macAddress, execFunction):
		self.__macAddress=macAddress
		self.__execFunction=execFunction

	def startListening(self):
		sniff(prn=self.__arp_display, filter="arp", store=0, count=0)

	def __arp_display(self, pkt):
		if pkt[ARP].op == 1:
			if pkt[ARP].hwsrc == self.__macAddress:
				self.__execFunction(dashButton)

#print (sniff(prn=arp_display, filter="arp", store=0, count=0))
