def generate_hint(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair = (numbers[i], numbers[j])
            for op in ['+', '-', '*', '/']:
                try:
                    result = eval(f"{pair[0]} {op} {pair[1]}")
                    if 12 <= result <= 20:
                        return f"Try combining {pair[0]} {op} {pair[1]} = {result:.2f}"
                except ZeroDivisionError:
                    continue
    return "No hints found!"