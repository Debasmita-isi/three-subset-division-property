from gurobipy import *

import time

class Klein:
	def __init__(self, Round, activebits):
		self.Round = Round
		self.activebits = activebits
		self.blocksize = 64
		self.filename_model = "Klein_" + str(self.Round) + "_" + str(self.activebits) + ".lp"
		self.filename_result = "result_" + str(self.Round) + "_" + str(self.activebits) + ".txt"
		fileobj = open(self.filename_model, "w")
		fileobj.close()
		fileboj = open(self.filename_result, "w")
		fileobj.close()

	S_T  =  [[0, -1, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, -1, 0, 0, 0, 0, 0, 1],
	     	[-1, 0, 0, 0, 0, 0, 0, 0, 1],
	     	[0, 1, 1, 1, -1, -1, -1, 0, 0],
	    	[1, 1, 1, 1, -1, -1, -1, -1, 0],
	        [1, 2, 1, 1, -2, -1, -1, -1, 0],
	        [0, 0, 0, 0, 0, 0, 0, -1, 1],
	        [0, 0, 0, 0, -1, 0, 0, 0, 1],
	        [-2, -2, -1, -1, 1, 0, 1, -1, 5],
	        [0, 0, 0, 0, 0, -1, 0, 0, 1],
	        [-1, -2, -1, -1, 1, -1, 1, -1, 5],
	        [-2, -2, -1, -1, 0, 1, -1, 1, 5],
	        [1, 1, 0, 0, -1, 0, -1, -1, 1],
	        [1, -1, 0, -1, 1, -2, -1, -1, 4],
	        [-1, -2, -3, -3, 2, -1, -2, 1, 9],
	        [1, 0, 1, 0, 0, -1, -1, -1, 1],
	        [2, 1, 1, 1, -1, -1, -2, -2, 1],
		[-1, 0, -1, -1, 0, -1, -1, 1, 4],
		[0, -1, 0, -1, 1, -1, 0, -1, 3],
		[-2, -1, -3, -3, 1, -2, -1, 2, 9],
		[-1, 0, -1, -1, 0, 1, -1, -1, 4],
		[0, -1, -1, -1, 1, -1, -1, 0, 4],
		[-1, -1, 0, 0, -1, 0, -1, 1, 3],
		[0, 0, 0, 0, 0, 0, -1, 0, 1],
		[-2, -1, -2, -1, 1, 1, -1, -1, 6],
		[1, 1, 1, 1, -1, -2, 0, 0, 0],
		[0, 1, -1, 1, 0, 0, 1, 0, 0],
		[1, 1, 1, 2, -1, -3, 0, 1, 0],
		[1, 1, -1, 1, -1, 0, 0, 0, 0],
		[1, 1, -1, 2, -1, -1, 0, 1, 0],
		[1, 2, -2, 3, -1, -1, 0, 1, 0],
		[-1, 1, 0, 1, 0, 0, 1, 0, 0],
		[1, 2, -1, 3, -2, -1, -1, 1, 0],
		[1, 2, 2, 3, -5, -1, -1, 1, 0],
		[1, 2, 1, 1, -1, -2, 0, -1, 0],
		[-1, 1, 1, 2, -1, -1, 0, 1, 0],
		[1, -1, 1, 2, -1, 0, 0, 0, 0],
		[-2, 2, 1, 3, -1, -1, 0, 1, 0],
		[1, -1, 1, 2, -1, -1, 0, 1, 0],
		[1, 1, 1, 1, -2, 0, 0, -1, 0],
		[-1, 2, 1, 3, -2, -1, -1, 1, 0],
		[2, 3, 2, 2, -5, -1, -1, -1, 0],
		[1, 0, 2, 2, -2, -1, -1, 0, 0],
		[1, 1, 1, 1, -1, 0, 0, -2, 0],
		[1, 2, 2, 2, -4, -1, -1, 0, 0],
		[2, 0, 2, 2, -2, -1, -1, -1, 0],
		[1, 0, 1, 1, -1, 0, 0, -1, 0],
		[1, 1, 0, 2, -1, -1, -1, 0, 0],
		[1, 1, 2, 3, -4, 0, -2, 2, 0],
		[0, 0, 1, 1, 0, 1, 0, -1, 0],
		[2, 1, 1, 1, -1, 0, -2, -1, 0],
		[3, 1, 2, 2, -1, -1, -3, -2, 0],
		[2, 0, 1, 1, -1, 0, -1, -1, 0],
		[-1, -1, 0, 1, 1, 2, 1, -1, 1],
		[0, 0, 0, 1, -1, 0, -1, 1, 1],
		[2, 1, 0, 1, -1, 0, -1, -1, 0],
		[0, 0, 1, 1, -2, 0, -1, 1, 1],
		[1, -2, 1, 2, 0, 2, 1, -1, 0],
		[2, 2, 3, -4, 2, 0, 1, -1, 0],
		[1, 1, 1, -2, 1, 0, 1, 0, 0],
		[-1, -1, 1, 2, 2, 4, 2, -2, 0],
		[1, -1, 1, 0, 1, 0, 0, 0, 0],
		[1, 2, 3, 0, -2, -1, -2, 1, 0],
		[0, -1, 1, 0, 1, 1, 1, 0, 0],
		[1, 1, -1, 0, 0, 0, 1, 0, 0],
		[1, -1, 1, 1, 0, 1, 0, -1, 0],
		[1, 1, 0, -1, 0, 0, 1, 0, 0],
		[0, 1, 1, 0, 0, -1, 0, 0, 0],
		[-1, -1, 0, -1, 1, 2, 1, 1, 1],
		[3, 3, 1, 1, -3, 0, -2, -2, 0],
		[-1, -1, 0, -1, 2, 3, 2, 2, 0],
		[0, 0, -1, 0, 1, 1, 1, 1, 0],
		[1, 2, 1, -3, 1, 0, 2, 1, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0],
		[-1, -1, -1, 1, 1, 1, 1, -1, 2],
		[2, 2, 1, 0, -2, 0, -1, -1, 0],
		[-1, 1, 1, 0, 0, 0, 0, 0, 0],
		[-1, -1, 1, -1, 2, 3, 2, 1, 0],
		[1, 1, 2, 1, 0, -1, -2, -1, 0],
		[0, 0, 1, 0, -1, 0, -1, 1, 1],
		[2, 1, 1, 0, -1, 0, -1, -1, 0],
		[1, 1, -3, 1, 1, 1, 2, 1, 0],
		[-1, -1, -1, -1, 3, 3, 3, 3, 0],
		[1, 1, 0, 0, 0, 0, 0, -1, 0],
		[2, 1, 2, 1, 0, -1, -2, -2, 0],
		[1, 2, 1, -1, 0, 1, -1, -1, 0],
		[1, 1, 1, -1, 0, -1, 1, 0, 0],
		[-1, -1, 0, -1, 0, 1, 0, 1, 2],
		[1, 1, -2, 1, 0, 0, 1, 1, 0],
		[0, -1, -1, -1, 1, 0, -1, 1, 3],
		[0, 0, 0, 1, 0, 1, 1, -1, 0],
		[2, 2, 1, 0, -1, 0, -1, -2, 0],
		[3, -1, 3, 1, 0, -1, -2, -1, 0],
		[0, -1, 0, -1, 1, 1, 0, 1, 1],
		[0, 1, 0, 0, 0, 0, 0, 0, 0],
		[3, 2, 4, -4, 2, -1, 1, -2, 0],
		[1, -1, 1, 1, 0, -1, 0, 1, 0],
		[-2, -2, -1, 0, 1, 1, 1, -1, 4],
		[1, 1, 0, 0, -1, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, -1, 0, 0, 0],
		[4, -1, 3, -1, 1, -2, -1, -1, 1],
		[1, 0, 1, 2, -1, -1, -1, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 0],
		[2, -1, 1, -1, 1, 0, -1, 1, 1],
		[1, 0, 0, 1, -1, 0, 0, 0, 0],
		[1, 0, 1, -2, 2, 1, 0, 1, 0],
		[1, 0, 0, -1, 1, 1, 0, 1, 0],
		[-1, 0, 1, -1, 1, 2, 1, 1, 0],
		[3, -1, 2, 0, 1, -1, -1, 0, 0],
		[1, 1, 0, -2, 1, 1, 1, 1, 0],
		[1, -1, 1, -2, 3, 2, 0, 2, 0],
		[1, 1, 1, 0, 0, -2, 1, 0, 0],
		[2, 2, -3, 1, 0, 1, 1, 0, 0],
		[2, -1, 1, -3, 3, 2, -1, 3, 1],
		[-1, -1, 1, 0, 2, 2, 2, 0, 0],
		[1, 0, 1, -1, 1, 1, -1, 1, 0],
		[1, 2, -2, 1, 0, 0, 1, 0, 0],
		[-1, 2, 1, 1, 0, -1, -1, 1, 0],
		[1, 0, 0, 1, 0, -1, 0, 1, 0],
		[3, -1, 2, -4, 5, 3, -1, 4, 0],
		[1, 1, 1, 1, -1, 0, -2, 0, 0],
		[2, 1, -2, 0, 0, 1, 1, 1, 0],
		[2, 2, 1, -1, -1, 1, -1, -1, 0],
		[3, 2, -4, 1, 0, 1, 2, 1, 0],
		[3, 3, 1, 0, -2, 1, -2, -2, 0],
		[2, 2, 3, -6, 4, 2, 1, 1, 0],
		[1, -1, 0, 0, 1, -1, -1, 0, 2],
		[3, 2, -2, 1, 0, 1, 0, -1, 0],
		[2, 0, 2, 1, 0, -1, -2, -1, 0],
		[-1, -1, 0, 0, 1, 1, 1, 0, 1],
		[2, 1, -1, -1, 0, 1, 1, 1, 0],
		[1, 1, 1, -2, 1, 1, 0, 0, 0],
		[2, 0, 2, 2, -1, -1, -2, -1, 0],
		[1, 1, 0, -1, 0, 1, 0, 0, 0],
		[-1, -1, -1, 0, 0, 1, -1, 1, 3],
		[0, -1, -1, -1, 1, 2, 1, 2, 1],
		[1, 1, 1, -3, 2, 1, 1, 1, 0],
		[1, 1, -1, 0, 0, 1, 0, 0, 0],
		[1, 2, 1, -4, 2, 1, 2, 2, 0],
		[0, 0, 0, -1, 1, 1, 1, 1, 0],
		[0, 1, 1, 0, 0, 0, -1, 0, 0],
		[2, 3, 2, -3, 0, 2, -1, -1, 0],
		[1, 0, 1, 0, 0, 0, -1, 0, 0],
		[1, 1, 2, -1, 0, 1, -2, 1, 0],
		[1, 1, 1, 0, 0, 1, -2, 0, 0],
		[1, 2, 4, 5, -7, -1, -3, 3, 0],
		[2, 2, -4, 1, 1, 1, 2, 1, 0],
		[1, 1, -2, 0, 1, 1, 1, 1, 0],
		[1, 0, -1, -1, 1, 2, 1, 2, 0],
		[-1, -1, 1, -2, 3, 4, 2, 2, 0],
		[2, 1, -1, -2, 1, 2, 1, 2, 0],
		[1, 0, 1, 1, 0, -2, 0, 1, 0],
		[1, 2, 1, 5, -4, -1, -3, 3, 0],
		[1, 0, 1, 1, 0, 0, -1, -1, 0],
		[1, 2, -4, 1, 2, 1, 2, 2, 0],
		[2, 3, -6, 2, 2, 1, 3, 2, 0],
		[2, 1, 2, 2, -1, -1, -3, -1, 0],
		[3, 1, 3, 2, 0, -1, -4, -2, 0],
		[-1, -2, -1, -1, 1, 1, 0, 1, 3],
		[1, 3, -5, 2, 2, 1, 2, 2, 0],
		[0, -1, 1, 2, 1, 3, 1, -2, 0],
		[0, -1, -1, -1, 2, 3, 2, 3, 0],
		[1, 2, -3, 2, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0],
		[1, 1, 2, -2, 1, 0, 1, -1, 0],
		[1, 0, 1, 1, 0, -1, -1, 0, 0],
		[2, 0, 2, -1, 1, -1, 0, -1, 0],
		[0, 2, -2, 1, 1, 0, 1, 1, 0],
		[1, 1, 3, -2, 2, 0, 2, -2, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0],
		[-2, 1, 1, 1, 0, 0, 1, 1, 0],
		[1, 1, 1, -1, 0, 0, 0, -1, 0],
		[1, 3, -4, 2, 1, 0, 2, 1, 0],
		[-1, -2, -1, -2, 4, 5, 4, 5, 0],
		[0, 1, 1, 1, -2, 0, 0, 0, 0],
		[-1, 1, 0, 1, 0, 0, 0, 1, 0],
		[2, 3, 2, 0, -3, -1, -1, -1, 0],
		[2, 4, -7, 3, 2, 1, 3, 2, 0],
		[1, 1, 1, 1, 0, -3, 1, 1, 0],
		[1, 2, 1, 1, 1, -4, 2, 1, 0],
		[0, 1, 1, 2, -2, -1, -1, 1, 0],
		[-1, 2, 0, 1, 1, -1, 0, 1, 0],
		[1, 1, 0, 1, -2, 0, 0, 0, 0],
		[1, 1, 1, 0, -1, -1, 0, 0, 0],
		[1, 0, 1, 1, -1, 0, -1, 0, 0],
		[1, 2, -4, 2, 1, 1, 2, 1, 0],
		[0, 0, 1, 1, -1, 0, 0, 0, 0],
		[1, 1, 1, -1, 0, 1, -1, 0, 0],
		[0, 1, 0, 1, 0, 0, -1, 1, 0],
		[-2, 3, 1, 1, 2, -2, 0, 2, 0],
		[1, 1, 1, 0, 0, 0, 0, -2, 0],
		[-1, 0, -1, -1, 1, -1, 0, 1, 3],
		[0, 1, 1, 1, 0, -2, 0, 1, 0],
		[1, 2, 2, 0, -2, -1, -1, 0, 0],
		[3, -1, 2, 2, 1, -3, -1, 2, 0],
		[-1, 2, 1, 1, 1, -2, 0, 1, 0],
		[2, 1, 2, -1, 1, -1, 0, -2, 0],
		[1, 0, 1, -1, 1, -1, 0, -1, 1],
		[-2, -3, -2, -1, 1, 2, -1, 1, 6],
		[1, 0, 1, 0, 0, 0, 0, -1, 0],
		[2, 1, 2, -2, 1, -1, 1, -1, 0],
		[-1, 2, -1, -1, 3, 0, 3, 3, 0],
		[-1, 3, -1, -1, 4, -1, 3, 4, 0],
		[0, 1, -1, 0, 1, 0, 1, 1, 0],
		[-1, 1, 1, 1, -1, 0, 0, 0, 0],
		[-3, 2, 1, 1, 1, 0, 1, 1, 0],
		[2, 1, 2, 0, 0, -1, -1, -2, 0],
		[-2, 2, 1, 1, 1, -1, 0, 1, 0],
		[1, -3, 1, 1, 2, 1, 2, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 0],
		[1, 2, -3, 1, 1, 0, 2, 1, 0],
		[-1, 1, 1, 1, 0, -1, 0, 1, 0],
		[2, 0, 2, 0, 0, -1, -1, -1, 0],
		[3, 1, 3, -2, 2, -2, 1, -2, 0],
		[1, 0, 1, 2, -2, 0, -1, 1, 0],
		[3, -1, 3, 3, -2, -1, -2, -1, 0],
		[1, 1, 1, 2, -1, -1, -2, 0, 0],
		[1, 2, 4, 1, -3, -1, -3, 2, 0],
		[1, 1, 2, 0, -1, -1, -1, 0, 0],
		[-1, 1, -1, 2, 1, 1, 0, 2, 0],
		[-1, -2, -1, -1, 4, 4, 3, 4, 0],
		[-2, -2, -1, -1, 5, 5, 4, 4, 0],
		[-2, -2, -1, -1, 2, 2, 1, 1, 3],
		[1, 0, 2, -1, 1, 0, 1, -1, 0],
		[-3, -3, 1, 1, 5, 5, 6, 1, 0],
		[1, 0, -1, 0, 0, 1, 1, 1, 0],
		[0, 0, -1, 1, 1, 1, 1, 0, 0],
		[-1, -1, -1, 2, 3, 3, 2, 0, 0],
		[-1, -1, -1, 3, 3, 3, 3, -1, 0],
		[-1, -1, -1, 0, 3, 3, 2, 2, 0],
		[-1, -2, -1, 4, 4, 4, 3, -1, 0],
		[-1, 0, -1, 1, 2, 2, 1, 1, 0],
		[-2, -2, -1, 4, 5, 5, 4, -1, 0],
		[0, -1, 0, 0, 1, 1, 1, 1, 0],
		[1, -2, 0, 1, 1, 1, 2, 1, 0],
		[1, -4, 1, 2, 2, 2, 3, 1, 0],
		[0, -3, 1, 1, 2, 2, 3, 1, 0],
		[1, 2, 1, 3, -2, -1, -3, 1, 0],
		[-3, 2, 1, 2, 0, 0, 1, 1, 0],
		[-1, 0, 0, 0, 1, 1, 1, 1, 0],
		[-2, 1, 0, 1, 1, 1, 1, 1, 0],
		[-3, 1, 1, 1, 1, 1, 2, 1, 0],
		[-4, 2, 1, 2, 1, 1, 2, 1, 0],
		[2, 1, -3, 1, 0, 1, 2, 1, 0],
		[-4, -4, 2, 1, 6, 7, 8, 1, 0],
		[1, 1, -2, 1, 0, 1, 1, 0, 0],
		[-1, 1, 2, -1, 0, 1, 0, 1, 0],
		[-1, 2, -1, 3, 0, 1, -1, 3, 0],
		[-1, -3, -1, -2, 5, 6, 4, 6, 0],
		[-2, -1, 1, -1, 2, 4, 3, 2, 0],
		[2, 3, 2, -2, -1, -1, 1, -1, 0],
		[1, 2, 1, 0, -1, -1, 0, -1, 0],
		[-1, -2, -1, -2, 1, 2, 1, 2, 3],
		[-2, -3, -1, -3, 1, 3, 1, 2, 5],
		[-1, -2, -1, -2, 0, 1, 1, 1, 4],
		[3, 2, 2, 1, -1, -1, -2, -3, 0],
		[0, 1, 1, -1, 0, 0, 0, 0, 0],
		[2, -1, -1, 1, 0, 1, 2, 1, 0],
		[1, 0, 2, 1, -1, -1, -1, 0, 0],
		[-1, 0, 1, 0, 0, 1, 1, 1, 0],
		[-1, 1, 2, 1, -2, 1, 0, 1, 0],
		[5, 2, 6, -4, 4, -3, 1, -4, 0],
		[0, 1, -1, 1, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0],
		[-1, -1, 2, 1, 0, 1, 2, 1, 0],
		[0, 1, 0, -1, 1, 0, 1, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0],
		[1, -1, 0, 1, 0, 0, 1, 1, 0],
		[0, -1, 1, 1, 0, 0, 1, 1, 0],
		[-2, -2, 1, 4, 3, 7, 4, -3, 0],
		[1, 1, 2, 0, -1, 0, -2, 1, 0],
		[-1, -4, 2, 1, 3, 4, 5, 1, 0],
		[2, 1, -2, -1, 1, 2, 1, 2, 0],
		[-1, -3, -1, -2, 2, 3, 1, 3, 3],
		[-2, -4, -1, -3, 2, 4, 1, 3, 5],
		[-2, 1, 1, 1, 0, 1, 1, 0, 0],
		[-3, 1, 2, 1, 0, 1, 2, 1, 0],
		[-4, 1, 2, 1, 1, 2, 3, 1, 0],
		[0, 1, -2, 1, 1, 1, 1, 1, 0],
		[-2, -2, 1, -1, 3, 5, 4, 2, 0],
		[1, 1, 2, -1, 1, -1, 0, -1, 0],
		[1, 1, 2, 0, 0, -1, -1, -1, 0],
		[1, 1, 2, 2, -3, 0, -2, 1, 0],
		[-1, -2, 1, 4, 2, 6, 3, -3, 0],
		[1, 1, 1, 3, -3, 0, -2, 2, 0],
		[-1, -1, -1, 0, 1, 1, 0, 0, 2],
		[-2, -2, -1, 1, 2, 2, 1, -1, 3],
		[1, 0, 0, 1, 0, 1, 0, -1, 0],
		[0, 1, 2, 2, -3, 0, -1, 1, 0],
		[-1, -2, -1, 2, 2, 2, 1, -1, 2],
		[0, 1, 0, 2, -1, 0, -1, 1, 0],
		[-1, 0, -1, 1, 0, 1, -1, 1, 2],
		[1, 0, -1, 2, 0, 2, 1, -1, 0],
		[0, 1, 0, 1, 0, -1, 0, 0, 0],
		[0, -1, 0, 2, 1, 2, 1, -1, 0],
		[1, 2, 4, 4, -6, -1, -3, 2, 0],
		[2, 1, 1, 1, -1, 0, -1, -2, 0],
		[1, 0, 1, 1, 0, 1, 0, -2, 0],
		[2, 2, 1, 1, -3, 0, -1, -1, 0],
		[4, 2, 2, 2, -2, -1, -3, -3, 0],
		[0, -1, 0, 1, 1, 1, 0, -1, 1],
		[1, -1, 1, 2, 1, 2, 0, -2, 0],
		[1, 2, 0, 1, -1, -1, 0, -1, 0],
		[3, 2, 1, 1, -2, 0, -2, -2, 0],
		[2, 5, 2, 2, -3, -3, 0, -3, 0],
		[-1, 1, -1, 3, 1, 1, 3, -1, 0],
		[2, -1, 2, 3, -2, -1, -1, 0, 0],
		[2, -1, 2, 4, -3, -1, -1, 1, 0],
		[-1, -1, -1, 0, 1, 0, 1, -1, 3],
		[-1, 0, -1, 1, 1, 0, 1, -1, 2],
		[-1, 2, -1, 3, 1, 0, 3, -1, 0],
		[0, 1, 0, 1, 0, 0, 1, -1, 0],
		[1, 2, 1, 1, -1, -1, 0, -2, 0],
		[1, 1, 1, 1, -2, -1, 0, 0, 0],
		[1, 1, 1, 2, -3, -1, 0, 1, 0],
		[1, 1, 1, 4, -3, -3, 0, 3, 0],
		[1, 1, 1, 2, -1, -2, -1, 0, 0],
		[1, 1, 1, 2, -3, 1, 1, -1, 0],
		[1, 0, 1, 3, -2, -1, -1, 1, 0],
		[1, 0, 2, 3, -3, -1, -1, 1, 0],
		[1, 0, 1, 1, -1, -1, 0, 0, 0],
		[0, 2, 1, 1, -1, -1, 0, -1, 0],
		[1, -1, 1, 2, -1, 1, 1, -1, 0],
		[-1, -1, -1, 0, -1, -1, 0, 1, 4],
		[-4, -4, -3, -4, 1, 2, 1, 1, 10],
		[-3, -3, -3, -3, 1, 1, 1, 1, 8],
		[-2, -2, -1, -2, 0, 1, 0, 1, 5],
		[-1, -2, -2, -2, 1, 0, -1, 1, 6],
		[-2, -2, -2, -1, 0, 1, 1, -1, 6],
		[-3, -3, -2, -1, 1, 1, 1, -1, 7],
		[-3, -3, -2, -2, 1, 1, 1, 0, 7],
		[-2, -3, -2, -2, 1, 1, 0, 1, 6],
		[-1, -1, -1, -1, 0, 1, 0, 0, 3],
		[-1, -1, -1, -1, 0, 0, 0, 1, 3],
		[-1, 0, 0, 1, -2, -1, -1, 1, 3],
		[-2, -1, -2, -2, 1, -1, 0, 1, 6],
		[-3, -4, -3, -2, 1, 2, -1, 1, 9],
		[-3, -2, -3, -3, 1, 0, 1, 1, 8],
		[-1, -1, -1, -1, 1, 0, 0, 0, 3],
		[-5, -5, -4, -4, 2, 2, 1, 1, 12],
		[-4, -5, -4, -5, 1, 2, 1, 2, 12],
		[-5, -6, -4, -6, 1, 3, 1, 2, 14],
		[-2, -3, -2, -3, 0, 1, 1, 1, 7],
		[-1, -1, -1, -1, 0, 0, 1, 0, 3],
		[-2, -2, -2, -1, 1, 1, 0, 0, 5],
		[0, 1, 0, 0, -1, -1, 0, -1, 2]]

	S_T1  = [[0, -1, 0, 0, 0, 0, 0, 0, 1], 
		[-1, 0, 0, 0, 0, 0, 0, 0, 1], 
		[0, 0, -1, 0, 0, 0, 0, 0, 1], 
		[0, -1, -1, -1, -1, 0, 1, 0, 3], 
		[1, 1, 1, 1, -1, -1, -1, -1, 0], 
		[0, 0, 0, -1, 0, 0, 0, 0, 1], 
		[-1, -1, -1, -1, 3, 3, 3, 3, 0], 
		[0, -1, 0, 0, 1, 1, 1, 1, 0], 
		[-1, -1, 0, 0, 2, 2, 2, 1, 0], 
		[-1, -1, 0, 0, 1, 1, 1, 0, 1], 
		[-2, -2, -1, -1, 5, 5, 4, 4, 0], 
		[0, 0, -1, 0, 1, 1, 1, 1, 0], 
		[-1, -2, -1, -1, 1, 1, 0, 1, 3], 
		[-1, 0, 0, 0, 1, 1, 1, 1, 0], 
		[-1, -1, -1, 0, 1, 1, 0, 0, 2], 
		[-1, -1, -1, 0, 3, 3, 2, 2, 0], 
		[0, -1, -1, -1, 2, 3, 2, 3, 0], 
		[0, -1, -1, -1, 1, 2, 1, 2, 1], 
		[-2, -4, -1, -3, 2, 4, 1, 3, 5], 
		[-1, -1, 0, -1, 0, 1, 0, 1, 2], 
		[-1, -1, 0, -1, 2, 3, 2, 2, 0], 
		[-1, -1, 0, -1, 1, 2, 1, 1, 1], 
		[-2, -2, -1, -1, 2, 2, 1, 1, 3], 
		[-1, -3, -1, -2, 2, 3, 1, 3, 3], 
		[-2, -3, -1, -3, 1, 3, 1, 2, 5], 
		[-1, 0, -1, -1, 3, 2, 3, 3, 0], 
		[-1, -2, -1, -2, 1, 2, 1, 2, 3], 
		[-1, -2, -1, -2, 0, 1, 1, 1, 4], 
		[0, -1, 0, -1, 1, 1, 0, 1, 1], 
		[-1, -2, -1, -2, 4, 5, 4, 5, 0], 
		[-1, -3, -1, -2, 5, 6, 4, 6, 0], 
		[-1, -2, -1, -1, 4, 4, 3, 4, 0], 
		[0, 0, 0, -1, 1, 1, 1, 1, 0], 
		[0, -1, 0, -1, 2, 2, 1, 2, 0], 
		[0, 3, 0, 0, -1, -1, -1, -1, 1], 
		[0, 0, 2, 1, -1, -1, -1, -1, 1], 
		[0, 1, 2, 0, -1, -1, -1, -1, 1], 
		[1, 0, 2, 0, -1, -1, -1, -1, 1], 
		[0, 0, 2, 0, -1, -1, -1, 0, 1], 
		[0, 0, 1, 0, 0, -1, 0, -1, 1], 
		[1, 1, 4, 1, -2, -2, -2, -2, 1], 
		[2, -1, 2, -1, -1, -1, -2, -1, 3], 
		[0, -1, -1, -1, 1, 0, -1, 0, 3], 
		[0, -1, 2, -1, -1, -1, -2, 1, 3], 
		[2, -1, 0, -1, 1, -1, -2, -1, 3], 
		[0, -1, 0, -1, 1, -1, -2, 1, 3], 
		[-2, -3, -2, -3, 0, 1, 1, 1, 7], 
		[-1, -2, -1, -2, -1, 0, 1, 1, 5], 
		[-4, -5, -4, -5, 1, 2, 1, 2, 12], 
		[-3, 0, -3, -3, 1, -2, 1, 1, 8], 
		[0, 0, 0, 1, -1, -1, 1, -1, 1], 
		[-1, -1, -1, -1, 0, 0, 1, 0, 3], 
		[0, 0, 0, 0, -1, -1, 1, 0, 1], 
		[0, 0, -1, 0, -1, -1, 2, -1, 2], 
		[0, 1, 0, 0, -1, -1, 1, -1, 1], 
		[1, 0, 0, 0, -1, -1, 1, -1, 1], 
		[-3, -3, -3, -3, 1, 1, 1, 1, 8], 
		[1, 1, 1, 1, -2, -2, -2, 1, 1], 
		[-1, 0, -1, -1, -1, -2, -1, 3, 4], 
		[0, 0, 0, 0, 0, -1, -1, 1, 1], 
		[-1, -1, -1, 0, 0, 0, -1, 1, 3], 
		[0, 0, 1, 0, -1, -1, -1, 1, 1], 
		[0, 1, 0, 0, -1, -1, -1, 1, 1], 
		[0, 0, 0, 0, -1, -1, 0, 1, 1], 
		[-1, -1, -1, -1, 0, 0, 0, 1, 3], 
		[0, 0, 0, 1, -1, -1, -1, 1, 1], 
		[-1, 0, 0, 0, -1, -1, -1, 2, 2], 
		[0, 0, 0, 3, -1, -1, -1, -1, 1], 
		[-1, -1, 0, 0, 1, -1, 1, -2, 3], 
		[-3, -3, -2, 0, 1, 1, 1, -2, 7], 
		[-3, -3, -2, -2, 1, 1, 1, 0, 7], 
		[-1, -1, 0, 1, 0, 0, 0, -1, 2], 
		[-1, -2, -1, -1, 1, 0, -1, 1, 4], 
		[-2, -3, -2, -1, 1, 1, -1, 1, 6],
		[-2, -4, -3, -2, 2, 1, -1, 1, 8], 
		[-2, -3, -2, -2, 1, 1, 0, 1, 6], 
		[-3, -5, -4, -2, 2, 2, -1, 1, 10], 
		[-3, -4, -2, -2, 1, 1, -1, 2, 8], 
		[-2, -2, -2, 0, 1, 1, -1, 0, 5], 
		[-2, -2, -2, 1, 1, 1, -1, -1, 5], 
		[-3, -3, -4, 0, 2, 2, -1, -1, 8], 
		[-1, -1, 1, -1, -1, 0, -1, 1, 3], 
		[-1, -1, 0, -1, -1, 0, 0, 1, 3], 
		[-3, -2, 0, -2, -1, 1, -1, 2, 6], 
		[-4, -4, -3, -4, 1, 2, 1, 1, 10], 
		[1, 1, 1, 1, -2, 1, -2, -2, 1], 
		[0, 0, 0, 0, 0, 0, 0, -1, 1], 
		[1, 0, 0, 0, -1, 0, 0, -1, 1], 
		[-1, -1, -1, 0, 0, 1, -1, 0, 3], 
		[1, 0, 0, 0, 0, 0, -1, -1, 1], 
		[0, 0, 1, 0, -1, 0, -1, 0, 1], 
		[1, 0, 0, 0, -1, 1, -1, -2, 2], 
		[0, 0, -1, 0, -1, 2, -1, -2, 3], 
		[0, 0, -1, 0, 0, 1, -1, -1, 2], 
		[1, 0, 1, 0, -1, 0, -1, -1, 1], 
		[0, 1, 0, 0, -1, 1, -1, -1, 1], 
		[-1, -1, -2, 0, -1, 3, -1, -2, 5], 
		[-1, 0, -1, 0, -1, 2, -1, -1, 3], 
		[0, 0, -1, 0, -1, 1, 0, -1, 2], 
		[-1, -1, -1, -1, 0, 1, 0, 0, 3], 
		[0, 0, 0, 1, -1, 1, -1, -1, 1], 
		[-1, -1, -2, 0, 0, 2, -1, -1, 4], 
		[-1, 0, 0, 0, -1, 1, -1, 0, 2], 
		[-5, -5, -4, -4, 2, 2, 1, 1, 12], 
		[-5, -6, -4, -6, 1, 3, 1, 2, 14], 
		[1, 1, 1, 1, 1, -2, -2, -2, 1], 
		[-1, 0, -1, -1, 3, -2, -1, -1, 4], 
		[0, 0, 0, 0, 1, -1, 0, -1, 1], 
		[0, 0, 0, 0, 1, -1, -1, 0, 1], 
		[1, 0, 0, 0, 1, -1, -1, -1, 1], 
		[0, 0, -1, 0, 2, -1, -1, -1, 2], 
		[0, 1, 0, 0, 1, -1, -1, -1, 1], 
		[-1, -1, -1, -1, 1, 0, 0, 0, 3], 
		[0, 0, 0, 1, 1, -1, -1, -1, 1], 
		[4, 1, 1, 1, -2, -2, -2, -2, 1], 
		[2, 0, 0, 0, -1, -1, 0, -1, 1], 
		[2, 0, 0, 0, 0, -1, -1, -1, 1], 
		[2, 0, 1, 0, -1, -1, -1, -1, 1], 
		[2, 1, 0, 0, -1, -1, -1, -1, 1], 
		[2, 0, 0, 1, -1, -1, -1, -1, 1], 
		[1, 1, 1, 1, -2, -2, 1, -2, 1], 
		[-1, 0, -1, -1, -1, -2, 3, -1, 4], 
		[0, 0, 0, 0, 0, -1, 1, -1, 1]]


	NUMBER = 9

	CP  =  [[0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], 
		[1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
		[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]]

	MR  =  [[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
  




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
			for j in range(0, 32):
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
			for j in range(0, 32):
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

	def VariableRotation(self, variablein):
		"""
		Bit Rotation.
		"""
		eqn = []
		for i in range(0, 64):
			eqn.append(variablein[(i + 16) % 64])
		return eqn



	def ConstraintsBySbox(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer.
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0, 16):
			for coff in Klein.S_T:
				temp = []
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[(4 * k) + u])
				for v in range(0, 4):
					temp.append(str(coff[v + 4]) + " " + variable2[(4 * k) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Klein.NUMBER - 1])
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
			for coff in Klein.S_T1:
				temp = []
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[(4 * k) + u])
				for v in range(0, 4):
					temp.append(str(coff[v + 4]) + " " + variable2[(4 * k) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Klein.NUMBER - 1])
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
		variable4 = Klein.CreateVariables9(i)
		variable5 = Klein.CreateVariables10(i)
		variable6 = Klein.CreateVariables11(i)
		variable7 = Klein.CreateVariables12(i)
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
		for coff in Klein.CP:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,32):
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,32):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(0)
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
			count += 1
                        fileobj.write("\n")
		count = 32
		for coff in Klein.CP:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,32):
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " <= " + s
                        fileobj.write(temp1)
			fileobj.write("\n")
			for v in range(0,32):
				temp = []
				temp.append(str(1) + " " + variable1[count])
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
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
		for coff in Klein.CP:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,32):
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 32
		for coff in Klein.CP:
			temp = []
			temp.append(str(1) + " " + variable1[count])
			for v in range(0,32):
				temp.append(str(-coff[v]) + " " + variable2[(count * 32) + v])
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
		for coff in Klein.MR:
			temp = []
			temp.append(str(-1) + " " + variable2[count])
			for v in range(0,32):
				temp.append(str(coff[v]) + " " + variable1[count + (v * 32)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		count = 0
		for coff in Klein.MR:
			temp = []
			temp.append(str(-1) + " " + variable2[count + 32])
			for v in range(0,32):
				temp.append(str(coff[v]) + " " + variable1[(32 * 32) + count + (v * 32)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(0)
			temp1 += " = " + s
                        count += 1
			fileobj.write(temp1)
			fileobj.write("\n")
		
	def Constraint(self):
		"""
		Generate the constraints used in the MILP model.
		"""
		assert(self.Round >= 1)
		fileobj = open(self.filename_model, "a")
		fileobj.write("Subject To\n")
		fileobj.close()
		
		for i in range(1, (self.Round+1)):
			variablein = Klein.CreateVariables4(i-1)
			variableout = Klein.CreateVariables5(i-1)  
                        self.ConstraintsBySbox1(variablein, variableout)
			variablein2 = self.VariableRotation(variableout) 
			variableout= Klein.CreateVariables6(i-1)
                        self.ConstraintsByCopy1(variablein2, variableout)
                        variablein =  Klein.CreateVariables6(i-1)
                        variableout = Klein.CreateVariables4(i)
                        self.ConstraintsByMixrow(variablein, variableout) 
                       
	def VariableBinary(self):
		"""
		Specify the variable type.
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Binary\n")
		
		for i in range(0, (self.Round + 1)):
			for j in range(0, 64):
				fileobj.write("x1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		
                
		for i in range(0, self.Round):
			for j in range(0, 64):
				fileobj.write("y1_" + str(i) + "_" + str(j))
                                fileobj.write("\n")
                for i in range (0, self.Round):
			for j in range(0, 64):
         			for k in range(0,32):
					fileobj.write("y1_" + str(i) + "_" + str(j) + "_" + str(k))
					fileobj.write("\n")
		fileobj.write("END")
		fileobj.close()

	def Init(self):
		"""
		Generate the constraints introduced by the initial division property.
		"""
		variableout = Klein.CreateVariables4(0)
		fileobj = open(self.filename_model, "a")
		temp = []
		for i in range(0, 1):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(1, 45):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(45, 47):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(47, 64):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                fileobj.close()
		
		#variableout = Klein.CreateVariables4(self.Round)
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



		  


	
