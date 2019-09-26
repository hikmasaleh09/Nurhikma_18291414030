class Hewan(object):
	def __init__ (self, a, k,c ):
		self.Anjing= a
		self.kucing = k
		self.cendrawasih = c

	def jumlahHewan(self):
		return self.anjing + self.kucing + self.cendrawasih

	def cetakData(self):
		print("Anjing\t: ", self.anjing)
		print("Kucing\t: ", self.kucing)
		print("Cendrawasih\t: ", self.cendrawasih)

	def cetakJH(self):
		print("Total dari semua hewan diatas\t= ", self.jumlahHewan())

class WarnaHewan(Hewan):
	def __init__(self, a, k, c, w):
		self.anjing = a 
		self.kucing = k 
		self.cendrawasih = c
		self.warna = w 
	def cetakData(self):
		print("Anjing\t: ", self.anjing)
		print("Kucing\t: ", self.kucing)
		print("Cendrawasih\t: ", self.cendrawasih)
		print("Warna dari semua hewan tersebut adalah", self.warna)

def main():
	wh1 = WarnaHewan (17, 3, 20, "Putih")

	wh1.cetakData()
	wh1.cetakJH()

if __name__ == "__main__":
	main()
