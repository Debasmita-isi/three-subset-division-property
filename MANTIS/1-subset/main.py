# Algorithm 3 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS

from mantis import Mantis

if __name__ == "__main__":

	ROUND1 = int(raw_input("Input the target forward round number: "))
	ROUND2 = int(raw_input("Input the target backward round number: "))
	while not (ROUND1 + ROUND2 > 0):
		print ("Input a round number greater than 0.")
		ROUND1 = int(raw_input("Input the target round number again: "))
		ROUND2 = int(raw_input("Input the target round number again: "))

	ACTIVEBITS = int(raw_input("Input the number of acitvebits: "))
	while not (ACTIVEBITS < 64 and ACTIVEBITS > 0):
		print ("Input a number of activebits with range (0, 128):")
		ACTIVEBITS = int(raw_input("Input the number of acitvebits again: "))

	mantis = Mantis(ROUND1, ROUND2, ACTIVEBITS)

	mantis.MakeModel()

	mantis.SolveModel_1()
