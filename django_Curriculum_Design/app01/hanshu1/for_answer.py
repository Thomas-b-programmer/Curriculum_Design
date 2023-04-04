#for_answer.py
from decimal import Decimal
import random
def Generate_listof_option_question_answer():

    """生成一个个列表，里面分别以字典的形式存放选项，问题，结果"""
    list_data, list_temple, dict_key1 = [], [], ['A', 'B', 'C', 'D', 'question', 'answer']
    for i in range(1, 11):
        list_temple = []  # 清空
        option, answer, question = generate_expression()
        option = option.split('\n')[0:4]
        list_temple.extend(option)
        list_temple.append(question)
        list_temple.append(answer)
        list_data.append(dict(zip(dict_key1, list_temple)))

    return list_data

def generate_expression():
    """随机生成一个四则运算表达式并计算其结果"""
    # 随机生成操作数和运算符
    expr = ""
    for i in range(random.randint(1,3)):
        if i!= 0:
            expr += str(random.choice(['+', '-', '*', '/']))
        if random.randint(1, 10) > 2: #让产生整数的概率更大
            # 生成整数
            if random.randint(1,10) > 2:
                #加括号
                expr += "("
                expr += str(random.randint(1, 100))
                expr += str(random.choice(['+', '-', '*', '/']))
                expr += str(random.randint(1, 100))
                expr += ")"
            else:
                expr += str(random.randint(1, 100))
                expr += str(random.choice(['+', '-', '*', '/']))
                expr += str(random.randint(1, 100))
        else:
            # 生成浮点数
            if random.randint(1, 10) > 2:
            # 加括号
                expr += "("
                expr += str(Decimal(str(random.uniform(1, 10))).quantize(Decimal('0.00')))
                expr += str(random.choice(['+', '-', '*', '/']))
                expr += str(Decimal(str(random.uniform(1, 10))).quantize(Decimal('0.00')))
                expr += ")"
            else:
                expr += str(Decimal(str(random.uniform(1, 10))).quantize(Decimal('0.00')))
                expr += str(random.choice(['+', '-', '*', '/']))
                expr += str(Decimal(str(random.uniform(1, 10))).quantize(Decimal('0.00')))

    # 计算表达式的值
    result = round(eval(str(expr)), 2)
    options = [result]
    while len(options) < 4:
        if result % 1 == 0:
            # 生成整数选项
            option = random.randint(result - 10, result + 10)
        else:
            # 生成浮点数选项
            option = Decimal(str(random.uniform(result - 10, result + 10))).quantize(Decimal('0.00'))
        if option not in options:
            options.append(option)

    # 打乱选项顺序
    random.shuffle(options)

    # 构造题目
    xuanxiang = ""
    for i, option in enumerate(options):
        xuanxiang += f"{option}\n"

    # 返回选项和答案和题目
    answer = chr(65 + options.index(result))

    #添加等号
    expr = expr + " ="
    return xuanxiang, answer,expr

def evaluate_expression(expression):
    """显示栈内值的情况"""
    dict_key = ['operator', 'operand']
    list_operation = []

    # 表达式去除所有空格
    expression = expression.replace(" ", "")

    # 定义操作符的优先级
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # 定义一个栈来存储操作符和操作数
    operator_stack = []
    operand_stack = []

    # 定义一个函数来执行操作符操作
    def apply_operator():
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        operand_stack.append(result)

    # 循环遍历表达式中的操作符和操作数
    i = 0
    while i < len(expression):
        token = expression[i]
        if token.isnumeric():
            # 如果是数字，将多位数字作为整体令牌处理
            j = i + 1
            while j < len(expression) and expression[j].isnumeric():
                j += 1
            operand_stack.append(int(expression[i:j]))
            i = j - 1
        elif token in "+-*/":
            # 如果是操作符，将其与栈顶的操作符进行比较
            while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence.get(
                    operator_stack[-1], 0):
                # 如果栈顶的操作符具有较高或相等的优先级，则执行栈顶的操作符
                apply_operator()
            # 将当前操作符推到操作符栈上
            operator_stack.append(token)
        elif token == "(":
            # 如果是左括号，将其推到操作符栈上
            operator_stack.append(token)
        elif token == ")":
            # 如果是右括号，将其与栈顶的操作符进行比较
            while operator_stack and operator_stack[-1] != "(":
                # 如果栈顶的操作符不是左括号，则执行栈顶的操作符
                apply_operator()
            # 弹出左括号
            operator_stack.pop()

        # 可视化栈的值的变化情况
        i += 1
        list = []
        list.append(str(operator_stack))
        list.append(str(operand_stack))
        list_operation.append(dict(zip(dict_key, list)))


    # 执行剩余的操作符
    while operator_stack:
        apply_operator()
        i += 1
        list = []
        list.append(str(operator_stack))
        list.append(str(operand_stack))
        list_operation.append(dict(zip(dict_key, list)))

    # 返回操作数栈中的最后一个值，即表达式的值
    return list_operation


