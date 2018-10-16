# 使用 mypy 库进行注解测试
# 在终端使用命令：mypy filename.py
# 如果有类型注解错误则会有相应输出


def add(x: int, y: int) -> int:
    return x + y


def area_calculation(radius: float) -> float:
    # 变量类型注解需要 py3.6 以上版本
    # Var Type Annotations need python 3.6 and later
    pi: float = 3.1415926
    return radius * radius * pi


if __name__ == '__main__':
    print(add(1, 2))
    print(add.__annotations__)
    print(area_calculation(2))
    print(area_calculation.__annotations__)
