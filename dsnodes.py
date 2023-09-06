class MySpecialTree():
    def __init__(self, values=None):
        self.data = values if values is not None else []
        for x in range(len(self.data)//2, -1, -1):
            self.__max_treeify__(x)

    def parent(self, x):
        return (x - 1) // 2

    def left_child(self, x):
        return 2 * x + 1

    def right_child(self, x):
        return 2 * x + 2

    def __max_treeify__(self, x):
        left = self.left_child(x)
        right = self.right_child(x)
        largest = x

        if left < len(self.data) and self.data[left] > self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] > self.data[largest]:
            largest = right

        if largest != x:
            self.data[x], self.data[largest] = self.data[largest], self.data[x]
            self.__max_treeify__(largest)

    def pop_max_value(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        max_value = self.data[0]
        self.data[0] = self.data.pop()
        self.__max_treeify__(0)
        return max_value

def special_tree(values, k):
    myTree = MySpecialTree(values)
    soln = []
    for _ in range(k):
        soln.append(myTree.pop_max_value())
    return soln

# Example usage
values = [4, 10, 3, 5, 1]
k = 3
result = special_tree(values, k)
print(result)  # Output should be [10, 5, 4]