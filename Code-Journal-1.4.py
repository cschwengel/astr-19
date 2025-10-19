#Connor Schwengel
#10/18/2025


class Hedgehog:
	def __init__(self, name, leg_length, eye_number, tail, furry):
		self.name=name
		self.leg_length=float(leg_length)
		self.eye_number=int(eye_number)
		self.tail=bool(tail)
		self.furry=bool(furry)

	def describe(self):
		print("The", self.name, "has legs that are", self.leg_length, "centimeters long.")
		print("It has", self.eye_number, "eyes,")
		if self.tail:
			print("and has a tail.")
		else:
			print("and does not have a tail.")
		if self.furry:
			print("It is furry.")
		else:
			print("It is not furry.")

def main():
	Hedgehog1=Hedgehog("Hedgehog",10,2,True,False)
	Hedgehog1.describe()


if __name__ == "__main__":
	main()