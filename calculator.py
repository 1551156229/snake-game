#!/usr/bin/env python3
"""命令行计算器"""


def calculate(a, operator, b):
    """执行基本运算"""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: 除数不能为零"
        return a / b
    elif operator == '**':
        return a ** b
    else:
        return "Error: 不支持的运算符"


def main():
    print("命令行计算器")
    print("支持运算符: + - * / **")
    print("输入 'quit' 退出\n")

    while True:
        expression = input("请输入表达式 (如 2 + 3): ").strip()

        if expression.lower() == 'quit':
            print("再见!")
            break

        try:
            parts = expression.split()
            if len(parts) != 3:
                print("Error: 请输入格式如 '2 + 3'")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, operator, b)
            print(f"结果: {result}\n")

        except ValueError:
            print("Error: 请输入有效的数字\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
