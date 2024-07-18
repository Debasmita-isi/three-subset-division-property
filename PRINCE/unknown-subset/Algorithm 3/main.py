
from prince import Prince

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

	prince = Prince(ROUND1, ROUND2, ACTIVEBITS)

	prince.MakeModel()

	prince.SolveModel_1()
