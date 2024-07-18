

from klein import Klein

if __name__ == "__main__":

	ROUND = int(raw_input("Input the target round number: "))
	while not (ROUND > 0):
		print "Input a round number greater than 0."
		ROUND = int(raw_input("Input the target round number again: "))

	ACTIVEBITS = int(raw_input("Input the number of acitvebits: "))
	while not (ACTIVEBITS <= 64 and ACTIVEBITS > 0):
		print "Input a number of activebits with range (0, 128):"
		ACTIVEBITS = int(raw_input("Input the number of acitvebits again: "))

	klein = Klein(ROUND, ACTIVEBITS)

	klein.MakeModel()

	klein.SolveModel()
