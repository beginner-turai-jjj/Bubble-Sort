def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # 隣同士を比較
            if arr[j] > arr[j + 1]:
                # 交換
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 動作確認
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubble_sort(data)
    print("ソート後:", sorted_data)