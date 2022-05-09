import random

def primary():

  f = open("quotes.txt", "r")
  quotes = f.readlines()
  f.close()

  f = open("quotes.txt", "a")
  f.write("New quote")
  f.close()

  last = 14
  rnd1 = random.randint(0, last)

  print(quotes[rnd1], end='')

if __name__== "__main__":
 primary()
