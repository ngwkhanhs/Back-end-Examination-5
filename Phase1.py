def find_combinations(brightness_values, expected_brightness):
    result = []
    current_combination = []
    find_combination(brightness_values, expected_brightness, 0, current_combination, result)
    return result

def find_combination(brightness_values, expected_brightness, start_index, current_combination, result):
    # tìm xong: expected còn lại bằng 0
    if expected_brightness == 0:
        result.append(list(current_combination))
        return

    # điều kiện dừng: expected âm hoặc vượt quá index của list
    if expected_brightness < 0 or start_index >= len(brightness_values):
        return

    # cộng từng số trong mảng vào tập hiện tại 
    for i in range(start_index, len(brightness_values)):
        current_combination.append(brightness_values[i])
        # tìm kiếm với expected_brightness đã giảm đi giá trị của số đó
        find_combination(brightness_values, expected_brightness - brightness_values[i], i, current_combination, result)
        current_combination.pop()

# test
lights_brightness_input = input('light_brightness_list = ')
light_brightness_list = [int(num) for num in lights_brightness_input.split()]
expected_brightness = int(input('expected_brightness = '))

combinations = find_combinations(light_brightness_list, expected_brightness)
print(combinations)