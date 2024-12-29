class Kadane:
    def run(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
# Contoh Penggunaan kadane's algorithm
arr = [-2, 1, -3, 4, -1, 2, 1, 5, -4]
print(Kadane.run(arr))