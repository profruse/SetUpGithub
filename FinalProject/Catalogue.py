from Book import Book


class Catalogue:
    def __init__(self):
        self.list = []

    def addBook(self, book):
        if type(book) == Book:
            self.list.append(book)
            self.sSort()
        else:
            raise Exception("Must be a book!")

    def check(self, title):
        for i in self.list:
            if i.name == title:
                return True
        return False

    def sSort(self):
        for ind in range(len(self.list)):
            min_index = ind

            for j in range(ind + 1, len(self.list)):
                # select the minimum element in every iteration
                if self.list[j].popularity > self.list[min_index].popularity:
                    min_index = j
            # swapping the elements to sort the self.list
            (self.list[ind], self.list[min_index]) = (self.list[min_index], self.list[ind])

    def priority(self, item):
        for i in range(len(self.list)):
            if self.list[i] == item:
                if self.list[i].volumes < 2:
                    return 'B'
                elif i < 3:
                    return 'A'
                elif i < len(self.list)/2:
                    return 'C'
                else:
                    return 'D'
        raise Exception("Book not found.")

    def printC(self):
        for i in self.list:
            print(f"{i.name}, Volumes: {i.volumes}, Popularity: {i.popularity}")
