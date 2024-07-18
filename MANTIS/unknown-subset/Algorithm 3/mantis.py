from gurobipy import *

import time

class Mantis:
   def __init__(self, Round1, Round2, activebits):
		self.Round1 = Round1
		self.Round2 = Round2
		self.activebits = activebits
		self.blocksize = 64
		self.filename_model = "Mantis_" + str(self.Round1+self.Round2) + "_" + str(self.activebits) + ".lp"
		self.filename_result = "result_" + str(self.Round1+self.Round2) + "_" + str(self.activebits) + ".txt"
		fileobj = open(self.filename_model, "w")
		fileobj.close()
		fileboj = open(self.filename_result, "w")
		fileobj.close()



   S_T=[[1, 1, 4, 1, -2, -2, -2, -2, 1],
	[0, 0, -3, 0, 1, 1, -2, 1, 2],
	[0, 0, 0, 0, -1, -1, 2, -1, 1],
	[-1, -1, 0, -1, 2, 2, 2, 2, 0],
	[0, -1, 0, -1, 0, 1, 1, 1, 1]]

   S_T1=[[1, 2, 3, 1, 0, -1, -1, -2, 0],
	[0, 1, -1, 1, 1, 0, -1, 1, 0],
	[-1, -1, 0, -1, 2, 2, 2, 2, 0],
	[-1, -2, 0, 0, -1, -1, 2, -1, 4],
	[2, -1, 0, 1, -1, 0, 2, 1, 0],
	[0, 2, 1, 1, -1, -1, -3, -2, 3],
	[-1, -3, -3, -2, 0, 2, -1, 1, 7],
	[0, 0, -1, 0, -1, -1, 0, 1, 2],
	[1, -2, 2, 3, 1, -1, 3, -1, 0],
	[-1, 0, -1, -2, 2, -2, -1, -1, 6],
	[0, 1, 1, 0, -1, 1, 1, 1, 0],
	[1, 1, -1, -1, 2, 1, 1, 1, 0],
	[0, 0, -2, 1, -1, -1, -1, 1, 3],
	[-2, -1, -1, -1, -1, 1, 1, -1, 5],
	[0, 1, 1, 0, 0, -1, -1, -1, 1],
	[0, 0, 1, 1, 0, 0, 0, -1, 0],
	[1, -1, 1, 0, 0, 0, 1, 1, 0],
	[-1, 1, 0, 1, 1, 1, 0, 0, 0]]

   MX0=[[0, 1, 1, 1, -1, -1, -1, -1, 1], 
	[0, 0, 0, 1, -1, -1, -1, 0, 2],
	[0, 0, 1, 0, -1, -1, 0, -1, 2], 
	[0, 1, 0, 0, -1, 0, -1, -1, 2], 
	[0, -1, -1, -1, 1, 0, 0, 0, 2], 
	[0, 1, 0, 1, 0, -1, 0, -1, 1], 
	[0, -1, -1, 0, 0, 1, 1, 0, 1], 
	[0, 0, -1, -1, 0, 0, 1, 1, 1], 
	[0, -1, 0, 0, 1, 0, 1, 1, 0], 
	[0, 0, -1, 0, 1, 1, 0, 1, 0], 
	[0, -1, 0, -1, 0, 1, 0, 1, 1], 
	[0, -1, -1, -1, 1, 1, 1, 1, 0], 
	[0, 0, 1, 1, 0, 0, -1, -1, 1], 
	[0, 1, 1, 1, -1, 0, 0, 0, 0], 
	[0, 0, 0, -1, 1, 1, 1, 0, 0], 
	[0, 1, 1, 0, 0, -1, -1, 0, 1],
	[1, 1, 1, 1, -1, -1, -1, -1, 0],
	[-1, -1, -1, -1, 1, 1, 1, 1, 0]]
  
   MX1=[[-1, -1, -1, -1, 1, 1, 1, 1, 0], 
	[0, 0, 0, 1, -1, -1, -1, 0, 2], 
	[0, 0, 1, 0, -1, -1, 0, -1, 2], 
	[1, 0, 0, 0, 0, -1, -1, -1, 2], 
	[0, 1, 0, 0, -1, 0, -1, -1, 2], 
	[-1, 0, -1, 0, 1, 0, 1, 0, 1], 
	[-1, -1, 0, 0, 1, 1, 0, 0, 1], 
	[0, -1, 0, -1, 0, 1, 0, 1, 1], 
	[0, -1, -1, 0, 0, 1, 1, 0, 1], 
	[1, 1, 0, 1, 0, 0, -1, 0, 0], 
	[-1, 0, 0, -1, 1, 0, 0, 1, 1], 
	[1, 0, 1, 1, 0, -1, 0, 0, 0],
	[0, 0, -1, -1, 0, 0, 1, 1, 1], 
	[1, 1, 1, 0, 0, 0, 0, -1, 0], 
	[0, 1, 1, 1, -1, 0, 0, 0, 0]]



   NUMBER = 9 


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
   def CreateVariables3(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("p" + "_" + str(n) + "_" + str(i)))
		return arrays

   @staticmethod
   def CreateVariables2(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("y" + "_" + str(n) + "_" + str(i)))
		return arrays

   
   @staticmethod
   def CreateVariables4(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z" + "_" + str(n) + "_" + str(i)))
		return arrays

   @staticmethod
   def CreateVariables5(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("x1" + "_" + str(n) + "_" + str(i)))
		return arrays

   @staticmethod
   def CreateVariables6(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("y1" + "_" + str(n) + "_" + str(i)))
		return arrays

   
   @staticmethod
   def CreateVariables7(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z1" + "_" + str(n) + "_" + str(i)))
		return arrays

   @staticmethod
   def CreateVariables8(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z2" + "_" + str(n) + "_" + str(i)))
		return arrays

   
   @staticmethod
   def CreateVariables9(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z3" + "_" + str(n) + "_" + str(i)))
		return arrays

   @staticmethod
   def CreateVariables10(n):
		"""
		Generate the variables used in the model.
		"""
		arrays = []
		for i in range(0, 64):
			arrays.append(("z4" + "_" + str(n) + "_" + str(i)))
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
			eqn.append("x" + "_" + str(self.Round1 + self.Round2 + 1) + "_" + str(i))
		temp = " + ".join(eqn)
		fileobj.write(temp)
		fileobj.write("\n")
		fileobj.close()


   def ConstraintsBySbox(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer(0-subset)
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,16):
			for coff in Mantis.S_T:
				temp = []
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[(k * 4) + 3 - u])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[(k * 4) + 3 - v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 


   def ConstraintsBySbox1(self, variable1, variable2):
		"""
		Generate the constraints by sbox layer(1-subset)
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,16):
			for coff in Mantis.S_T1:
				temp = []
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[(k * 4) + 3 - u])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[(k * 4) + 3 - v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 

		"""

   def ConstraintsBySinverse(self, variable1, variable2):
		"""
		#Generate the constraints by sbox layer(0-subset)
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,16):
			for coff in Mantis.S_I:
				temp = []
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[(k * 4) + 3 - u])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[(k * 4) + 3 - v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 


   def ConstraintsBySinverse1(self, variable1, variable2):
		"""
		#Generate the constraints by sbox layer(1-subset)
		"""
		fileobj = open(self.filename_model,"a")
		for k in range(0,16):
			for coff in Mantis.S_I1:
				temp = []
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[(k * 4) + 3 - u])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[(k * 4) + 3 - v])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 
		"""

   def ConstraintsByMix(self, variable1, variable2):

		fileobj = open(self.filename_model,"a")
		for k in range(0, 4):
			for coff in Mantis.MX0:
				temp=[]
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[0 + (4 * (3 - u)) + (16 * k)])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[0 + (4 * (3 - v)) + (16 * k)])
				temp1 = []
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")

			for coff in Mantis.MX0:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		
			for coff in Mantis.MX0:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")

			for coff in Mantis.MX0:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		fileobj.close(); 
		"""
		for coff in Mantis.MX04:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX01:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX02:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX03:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX04:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX01:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX02:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX03:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX01:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			
		for coff in Mantis.MX02:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v)  + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
	
		for coff in Mantis.MX03:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX04:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		fileobj.close(); 

    
   def ConstraintsByMix1(self, variable1, variable2):


		fileobj = open(self.filename_model,"a")
		for coff in Mantis.MX11:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u)])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			
		for coff in Mantis.MX12:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u)])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
	
		for coff in Mantis.MX13:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u)])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX14:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u)])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v)])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX14:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX11:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX12:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX13:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 16])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 16])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX14:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX11:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX12:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX13:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 32])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 32])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX11:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[0 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[0 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
			
		for coff in Mantis.MX12:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v)  + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
	
		for coff in Mantis.MX13:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")

		for coff in Mantis.MX14:
			temp=[]
			for u in range(0, 4):
				temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + 48])
			for v in range(0, 4):
				temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + 48])
			temp1 = " + ".join(temp)
			temp1 = temp1.replace("+ -", "- ")
			s = str(-coff[Mantis.NUMBER - 1])
			s = s.replace("--", "")                                      
			temp1 += " >= " + s
			fileobj.write(temp1)
			fileobj.write("\n")
		fileobj.close(); 
	"""

   def ConstraintsByMix1(self, variable1, variable2):

		fileobj = open(self.filename_model,"a")
		for k in range(0, 4):
			for coff in Mantis.MX1:
				temp=[]
				for u in range(0,4):
					temp.append(str(coff[u]) + " " + variable1[0 + (4 * (3 - u)) + (16 * k)])
				for v in range(0,4):
					temp.append(str(coff[v + 4]) + " " + variable2[0 + (4 * (3 - v)) + (16 * k)])
				temp1 = []
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")

			for coff in Mantis.MX1:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[1 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[1 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")
		
			for coff in Mantis.MX1:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[2 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[2 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
				s = s.replace("--", "")                                      
				temp1 += " >= " + s
				fileobj.write(temp1)
				fileobj.write("\n")

			for coff in Mantis.MX1:
				temp=[]
				for u in range(0, 4):
					temp.append(str(coff[u]) + " " + variable1[3 + 4 * (3 - u) + (16 * k)])
				for v in range(0, 4):
					temp.append(str(coff[v+4]) + " " + variable2[3 + 4 * (3 - v) + (16 * k)])
				temp1 = " + ".join(temp)
				temp1 = temp1.replace("+ -", "- ")
				s = str(-coff[Mantis.NUMBER - 1])
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
			temp.append(str(64) + " " + variable2[k])
		for k in range(0, 64):
			temp.append(str(-63) + " " + variable1[k])
		temp1 = " + ".join(temp)
		temp1 = temp1.replace("+ -", "- ")
		s = str(64)
		temp1 += " >= " + s
		fileobj.write(temp1)
		fileobj.write("\n")
  		fileobj.close()

   def ConstraintsByAssign(self, variable1, variable2, variable3, i):

		fileobj = open(self.filename_model,"a")
		variable4 = Mantis.CreateVariables9(i)
		variable5 = Mantis.CreateVariables10(i)
		variable6 = Mantis.CreateVariables11(i)
		variable7 = Mantis.CreateVariables12(i)
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

   @staticmethod
   def LinearLaryer(variable):
		"""
		Shuffle-Cell of Midori
		"""
		array = ["" for i in range(0,64)]
		for i in range(0, 4):
			array[i] = variable[i]
		for i in range(4, 8):
			array[i] = variable[(10 * 4) + (i - 4)]
		for i in range(8, 12):
 			array[i] = variable[(5 * 4) + (i - 8)]
		for i in range(12, 16):
			array[i] = variable[(15 * 4) + (i - 12)]
		for i in range(16, 20):
			array[i] = variable[(14 * 4) + (i - 16)]
		for i in range(20, 24):
			array[i] = variable[(4 * 4) + (i -20)]
		for i in range(24, 28):
			array[i] = variable[(11 * 4) + (i -24)]
		for i in range(28, 32):
			array[i] = variable[(1 * 4) + (i -28)]
		for i in range(32, 36):
			array[i] = variable[(9 * 4) + (i - 32)]
		for i in range(36, 40):
			array[i] = variable[(3 * 4) + (i - 36)]
		for i in range(40, 44):
			array[i] = variable[(12 * 4) + (i - 40)]
		for i in range(44, 48):
			array[i] = variable[(6 * 4) + (i - 44)]
		for i in range(48, 52):
			array[i] = variable[(7 * 4) + (i - 48)]
		for i in range(52, 56):
			array[i] = variable[(13 * 4) + (i - 52)]
		for i in range(56, 60):
			array[i] = variable[(2 * 4) + (i - 56)]
		for i in range(60, 64):
			array[i] = variable[(8 * 4) + (i - 60)]


		"""
   		for k in range(0, 4):
			array[0 + (16*k)] = variable[0 + (16*k)]
			array[1 + (16*k)] = variable[5 + (16*k)]
			array[2 + (16*k)] = variable[10 + (16*k)]
			array[3 + (16*k)] = variable[15 + (16*k)]
			array[4 + (16*k)] = variable[4 + (16*k)]
			array[5 + (16*k)] = variable[9 + (16*k)]
			array[6 + (16*k)] = variable[14 + (16*k)]
			array[7 + (16*k)] = variable[3 + (16*k)]
			array[8 + (16*k)] = variable[8 + (16*k)]
			array[9 + (16*k)] = variable[13 + (16*k)]
			array[10 + (16*k)] = variable[2 + (16*k)]
			array[11 + (16*k)] = variable[7 + (16*k)]
			array[12 + (16*k)] = variable[12 + (16*k)]
			array[13 + (16*k)] = variable[1 + (16*k)]
			array[14 + (16*k)] = variable[6 + (16*k)]
			array[15 + (16*k)] = variable[11 + (16*k)]
		"""
		return array

   @staticmethod
   def LinearLaryerInverse(variable):
		"""
		Shuffle-Cell of Midori
		"""
		array = ["" for i in range(0,64)]
		for i in range(0, 4):
			array[i] = variable[i]
		for i in range(4, 8):
			array[i] = variable[(7 * 4) + (i - 4)]
		for i in range(8, 12):
 			array[i] = variable[(14 * 4) + (i - 8)]
		for i in range(12, 16):
			array[i] = variable[(9 * 4) + (i - 12)]
		for i in range(16, 20):
			array[i] = variable[(5 * 4) + (i - 16)]
		for i in range(20, 24):
			array[i] = variable[(2 * 4) + (i -20)]
		for i in range(24, 28):
			array[i] = variable[(11 * 4) + (i -24)]
		for i in range(28, 32):
			array[i] = variable[(12 * 4) + (i -28)]
		for i in range(32, 36):
			array[i] = variable[(15 * 4) + (i -32)]
		for i in range(36, 40):
			array[i] = variable[(8 * 4) + (i - 36)]
		for i in range(40, 44):
			array[i] = variable[(1 * 4) + (i - 40)]
		for i in range(44, 48):
			array[i] = variable[(6 * 4) + (i - 44)]
		for i in range(48, 52):
			array[i] = variable[(10 * 4) + (i - 48)]
		for i in range(52, 56):
			array[i] = variable[(13 * 4) + (i - 52)]
		for i in range(56, 60):
			array[i] = variable[(4 * 4) + (i - 56)]
		for i in range(60, 64):
			array[i] = variable[(3 * 4) + (i - 60)]		

		"""
   		for k in range(0, 4):
			array[0 + (16*k)] = variable[0 + (16*k)]
			array[1 + (16*k)] = variable[13 + (16*k)]
			array[2 + (16*k)] = variable[10 + (16*k)]
			array[3 + (16*k)] = variable[7 + (16*k)]
			array[4 + (16*k)] = variable[4 + (16*k)]
			array[5 + (16*k)] = variable[1 + (16*k)]
			array[6 + (16*k)] = variable[14 + (16*k)]
			array[7 + (16*k)] = variable[11 + (16*k)]
			array[8 + (16*k)] = variable[8 + (16*k)]
			array[9 + (16*k)] = variable[5 + (16*k)]
			array[10 + (16*k)] = variable[2 + (16*k)]
			array[11 + (16*k)] = variable[15 + (16*k)]
			array[12 + (16*k)] = variable[12 + (16*k)]
			array[13 + (16*k)] = variable[9 + (16*k)]
			array[14 + (16*k)] = variable[6 + (16*k)]
			array[15 + (16*k)] = variable[3 + (16*k)]
		"""
		return array

   def Constraint(self):
		"""
		Generate the constraints used in the MILP model.
		"""
		assert(self.Round1 >= 1)
		assert(self.Round2 >= 1)
		fileobj = open(self.filename_model, "a")
		fileobj.write("Subject To\n")
		fileobj.close()
		#variablein = Mantis.CreateVariables5(0)
		#variableout = Mantis.CreateVariables8(0)  
		#self.ConstraintsBySucc(variablein, variableout)
		#variablein1 = Mantis.CreateVariables1(0)
		#variablein2 = Mantis.CreateVariables8(0)
		#variableout = Mantis.CreateVariables2(0)
		#self.ConstraintsByAssign(variablein1, variablein2, variableout, 0)   
		variablein = Mantis.CreateVariables1(0)
		variableout = Mantis.CreateVariables2(0)  
                self.ConstraintsBySbox(variablein, variableout)
		variablein = Mantis.CreateVariables5(0)
		variableout = Mantis.CreateVariables6(0)  
                self.ConstraintsBySbox1(variablein, variableout)
		for i in range(1, self.Round1 + 1):
			variablein1 = Mantis.CreateVariables6(i-1)
			variableout = Mantis.CreateVariables8(i-1)
			self.ConstraintsBySucc(variablein1, variableout)
			variablein1 = Mantis.CreateVariables8(i-1)
			variablein2 = Mantis.CreateVariables2(i-1)
			variableout = Mantis.CreateVariables3(i-1)
			self.ConstraintsByAssign(variablein1, variablein2, variableout, i-1)
			variablein = Mantis.LinearLaryer(variableout)
			variableout = Mantis.CreateVariables1(i)  
                        self.ConstraintsByMix(variablein, variableout)
			variablein = Mantis.LinearLaryer(variablein1)
			variableout = Mantis.CreateVariables5(i)  
                        self.ConstraintsByMix1(variablein, variableout)
			variablein = Mantis.CreateVariables1(i)
			variableout = Mantis.CreateVariables2(i)  
                	self.ConstraintsBySbox(variablein, variableout)
			variablein = Mantis.CreateVariables5(i)
			variableout = Mantis.CreateVariables6(i)  
                	self.ConstraintsBySbox1(variablein, variableout)
		variablein = Mantis.CreateVariables2(self.Round1)
		variableout = Mantis.CreateVariables4(self.Round1) 
		self.ConstraintsByMix(variablein, variableout)
		variablein = Mantis.CreateVariables6(self.Round1)
		variableout =  Mantis.CreateVariables7(self.Round1) 
		self.ConstraintsByMix1(variablein, variableout)
		variablein = Mantis.CreateVariables4(self.Round1) 
		variableout = Mantis.CreateVariables1(self.Round1+1)
		self.ConstraintsBySbox(variablein, variableout)
		variablein = Mantis.CreateVariables7(self.Round1) 
		variableout = Mantis.CreateVariables5(self.Round1+1)
		self.ConstraintsBySbox1(variablein, variableout)
		#variablein = Mantis.CreateVariables5(self.Round1+1)
		#variableout = Mantis.CreateVariables8(self.Round1+1)  
		#self.ConstraintsBySucc(variablein, variableout)
		#variablein1 = Mantis.CreateVariables1(self.Round1+1)
		#variablein2 = Mantis.CreateVariables8(self.Round1+1)
		#variableout = Mantis.CreateVariables2(self.Round1+1)
		#self.ConstraintsByAssign(variablein1, variablein2, variableout, self.Round1+1)   
		for i in range(self.Round1+1, self.Round1+self.Round2+1):
			variablein = Mantis.CreateVariables1(i)
			variableout1 = Mantis.CreateVariables2(i)
			self.ConstraintsByMix(variablein, variableout1)
			variablein = Mantis.CreateVariables5(i)
			variableout = Mantis.CreateVariables6(i)
			self.ConstraintsByMix1(variablein, variableout)
			variablein1 = Mantis.LinearLaryerInverse(variableout)
			variableout = Mantis.CreateVariables8(i)  
			self.ConstraintsBySucc(variablein1, variableout)
			variablein2 = Mantis.LinearLaryerInverse(variableout1)
			variablein3 = variableout
			variableout = Mantis.CreateVariables3(i)
			self.ConstraintsByAssign(variablein2, variablein3, variableout, i)
			variablein = Mantis.CreateVariables3(i)
			variableout = Mantis.CreateVariables1(i+1)
			self.ConstraintsBySbox(variablein, variableout)
			variableout = Mantis.CreateVariables5(i+1)
			self.ConstraintsBySbox1(variablein1, variableout)
			"""
			variablein = Mantis.CreateVariables5(i+1)
			variableout = Mantis.CreateVariables8(i+1)
			self.ConstraintsBySucc(variablein, variableout)
			variablein1 = Mantis.CreateVariables8(i+1)
			variablein2 = Mantis.CreateVariables1(i+1)
			variableout = Mantis.CreateVariables2(i+1)
			self.ConstraintsByAssign(variablein1, variablein2, variableout, i+1)
			"""

   def VariableBinary(self):
		"""
		Specify the variable type.
		"""
		fileobj = open(self.filename_model, "a")
		fileobj.write("Binary\n")
		for i in range(0, (self.Round1 + self.Round2 + 2)):
			for j in range(0, 64):
				fileobj.write("x_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round1 + self.Round2 + 2)):
			for j in range(0, 64):
				fileobj.write("x1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for j in range(0, 64):
			fileobj.write("z1_" + str(self.Round1) + "_" + str(j))
			fileobj.write("\n")
		for j in range(0, 64):
			fileobj.write("z_" + str(self.Round1) + "_" + str(j))
			fileobj.write("\n")
		for i in range(0, self.Round1):
			for j in range(0, 64):
				fileobj.write("z2_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(self.Round1 + 1, self.Round1 + self.Round2 + 1):
			for j in range(0, 64):
				fileobj.write("z2_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, self.Round1):
			for j in range(0, 64):
				fileobj.write("z3_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(self.Round1 + 1, self.Round1 + self.Round2 + 1):
			for j in range(0, 64):
				fileobj.write("z3_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, self.Round1):
			for j in range(0, 64):
				fileobj.write("z4_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(self.Round1 + 1, self.Round1 + self.Round2 + 1):
			for j in range(0, 64):
				fileobj.write("z4_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, self.Round1):
			fileobj.write("b_" + str(i))
			fileobj.write("\n")
		for i in range(self.Round1+1, (self.Round1 + self.Round2 + 1)):
			fileobj.write("b_" + str(i))
			fileobj.write("\n")
		for i in range(0, self.Round1):
			fileobj.write("c_" + str(i))
			fileobj.write("\n")
		for i in range(self.Round1+1, (self.Round1 + self.Round2 + 1)):
			fileobj.write("c_" + str(i))
			fileobj.write("\n")
		for i in range(0, (self.Round1 + self.Round2 + 1)):
			for j in range(0, 64):
				fileobj.write("y_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, (self.Round1 + self.Round2 + 1)):
			for j in range(0, 64):
				fileobj.write("y1_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(0, self.Round1):
			for j in range(0, 64):
				fileobj.write("p_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		for i in range(self.Round1 + 1, self.Round1 + self.Round2 + 1):
			for j in range(0, 64):
				fileobj.write("p_" + str(i) + "_" + str(j))
				fileobj.write("\n")
		fileobj.write("END")
		fileobj.close()

   def Init(self):
		"""
		Generate the constraints introduced by the initial division property.
		"""
		variableout = Mantis.CreateVariables5(0)
		fileobj = open(self.filename_model, "a")
		temp = []
		for i in range(0, 1):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(1, 2):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(2, 24):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(24, 40):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(40, 48):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(48, 56):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                for i in range(56, 64):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
                #for i in range(60, 64):
		#	temp = variableout[i] + " = 0"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
                #for i in range(64, 66):
		#	temp = variableout[i] + " = 1"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		#for i in range(66, 96):
		#	temp = variableout[i] + " = 1"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		fileobj.close()
		variableout = Mantis.CreateVariables1(0)
		fileobj = open(self.filename_model, "a")
		temp = []
		for i in range(0, 64):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		fileobj.close()
		
		variableout = Mantis.CreateVariables1(self.Round1+self.Round2+1)
		fileobj = open(self.filename_model, "a")
		temp = []
		for i in range(0, 1):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(1, 2):
			temp = variableout[i] + " = 1"
			fileobj.write(temp)
			fileobj.write("\n")
		for i in range(2, 64):
			temp = variableout[i] + " = 0"
			fileobj.write(temp)
			fileobj.write("\n")
	
		#for i in range(33, 96):
		#	temp = variableout[i] + " = 0"
		#	fileobj.write(temp)
		#	fileobj.write("\n")
		fileobj.close()
	        
                             
   def MakeModel(self):
		"""
		Write the MILP model into the file
		"""
		#self.CreateObjectiveFunction()
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














