import os, time, subprocess
from threading import Lock
lock=Lock()
class Clean:
	
	def __init__(self, days=20, rec=False):
		self.rec=rec
		self.days=days
		self.start=time.time()
	def current(self, p):
		for self.i in os.listdir(p):
			if not os.path.isdir(self.i):
				print(self.i)
				self.d=(self.start-os.stat(p).st_atime)/(3600*24)
				self.e=(self.start-os.stat(p).st_mtime)/(3600*24)
				if int(self.d)>self.days or int(self.e)>self.days:
					self.a=input("Delete "+self.i+"? Yes or No")
					type(self.a)
					if self.a=="Yes":
						os.system("mv " +p+"/"+self.i+" /home/anirban/.local/share/Trash")
	def all(self, p):
		self.j=subprocess.check_output(["find", p, "-type", "d", "-print"])
		self.j=self.j.decode("utf-8")
		self.line=self.j.split("\n")
		for self.k in self.line:
			print(self.k)
			with lock:
				try:
					self.current(self.k)
				except Exception as e:
					print(e)

