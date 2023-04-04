import random

# 随机生成算术表达式
numbers = [i for i in range(1, 11)]  # 生成1-10的整数列表
operators = ['+', '-', '*', '/']


def generate_expression():
    expression = ""
    for i in range(random.randint(1, 3)):  # 随机生成1-3对包含两个数字和一个字符的整体
        shuzi = int(random.randint(1, 10))  # 随机生成一队括号的概率
        if i == 0:
            pass
        else:
            expression += random.choice(operators)
        if shuzi > 7:
            expression += "("
            expression += str(random.choice(numbers))  # 以第一个数字作为表达式的开头
            expression += random.choice(operators)
            expression += str(random.choice(numbers))
            expression += ")"
        else:
            expression += str(random.choice(numbers))  # 以第一个数字作为表达式的开头
            expression += random.choice(operators)
            expression += str(random.choice(numbers))
    return expression


class SqStack:
    def __init__(self):  # 构造方法
        self.data = []

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 元素e进栈
        self.data.append(e)

    def pop(self):  # 元素出栈
        assert not self.empty()  # 检测栈为空
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()  # 检测栈为空
        return self.data[-1]


class ExpressClass:
    def __init__(self, str):
        self.exp = str
        self.postexp = []

    def getpostexp(self):
        return self.postexp

    #把中缀表达式转换成后缀表达式
    def Trans(self):
        opor = SqStack()
        i = 0
        self.postexp = []
        while i < len(self.exp):
            ch = self.exp[i]
            if ch == "(":
                opor.push(ch)
            elif ch == ")":
                while not opor.empty() and opor.gettop() != "(":
                    e = opor.pop()
                    self.postexp.append(e)
                opor.pop()  # 把"("弹出
            elif ch == "*" or ch == "/":
                while not opor.empty():
                    e = opor.gettop()
                    if e != "(" and (e == "*" or e == "/"):
                        e = opor.pop()
                        self.postexp.append(e)
                    else:
                        break
                opor.push(ch)
            elif ch == "+" or ch == "-":
                while not opor.empty():
                    e = opor.gettop()
                    if e != "(":
                        opor.pop()
                        self.postexp.append(e)
                    else:
                        break
                opor.push(ch)
            else:
                d = ""
                while ch >= "0" and ch <= "9":
                    d += ch
                    i += 1
                    if i < len(self.exp):
                        ch = self.exp[i]
                    else:
                        break
                i -= 1
                self.postexp.append(int(d))
            i += 1
        while not opor.empty():
            e = opor.pop()
            self.postexp.append(e)

        return self.postexp

    def getValue(self):
        opand = SqStack()
        i, j = 0, 0
        list_data = [] #用来存放栈内的值
        print(self.postexp)
        while i < len(self.postexp):
            opv = self.postexp[i]
            if opv == "+":
                a = opand.pop()
                list_data.pop()
                b = opand.pop()
                list_data.pop()
                c = b + a
                opand.push(c)
                list_data.append(c)
                print(f"第{j}步栈的情况：{list_data}")
                j += 1
            elif opv == "-":
                a = opand.pop()
                list_data.pop()
                b = opand.pop()
                list_data.pop()
                c = b - a
                opand.push(c)
                list_data.append(c)
                print(f"第{j}步栈的情况：{list_data}")
                j += 1
            elif opv == "*":
                a = opand.pop()
                list_data.pop()
                b = opand.pop()
                list_data.pop()
                c = b * a
                opand.push(c)
                list_data.append(c)
                print(f"第{j}步栈的情况：{list_data}")
                j += 1
            elif opv == "/":
                a = opand.pop()
                list_data.pop()
                b = opand.pop()
                list_data.pop()
                c = b / a
                opand.push(c)
                list_data.append(c)
                print(f"第{j}步栈的情况：{list_data}")
                j += 1
            else:
                opand.push(opv)
                list_data.append(opv)
                print(f"第{j}步栈的情况：{list_data}")
                j += 1

            i += 1
        return list_data[0]

def main():
    print("欢迎使用四则运算出题系统")
    num = int(input("请输入你需要几道计算题："))
    score = 0
    for i in range(num):
        expression = generate_expression()
        print("(10分)题目：", expression)
        answer = input("请输入你的答案(保留2位小数)：")
        obj = ExpressClass(expression)
        obj.Trans()
        print("----------栈的变化情况------------")
        a = "{:.2f}".format(obj.getValue())
        print("--------------------------------")
        if answer == a:
            print("恭喜你答对了！！")
            score += 10
        else:
            print("很遗憾你错了！！")
            print("正确答案是：",a)
        print(f"当前的累计分数是：{score}")
        print()

#调用
if __name__ == '__main__':
    main()
