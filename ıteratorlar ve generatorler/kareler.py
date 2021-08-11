class Kareler():
    def __init__(self,max):
        self.max = max
        self.sayi = 1
    def __iter__(self):
        return self
    def __next__(self):
        if (self.sayi <= self.max):
            sonuc = 2 ** self.sayi
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration
kareler = Kareler(5)
for i in kareler:
    print(i)
