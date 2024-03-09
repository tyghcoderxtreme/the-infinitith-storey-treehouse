from time import sleep
book = 1
year = 2011
print("Mathematically figuring out every treehouse book from now till infinity\n...")
while True:
    booknum = book * 13
    print("Book "+str(book)+": The "+str(booknum)+"-Storey Treehouse, written by Andy Griffiths and illustrated by Terry Denton, released in",str(year))
    sleep(0.5)
    book = book + 1
    year = year + 1