def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Некоректне значення заробітної плати у рядку: {line}")
                else:
                    print(f"Некоректний формат рядка: {line}")

            if count == 0:
                return 0, 0

            average_salary = total / count
            return total, average_salary
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None


total, average = total_salary("salary.txt")
if total is not None and average is not None:
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
