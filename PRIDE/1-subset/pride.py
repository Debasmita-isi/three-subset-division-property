from gurobipy import *

import time

class Pride:
	def __init__(self, Round, activebits):
		self.Round = Round
		self.activebits = activebits
		self.blocksize = 64
		self.filename_model = "Pride_" + str(self.Round) + "_" + str(self.activebits) + ".lp"
		self.filename_result = "result_" + str(self.Round) + "_" + str(self.activebits) + ".txt"
		fileobj = open(self.filename_model, "w")
		fileobj.close()
		fileboj = open(self.filename_result, "w")
		fileobj.close()

	S_T  =  [[-1, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, -1, 0, 0, 0, 0, 0, 1],
		[0, -1, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, -1, 0, 0, 0, 1],
		[0, 0, 0, 1, 0, -1, 0, -1, 1],
		[0, -1, -1, -1, 0, 0, 0, 1, 2],
		[0, 0, 0, 0, 0, -1, 0, 0, 1],
		[-1, 0, -1, 0, 1, -1, 0, 0, 2],
		[0, 1, 0, 1, 0, -1, -1, -1, 1],
		[0, 0, 0, 0, 0, 0, -1, 0, 1],
		[1, 1, 1, 1, -1, -1, -1, -1, 0],
		[1, 0, 1, 0, -1, -1, -1, 0, 1],
		[-1, -1, -2, -2, 1, 0, 1, 1, 3],
		[-1, -2, -3, -3, 0, 1, 1, 2, 5],
		[-1, -1, -2, -2, 0, 1, 0, 1, 4],
		[-2, -1, -1, -2, 1, 1, -1, -1, 6],
		[-1, -1, -2, -1, 1, 0, 1, 0, 3],
		[0, 0, 0, -1, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, -1, 1],
		[-1, 0, -1, -1, 1, 0, 0, 0, 2],
		[0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 1, 1, 2, 0, -2, 0, -1, 0],
		[0, 1, 0, 1, 0, -1, 0, 0, 0],
		[1, -1, 0, 0, -1, 0, 0, 1, 1],
		[0, 1, 1, 1, -1, -1, 0, 0, 0],
		[-1, 1, 1, 1, 0, -1, 0, 0, 0],
		[1, 0, 2, 1, -1, -1, -1, 0, 0],
		[-1, 2, -1, 2, 1, -1, 0, 0, 0],
		[1, 1, 1, 2, -1, -2, 0, -1, 0],
		[1, 0, 1, 1, -1, -1, 0, 0, 0],
		[-2, 1, 1, 2, 1, -1, 0, 0, 0],
		[0, 1, 1, 1, 0, 0, -2, 1, 0],
		[0, 0, 1, 1, 0, 0, -1, 0, 0],
		[0, 2, 1, 3, 0, -2, -1, -2, 0],
		[0, 2, 2, 2, -2, -1, -1, -1, 0],
		[0, 1, 2, 1, -1, -1, -1, 0, 0],
		[1, 0, 1, 1, -1, 0, -1, 0, 0],
		[2, 0, 2, 2, -2, -1, -1, -1, 0],
		[0, 2, 0, 2, 0, -1, -1, -1, 0],
		[1, 1, 2, 1, -1, -1, -2, 0, 0],
		[2, 0, 2, 1, -2, -1, -1, 0, 0],
		[0, 0, 1, 1, 0, -1, 0, 0, 0],
		[0, 1, 1, 1, -1, 0, -1, 0, 0],
		[-1, 1, 1, 1, 0, 0, -1, 1, 0],
		[-1, 0, 1, 2, 1, -1, 0, 0, 0],
		[1, -1, 0, 1, -1, 0, 0, 0, 1],
		[1, 1, 1, 3, -1, -2, 0, -2, 0],
		[0, 1, 0, 1, 0, 0, -1, 0, 0],
		[-2, 1, -1, 0, 2, 0, 2, 1, 0],
		[-1, 1, 0, 1, 0, 0, 0, 0, 0],
		[2, -2, 3, 2, 1, 1, -2, -1, 0],
		[1, -1, 1, 1, 0, 1, -1, 0, 0],
		[0, 1, 1, 2, -1, -1, 0, -1, 0],
		[0, -1, 0, -1, -1, 1, 1, 0, 2],
		[0, 1, 2, 1, -1, 1, 1, -2, 0],
		[2, -3, 4, 3, 1, 1, -2, -1, 0],
		[0, -1, -1, -1, 0, 1, 1, 1, 1],
		[-1, 1, 1, 2, 0, -1, 0, -1, 0],
		[-1, 0, 1, 1, 1, 0, 0, 0, 0],
		[0, 0, 1, 2, 0, -1, 0, -1, 0],
		[-3, 2, -1, 1, 3, 0, 2, 0, 0],
		[3, -2, 1, -1, 0, 1, 0, 2, 0],
		[2, -1, 3, 2, 1, 1, -3, -1, 0],
		[0, 1, 0, 2, 0, -1, 0, -1, 0],
		[0, 1, 1, 3, 0, -2, 0, -2, 0],
		[-1, 1, -1, 1, 1, 0, 1, 0, 0],
		[-3, 2, -1, 0, 3, 0, 2, 1, 0],
		[-1, 1, 1, 1, 0, 0, 1, -1, 0],
		[-1, 0, -1, -1, 1, 1, 2, 2, 0],
		[1, 0, 0, 1, 0, 1, -1, 0, 0],
		[0, 1, 1, 1, 0, -1, 0, -1, 0],
		[1, -1, 1, 0, 0, 0, 0, 0, 0],
		[-1, 1, 0, 0, 0, 0, 1, 1, 0],
		[0, -1, 3, 2, 1, 1, -1, -1, 0],
		[1, -2, 3, 2, 1, 1, -1, -1, 0],
		[-1, 1, 0, 0, 0, 1, 0, 1, 0],
		[2, 1, 1, 2, -1, -1, -1, -2, 0],
		[0, 0, 1, 1, 0, 0, 0, -1, 0],
		[2, -1, 3, 3, -1, -1, -1, -2, 0],
		[0, 1, 1, 0, 0, 0, 1, -1, 0],
		[2, 0, 2, 2, -1, -1, -1, -2, 0],
		[1, 1, 0, 1, 0, 0, -1, -1, 0],
		[-2, 1, -1, 1, 2, 0, 2, 0, 0],
		[1, -1, 2, 1, 1, 1, -1, -1, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, 0, -1, 0, 0],
		[0, 1, 0, 1, 0, 0, 0, -1, 0],
		[1, -1, 0, -1, 1, 0, 1, 0, 1],
		[-2, 3, 1, -2, 0, 2, 1, 3, 0],
		[-1, 0, -1, 0, 1, 1, 2, 1, 0],
		[2, 1, 1, 0, 0, 0, -1, -1, 0],
		[0, 1, 1, 0, 0, 0, -1, 1, 0],
		[-1, 0, -1, -1, 1, 0, 1, 1, 1],
		[-1, 1, 1, -1, 0, 1, 1, 1, 0],
		[1, 0, 1, 1, 0, 1, -2, 0, 0],
		[-1, 0, 0, 0, 1, 0, 1, 1, 0],
		[0, 1, 2, -1, -1, 1, 1, 0, 0],
		[-1, 0, 0, 1, 1, 0, 1, 0, 0],
		[1, 1, 1, 0, -1, 0, 0, -1, 0],
		[-1, 1, 0, -1, 0, 1, 1, 2, 0],
		[1, 0, 1, 2, -1, -1, 0, -1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 0],
		[1, 0, 1, -1, 0, 1, 0, 0, 0],
		[-2, 2, 1, -1, 0, 1, 1, 2, 0],
		[0, 1, 1, -2, 0, 2, 1, 1, 0],
		[1, -1, 0, -1, 0, 1, 1, 1, 0],
		[0, -1, 1, 1, 1, 0, 0, 0, 0],
		[-1, 1, 1, 0, 0, 0, 0, 1, 0],
		[-2, 1, -1, -1, 1, 1, 2, 3, 0],
		[-1, 0, -1, -1, 0, 1, 1, 2, 1],
		[2, -1, 1, 1, -1, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, 0, 0, -1, 0],
		[1, 1, 1, 2, 0, -1, -1, -2, 0],
		[-1, 2, -1, 1, 1, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, -1, 0, -1, 0],
		[-2, 1, 0, 1, 1, 0, 1, 0, 0],
		[-1, 1, -1, 0, 1, 0, 1, 1, 0],
		[-1, 1, 0, 1, 1, -1, 0, 0, 0],
		[1, 0, 1, 0, -1, 1, 1, -1, 0],
		[1, 0, 1, 1, 0, 0, -1, -1, 0],
		[0, -1, -1, -1, 1, 2, 2, 2, 0],
		[-3, 2, -1, -1, 3, 1, 2, 2, 0],
		[4, -1, 3, 4, -3, -1, -1, -2, 0],
		[1, -1, 0, 0, 0, 1, 0, 1, 0],
		[-2, 2, -1, 0, 2, 0, 1, 1, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0],
		[2, 1, 2, 2, -1, -1, -1, -3, 0],
		[0, 1, 1, 2, 0, -1, 0, -2, 0],
		[2, 1, 2, 3, -1, -2, -1, -3, 0],
		[-2, 1, -1, -1, 2, 0, 1, 1, 1],
		[2, -1, 1, 0, -1, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0],
		[1, 1, 2, 1, -1, 1, 1, -3, 0],
		[-1, 1, 0, 0, 1, 0, 0, 1, 0],
		[-1, 1, 1, 0, 0, 0, 1, 0, 0],
		[1, -1, 0, -1, 0, 0, 0, 1, 1],
		[-4, 3, -1, -1, 3, 1, 2, 3, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, -1, -1, -2, 1, 0, 1, 1, 2],
		[3, -1, 3, 3, -2, -1, -1, -2, 0],
		[0, 0, 0, -1, 0, 1, 1, 1, 0],
		[1, 0, 1, -1, -1, 1, 1, 0, 0],
		[3, -1, 4, -1, 1, 1, -1, -1, 0],
		[1, 0, 1, 1, -1, 0, 0, -1, 0],
		[1, 1, 2, -2, -1, 2, 1, 0, 0],
		[1, -1, 2, 2, 0, 0, -1, -1, 0],
		[1, 1, 2, -1, -1, 1, 1, -1, 0],
		[1, 1, 1, 1, -1, 0, 0, -2, 0],
		[0, 1, 1, 1, 0, 0, 1, -2, 0],
		[0, 1, 1, 1, -1, 0, 0, -1, 0],
		[0, 1, -1, 1, 1, 0, 0, 0, 0],
		[-1, 1, 0, 1, 1, 0, 1, -1, 0],
		[2, -1, 1, 2, -1, 1, -1, 0, 0],
		[0, 1, 1, 0, -1, 0, 0, 0, 0],
		[-2, 1, 0, 0, 1, 0, 1, 1, 0],
		[-3, 2, 1, 2, 1, -1, 0, 1, 0],
		[1, 1, 2, 1, -2, -1, -1, 0, 0],
		[1, 1, 2, 2, -1, 0, -3, 0, 0],
		[1, 0, 2, 2, -1, -1, -1, -1, 0],
		[0, 1, 2, 2, -1, -1, -1, -1, 0],
		[-1, -1, -1, -1, 0, 0, 1, 0, 3],
		[-1, -2, -1, -2, -1, 1, 1, 0, 5],
		[-1, -2, -2, -2, 0, 1, 1, 1, 4],
		[-1, -1, -1, -1, 0, 1, 0, 0, 3]]

	S_T1  = [[1, 1, 1, 1, -1, -1, -1, -1, 0],
		[-1, 0, 0, 0, 3, -2, -1, -1, 2],
		[0, -1, -1, -2, 1, 2, 3, 3, 0],
		[2, 1, 1, 0, -3, 1, -2, -2, 2],
		[0, -1, 0, 0, -1, 0, -1, 1, 2],
		[-2, 0, -2, -1, 2, -1, 1, 0, 3],
		[0, 0, 1, 1, -1, -1, 0, -1, 1],
		[-1, 0, -1, 0, -1, 1, 0, 1, 2],
		[1, 0, 0, 2, -1, -1, -1, -1, 1],
		[0, -1, 0, -1, -1, 1, 0, 0, 2],
		[-1, 0, 0, 0, 1, 0, 1, 1, 0]]
	NUMBER = 9

	C0  =   [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]]

	C1  =   [[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]]

	C2  =   [[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
		[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]]

	C3   =  [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]] 


	M0  =   [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]]

	M1  =   [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]] 

	M2  =   [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]

	M3  =   [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]
		  




	@staticmethod
	def CreateVariables1(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			array.append(("x" + "_" + str(n) + "_" + str(i)))
		return array

	@staticmethod
	def CreateVariables2(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			array.append(("y" + "_" + str(n) + "_" + str(i)))
		return array

	@staticmethod
	def CreateVariables3(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			for j in range(0, 16):
				array.append(("y" + "_" + str(n) + "_" + str(i) + "_" + str(j)))
		return array


	@staticmethod
	def CreateVariables4(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			array.append(("x1" + "_" + str(n) + "_" + str(i)))
		return array

	@staticmethod
	def CreateVariables5(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			array.append(("y1" + "_" + str(n) + "_" + str(i)))
		return array

	@staticmethod
	def CreateVariables6(n):
		"""
		Generate the variables used in the model.
		"""
		array = []
		for i in range(0, 64):
			for j in range(0, 16):
				array.append(("y1" + "_" + str(n) + "_" + str(i) + "_" + str(j)))
		return array

	@staticmethod
  	def CreateVariables7(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z" + "_" + str(n) + "_" + str(i)))
		return arrays

	@staticmethod
	def CreateVariables8(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z1" + "_" + str(n) + "_" + str(i)))
		return arrays

	@staticmethod
	def CreateVariables9(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z2" + "_" + str(n) + "_" + str(i)))
		return arrays

	@staticmethod
	def CreateVariables10(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z3" + "_" + str(n) + "_" + str(i)))
		return arrays

	@staticmethod
	def CreateVariables11(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		arrays.append(("b" + "_" + str(n)))
		return arrays

	@staticmethod
	def CreateVariables12(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		arrays.append(("c" + "_" + str(n)))
		return arrays

	def CreateObjectiveFunction(self):
		"""
		Create objective function of the MILP model
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Minimize\n")
		eqn = []
		for i in range(0, 64):
			eqn.append("x1" + "_" + str(self.Round) + "_" + str(i))
		temp = " + ".join(eqn)
		fileobj.write(temp)
		fileobj.write("\n")
		fileobj.close()

	def VariableRotation1(self, variablein):
		"""
		Bit Rotation.
		"""
		eqn = []
		for i in range(0, 64):
			eqn.append(variablein[((4 * i) % 64) + (i//16)])
		return eqn


	def VariableRotation2(self, variablein):
		"""
		Bit Rotation.
		"""
		eqn = ["" for i in range(0, 64)]
		for k in range(0, 16):
			eqn[(4 * k)] = variablein[k]
		for k in range(0, 16):
			eqn[(4 * k) + 1] = variablein[16 + k]
		for k in range(0, 16):
			eqn[(4 * k) + 2] = variablein[32 + k]
		for k in range(0, 16):
			eqn[(4 * k) + 3] = variablein[48 + k]
		return eqn




	def ConstraintsBySbox(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer.
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0, 16):
			for coff in Pride.S_T:
				temp = []
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[(4 * k) + u])
				for v in range(0, 4):
					temp.append(str(coff[v + 4]) + " " + variable2[(4 * k) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Pride.NUMBER - 1])
				s = s.replace("--", "")
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 

	def ConstraintsBySbox1(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer.
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0, 16):
			for coff in Pride.S_T1:
				temp = []
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[(4 * k) + u])
				for v in range(0, 4):
					temp.append(str(coff[v + 4]) + " " + variable2[(4 * k) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Pride.NUMBER - 1])
				s = s.replace("--", "")
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 

	def ConstraintsBySucc(self, variable1, variable2):

		fileobj = open(self.filename_model,"a")
		for k in range(0, 64):
			temp = []
			temp.append(str(1) + " " + variable2[k])
			temp.append(str(-1) + " " + variable1[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		temp = []
		for k in range(0, 64):
			temp.append(str(63) + " " + variable2[k])
		for k in range(0, 64):
			temp.append(str(-62) + " " + variable1[k])
		temp1 = " + ".join(temp)
		temp1 = temp1.replace("+ -", "- ")
		s = str(64)
		temp1 += " >= " + s
		fileobj.write(temp1)
		fileobj.write("\n")
  		fileobj.close()

	def ConstraintsByAssign(self, variable1, variable2, variable3, i):

		fileobj = open(self.filename_model,"a")
		variable4 = Pride.CreateVariables9(i)
		variable5 = Pride.CreateVariables10(i)
		variable6 = Pride.CreateVariables11(i)
		variable7 = Pride.CreateVariables12(i)
		temp = []
		temp.append(str(1) + " " + variable6[0])
		temp.append(str(1) + " " + variable7[0])
		temp1 = " + ".join(temp)
		temp1 = temp1.replace("+ -", "- ")
		s = str(1)
		temp1 += " = " + s
		fileobj.write(temp1)
		fileobj.write("\n")
		for k in range(0, 64):
			temp = []
			temp.append(str(1) + " " + variable1[k])
			temp.append(str(-1) + " " + variable4[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			temp = []
			temp.append(str(1) + " " + variable6[0])
			temp.append(str(-1) + " " + variable4[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			temp = []
			temp.append(str(1) + " " + variable1[k])
			temp.append(str(1) + " " + variable6[0])
			temp.append(str(-1) + " " + variable4[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(1)
			temp1 += " <= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		for k in range(0, 64):
			temp = []
			temp.append(str(1) + " " + variable2[k])
			temp.append(str(-1) + " " + variable5[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			temp = []
			temp.append(str(1) + " " + variable7[0])
			temp.append(str(-1) + " " + variable5[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			temp = []
			temp.append(str(1) + " " + variable2[k])
			temp.append(str(1) + " " + variable7[0])
			temp.append(str(-1) + " " + variable5[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(1)
			temp1 += " <= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		for k in range(0, 64):
			temp = []
			temp.append(str(1) + " " + variable4[k])
			temp.append(str(1) + " " + variable5[k])
			temp.append(str(-1) + " " + variable3[k])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		fileobj.close()


	def ConstraintsByCopy(self, variable1, variable2):
		"""
		Generate the constraints by copy.
		"""
		
                fileobj = open(self.filename_model,"a")
                count = 0
		for coff in Pride.C0:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,16):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(0)
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
			count += 1
                        fileobj.write("\n")
		count = 16
		for coff in Pride.C1:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,16):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(0)
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
			count += 1
                        fileobj.write("\n")
		count = 32
		for coff in Pride.C2:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,16):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(0)
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
			count += 1
                        fileobj.write("\n")
		count = 48
		for coff in Pride.C3:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,16):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(0)
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
			count += 1
                        fileobj.write("\n")
		
		fileobj.close(); 

	def ConstraintsByCopy1(self, variable1, variable2):
		"""
		Generate the constraints by copy.
		"""
		
                fileobj = open(self.filename_model,"a")
                count = 0
		for coff in Pride.C0:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0, 16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 16
		for coff in Pride.C1:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0, 16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 32
		for coff in Pride.C2:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0, 16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 48
		for coff in Pride.C3:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0, 16):
				temp.append(str(-coff[v]) + " " + variable2[(count * 16) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		fileobj.close(); 

	def ConstraintsByMixrow(self, variable1, variable2):
		"""
		Generate the constraints by mixrow.
		"""
		
                fileobj = open(self.filename_model,"a")
                count = 0
		for coff in Pride.M0:
			temp = []
			temp.append(str(-1) + " " + variable2[count])
			for v in range(0, 16):
				temp.append(str(coff[v]) + " " + variable1[count + (v * 16)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 0
		for coff in Pride.M1:
			temp = []
			temp.append(str(-1) + " " + variable2[count + 16])
			for v in range(0, 16):
				temp.append(str(coff[v]) + " " + variable1[(16 * 16) + count + (v * 16)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 0
		for coff in Pride.M2:
			temp = []
			temp.append(str(-1) + " " + variable2[count + 32])
			for v in range(0, 16):
				temp.append(str(coff[v]) + " " + variable1[(16 * 32) + count + (v * 16)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 0
		for coff in Pride.M3:
			temp = []
			temp.append(str(-1) + " " + variable2[count + 48])
			for v in range(0, 16):
				temp.append(str(coff[v]) + " " + variable1[(16 * 48) + count + (v * 16)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		fileobj.close(); 
		
	def Constraint(self):
		"""
		Generate the constraints used in the MILP model.
		"""
		assert(self.Round >= 1)
		fileobj = open(self.filename_model, "a")
		fileobj.write("Subject To\n")
		fileobj.close()
		variablein1 = Pride.CreateVariables4(0)
		variablein1 = self.VariableRotation2(variablein1)
		for i in range(1, self.Round):
			variablein = variablein1
			variableout = Pride.CreateVariables5(i-1)  
                        self.ConstraintsBySbox1(variablein, variableout)
			variableout2 = self.VariableRotation1(variableout)
			variableout= Pride.CreateVariables6(i-1)
                        self.ConstraintsByCopy1(variableout2, variableout)
			variablein =  Pride.CreateVariables6(i-1)
                        variableout2 = Pride.CreateVariables4(i)
                        self.ConstraintsByMixrow(variablein, variableout2)
			variableout2 = self.VariableRotation2(variableout2)
			variablein1 = variableout2
		variablein = variableout2
		variableout = Pride.CreateVariables4(self.Round)  
                self.ConstraintsBySbox1(variablein, variableout)
			

	def VariableBinary(self):
		"""
		Specify the variable type.
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Binary\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("x_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("x1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("z1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("z_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("z2_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("z3_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			fileobj.write("b_" + str(i))
			fileobj.write("\n")
		for i in range(0, (self.Round + 1)):
			fileobj.write("c_" + str(i))
			fileobj.write("\n")
		for i in range(0, self.Round):
			for j in range(0, 64):
				fileobj.write("y_" + str(i) + "_" + str(j))
                                fileobj.write("\n")
                for i in range (0, self.Round):
			for j in range(0, 64):
         			for k in range(0, 16):
					fileobj.write("y_" + str(i) + "_" + str(j) + "_" + str(k))
					fileobj.write("\n")
		for i in range(0, self.Round):
			for j in range(0, 64):
				fileobj.write("y1_" + str(i) + "_" + str(j))
                                fileobj.write("\n")
                for i in range (0, self.Round):
			for j in range(0, 64):
         			for k in range(0,16):
					fileobj.write("y1_" + str(i) + "_" + str(j) + "_" + str(k))
					fileobj.write("\n")
		fileobj.write("END")
		fileobj.close()

	def Init(self):
		"""
		Generate the constraints introduced by the initial division property.
		"""
		variableout = Pride.CreateVariables4(0)
		fileobj = open(self.filename_model, "a")
		temp = []
		for i in range(0, 1):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(1, 3):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(3, 63):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(63, 64):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                fileobj.close()
		
		#variableout = Pride.CreateVariables4(self.Round)
		#fileobj = open(self.filename_model, "a")
		#temp = []
		#for i in range(0, 32):
		#	temp = variableout[i] + " = 0"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		#for i in range(32, 33):
		#	temp = variableout[i] + " = 1"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		#for i in range(33, 64):
		#	temp = variableout[i] + " = 0"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		#fileobj.close()
                             


	def MakeModel(self):
		"""
		Write the MILP model into the file
		"""
		self.CreateObjectiveFunction()
		self.Constraint()
		self.Init()
		self.VariableBinary()

	def WriteObjective(self, obj):
		"""
		Write the objective value into filename_result.
		"""
		fileobj = open(self.filename_result, "a")
		fileobj.write("The objective value = %d\n" %obj.getValue())
		eqn1 = []
		eqn2 = []
		for i in range(0, self.blocksize):
			u = obj.getVar(i)
			if u.getAttr("x") != 0:
				eqn1.append(u.getAttr('VarName'))
				eqn2.append(u.getAttr('x'))
		length = len(eqn1)
		for i in range(0,length):
			s = eqn1[i] + "=" + str(eqn2[i])
			fileobj.write(s)
			fileobj.write("\n")
		fileobj.close()

	def SolveModel_2(self):
		"""
		Solve the MILP model to search the integral distinguisher of Simon.
		"""
		time_start = time.time()
		m = read(self.filename_model)
		m.setParam( 'OutputFlag', 0 )
		m.setParam( 'Presolve', 0 )
		m.setParam( 'PoolSearchMode',  1 )

		#set_zero = []
		#global_flag = False
		#while counter < self.blocksize:
		m.optimize()
			# Gurobi syntax: m.Status == 2 represents the model is feasible.

		if m.Status == 2:
			fileobj = open(self.filename_result, "a")
			counter = m.getAttr( 'SolCount' ) 
			print( "{} solutions...".format( counter ) )
			fileobj.write("************************************COUNTER = %d\n" % counter)
			fileobj.write("\n")
			time_end = time.time()
			fileobj.write(("Time used = " + str(time_end - time_start)))
			fileobj.close()


	def SolveModel_1(self):
		"""
		Solve the MILP model to search the integral distinguisher of Simon.
		"""
		time_start = time.time()
		m = read(self.filename_model)
		counter = 0
		set_zero = []
		global_flag = False
		m.optimize()
			# Gurobi syntax: m.Status == 2 represents the model is feasible.
		if m.Status == 2:
			fileobj = open(self.filename_result, "a")
			fileobj.write("\nIntegral Distinguisher Found!\n\n")
			print "Integral Distinguisher Found!\n"
				
			# Gurobi syntax: m.Status == 3 represents the model is infeasible.
		elif m.Status == 3:
			
			fileobj = open(self.filename_result, "a")		
		
			fileobj.write("\nIntegral Distinguisher do NOT exist\n\n")
			print "Integral Distinguisher do NOT exist\n"

		
		fileobj.write("\n")
		time_end = time.time()
		fileobj.write(("Time used = " + str(time_end - time_start)))
		fileobj.close()

	def SolveModel(self):
		"""
		Solve the MILP model to search the integral distinguisher of Present.
		"""
		time_start = time.time()
		m = read(self.filename_model)
		counter = 0
		set_zero = []
		global_flag = False
		while counter < self.blocksize:
			m.optimize()
			# Gurobi syntax: m.Status == 2 represents the model is feasible.
			if m.Status == 2:
				obj = m.getObjective()
				if obj.getValue() > 1:
					global_flag = True
					break
				else:
					fileobj = open(self.filename_result, "a")
					fileobj.write("************************************COUNTER = %d\n" % counter)
					fileobj.close()
					self.WriteObjective(obj)
					for i in range(0, self.blocksize):
						u = obj.getVar(i)
						temp = u.getAttr('x')
						if temp == 1:
							set_zero.append(u.getAttr('VarName'))
							u.ub = 0
							m.update()
							counter += 1
							break
			# Gurobi syntax: m.Status == 3 represents the model is infeasible.
			elif m.Status == 3:
				global_flag = True
				break
			else:
				print "Unknown error!"

		fileobj = open(self.filename_result, "a")		
		if global_flag:
			fileobj.write("\nIntegral Distinguisher Found!\n\n")
                     
			print "Integral Distinguisher Found!\n"
		else:
			fileobj.write("\nIntegral Distinguisher do NOT exist\n\n")
			print "Integral Distinguisher do NOT exist\n"

		fileobj.write("Those are the coordinates set to zero: \n")
		for u in set_zero:
			fileobj.write(u)
			fileobj.write("\n")
		fileobj.write("\n")
		time_end = time.time()
		fileobj.write(("Time used = " + str(time_end - time_start)))
		fileobj.close()



		  


	
