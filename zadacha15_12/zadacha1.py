class Count_elements:
    def __init__(self, num_list: list):
        self.num_list = num_list

    def count_elements(self):

        result = dict((i, self.num_list.count(i)) for i in self.num_list)
        return result

num_list = [1, 1, 3, 2, 1, 1, 3, 4]
c = Count_elements(num_list)
print(c.count_elements())
