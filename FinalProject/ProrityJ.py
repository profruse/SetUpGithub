class PriorityQueue:  # Just a few small alterations to the Queue class
    def __init__(self, catalogue):
        self.curr_size = 0  # Rename this so that is doesn't overlap with the method
        self.catalogue = catalogue
        self.items = []  # The container for all items in the queue

    def is_empty(self):
        return self.curr_size == 0  # Simply test the current size of the list

    def enqueueAll(self):  # Checks if a book is either complete or already in the queue and adds it to the queue if it is neither
        for i in self.catalogue.list:
            present = False
            if i.complete:
                present = True
            for j in self.items:
                if i == j[0]:
                    present = True
            if not present:
                pop = self.catalogue.priority(i)
                self.items.append((i, pop))
                self.curr_size += 1
                self.bSort()  # Sorts them afterward

    def translate(self, new):
        if not self.is_empty():  # Removes highest priority item
            item = self.items[0]
            item[0].addVolume()  # Updates the necessary information to the book
            item[0].changePopularity(new)
            print(f"Translating: {item[0].name}: Volume {item[0].volumes}")  # Displays what it's translating
            self.curr_size -= 1
            self.items.remove(self.items[0])
            self.catalogue.sSort()  # Sorts the catalogue now that popularity has been updated
        else:
            raise Exception("Queue is empty!")

    def peek(self):
        if not self.is_empty():  # Takes a look and returns the item with the highest priority
            item_str = self.items[0]
            return item_str[0].name
        else:
            raise Exception("Queue is empty!")

    def size(self):
        return self.curr_size  # Return the size variable

    def bSort(self):  # Sorts all items based on priority
        for ind in range(len(self.items)):
            min_index = ind

            for j in range(ind + 1, len(self.items)):
                # select the minimum element in every iteration
                if self.items[j][1] < self.items[min_index][1]:
                    min_index = j
            # swapping the elements to sort the self.items
            (self.items[ind], self.items[min_index]) = (self.items[min_index], self.items[ind])

    def print_queue(self):
        if not self.is_empty():  # Prints out all items in stack, each on a new line, unless empty
            stack_str = ""
            for x in self.items:
                stack_str += x[0].name
                stack_str += ", "
                stack_str += x[1]
                stack_str += "\n"
            return stack_str
        else:
            raise Exception("Queue is empty!")