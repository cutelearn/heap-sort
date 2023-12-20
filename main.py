class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def _heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.arr[i] < self.arr[l]:
            largest = l

        if r < n and self.arr[largest] < self.arr[r]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self._heapify(n, largest)

    def sort(self):
        # 建立最大堆積
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify(self.n, i)

        # 堆積排序
        for i in range(self.n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            print(f"{self.arr[:i]} | {self.arr[i:]} <-- (swap)")
            self._heapify(i, 0)
            print(f"{self.arr[:i]} | {self.arr[i:]} <-- (sift down)")

        return self.arr


if __name__ == "__main__":
    arr = [2, 6, 3, 5, 4, 1, 7]
    heap_sort_instance = HeapSort(arr)
    sorted_arr = heap_sort_instance.sort()
    print(sorted_arr)
