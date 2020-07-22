class Complex():

#constructor for initializing complex numbers

	def __init__(self,real,complex_):

		self.real = real
		self.complex_ = complex_

		if complex_ < 0:
			self.complex_number = str(real) + " - "+ str(-1 * complex_) + "i"

		elif complex_>0:
			self.complex_number = str(real) + " + "  + str(complex_) + "i"

		else:
			self.complex_number = str(real)

#method to display complex number

	def display(self):

		print(self.complex_number)

#method to add a complex number

	def add(self,number):

		real = self.real + number.real
		complex_ = self.complex_ + number.complex_
		return Complex(real,complex_)

#method to subtract a complex number

	def sub(self,number):

		real = self.real - number.real
		complex_ = self.complex_ - number.complex_
		return Complex(real,complex_)

#method to find conjugate of complex number

	def conjucate(self):

		real = self.real
		complex_ = self.complex_ * (-1)
		return Complex(real, complex_)

#method to find modulus of complex number upto 2 decimals

	def mod(self):

		real = self.real
		complex_ = self.complex_
		modulus = (real*real + complex_*complex_)**0.5
		modulus = round(modulus,2)
		return Complex(modulus, 0)

#method to mutliply a complex number

	def multi(self,number):

		real = self.real*number.real - self.complex_*number.complex_
		complex_ = self.real*number.complex_ + self.complex_*number.real
		return Complex(real,complex_)

#method to find inverse of a complex number

	def inverse(self):

		deno = (self.real)**2 + (self.complex_)**2
		real = self.real/deno
		real = round(real,4)
		complex_ = (-1)*self.complex_/deno
		complex_ = round(complex_,4)
		return Complex(real,complex_)


a = Complex(1,2)
print("Complex number a is :", end = " ")
a.display()
b = Complex(2,-3)
print("Complex number b is :", end = " ")
b.display()
c = b.add(a)
print("Complex number c is addition of a and b. The value of c is: ", end=" ") 
c.display()
d = b.sub(a)
print("Complex number d is subtraction of a from b. The value of d is: ", end=" ") 
d.display()
print("Conjucate of Complex number  d is :", end=" ")
d.conjucate().display()
print("Modulus of Complex number d is:", end=" ")
d.mod().display()
e = b.multi(a)
print("Multiplication of complex number a and b is e. The value of e is:", end=" ")
e.display()
print("Inverse of Complex number d is :", end = " ")
d.inverse().display()

