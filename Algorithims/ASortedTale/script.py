import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

long_bookshelf = utils.load_books("books_large.csv")
# print(ord('a'))
# print(ord(' '))
# print(ord('A'))


def by_title_searching(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_searching(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    return (len(book_a['title_lower']) + len(book_a['author_lower'])) > (len(book_b['title_lower']) + len(book_b['author_lower']))


for book in bookshelf:
    print(book['title_lower'])

sort_1 = sorts.bubble_sort(bookshelf, by_title_searching)

for book in sort_1:
    print(book)

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_searching)

for book in sort_2:
    print(book)

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_searching)
for book in bookshelf_v2:
    print(book)

# print("Bubble Long")
# sort_4 = sorts.bubble_sort(long_bookshelf, by_total_length)
# for book in sort_4:
#     print(book)

print("Quicksort long")
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
for book in long_bookshelf:
    print(book)