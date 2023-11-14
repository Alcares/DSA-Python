import utils
import sorts

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  return False


def by_total_length(book_a, book_b):
  sum_a = len(book_a['title']) + len(book_a['author'])
  sum_b = len(book_b['title']) + len(book_b['author'])
  if sum_a > sum_b:
    return True
  return False

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  return False

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
long_bookshelf_v1 = long_bookshelf.copy()
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf_v1, 0, len(bookshelf_v2) - 1, by_total_length)
print('finished')

# for book in bookshelf_v2:
#   print(book['author'])
