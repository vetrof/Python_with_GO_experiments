import subprocess


def calculator_go(x, y):
    result = subprocess.run(['./calc', str(x), str(y)], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error running calculator: {result.stderr}")
    return int(result.stdout.strip())


# Пример использования
x = 10
y = 20

result = calculator_go(x, y)
print("result", result)


