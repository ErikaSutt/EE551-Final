import csv
import sys

bks = open(r'BookData\books.csv')
reader = csv.DictReader(bks)
tag = open(r'BookData\tags.csv')
readertg = csv.DictReader(tag)
bktag = open(r'BookData\book_tags.csv')
readbktg = csv.DictReader(bktag)

tagid=[]
grbkid=[]
names=[]

repeat = 1


#while repeat == 1:
author = None
book = None
genre = None
yr1 = None
yr2 = None

print('###############################################################################') 
print('Hello, welcome to a library of 10,000 books. Here you can: \n')
print('1: Look up all books in the library that were published in a range of years.\n')
print('2: Search the library for books published by the same author.\n')
print('3: Search the library for a book title.\n')
print('4: Search the library for all books that fall under a specific genre.\n')
print('Q: Press Q to quit!\n')
print('###############################################################################') 
ch = raw_input("Enter your choice: ")

if ch == '1':
    yr1 = ''
    yr2 = ''
    yr1 = raw_input('Enter the beginning year: ')
    yr2 = raw_input('Enter the end year: ')
    count1 = 0
    for rows in reader:
        if yr1 <= rows['year'] <= yr2:
            count1 = count1 + 1
            print'Title:', rows['title'], '; Average Rating:', rows['average_rating']
    if count1 == 1: print'Found', count1, 'book written between years', yr1, 'and', yr2
    else: print'Found', count1, 'books written between years', yr1, 'and', yr2
elif ch == '2':
    author = raw_input('Enter the full name of the author to search for: ')
    count = 0
    for row in reader:
        if author in row['authors']:
            count = count + 1
            print'Title:', row['title'], '; Average Rating:', row['average_rating']
    if count == 1: print'Found', count, 'book written by', author
    else: print'Found', count, 'books written by', author
elif ch == '3':
    book = raw_input('Enter the name of the book to search for (the titles are case sensitive!): ')
    count2 = 0
    for row in reader:
        if book in row['title']:
            count2 = count2 + 1
            print'Title:', row['title'],'; Average Rating:', row['average_rating']
    if count2 == 1: print'Found', count2, 'book with a title matching', book
    else: print'Found', count2, 'books with a title matching', book
elif ch == '4':
    genre = raw_input('Enter the genre: ')
    count3 = 0
    for row in readertg:
        if genre in row['tag_name']:
            names.append(row['tag_name'])
            tagid.append(row['tag_id'])
    for row in readbktg:
        if row['tag_id'] in tagid:
            grbkid.append(row['goodreads_book_id'])
    for row in reader:
        if row['goodreads_book_id'] in grbkid:
            count3 = count3 + 1
            print'Title:', row['title'], '; Average Rating:', row['average_rating']
    if count3 == 0: print'Found', count3, 'books in genre', genre
    elif count3 == 1: print'Found', count3, 'book in genre', genre, ': [', names,']'
    else: print'Found', count3, 'books in genre', genre, ': [', names,']'
elif ch == 'Q' or 'q':
    exit()
    #repeat = input('Press 1 to continue browsing the library or press 0 to quit: ')
#print'Goodbye!'
#exit()

