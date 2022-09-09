from string import ascii_uppercase


def mov(dic_: dict, value1, value2):
    dic_[value1] = int(is_numeric(dic_, value2))
    return dic_


def add(dic_: dict, value1, value2):
    dic_[value1] += int(is_numeric(dic_, value2))
    return dic_


def sub(dic_: dict, value1, value2):
    dic_[value1] -= int(is_numeric(dic_, value2))
    return dic_


def mul(dic_: dict, value1, value2):
    dic_[value1] *= int(is_numeric(dic_, value2))
    return dic_


def print_(dic_: dict, list_of_print: list, var):
    list_of_print.append(int(is_numeric(dic_, var)))
    return list_of_print


def is_numeric(dic_: dict, value):
    if value.isnumeric():
        return value
    return dic_[value]


def jump(list_of_program: list, element):
    index = list_of_program.index(f"{element}:")
    return list_of_program[index:]


def comparing(op1, oper, op2):
    op1 = int(op1)
    op2 = int(op2)
    dic_of_comp = {"==": op1 == op2, ">": op1 > op2,
                   "<": op1 < op2, "<=": op1 <= op2, ">=": op1 >= op2, "!=": op1 != op2}
    return dic_of_comp[oper]


def run(program: list):
    copy = program[:]
    dict_of_var = {}
    result_list = []
    alphabets = ascii_uppercase
    if len(program) == 0:
        return result_list

    for elements in alphabets:
        dict_of_var[elements] = 0

    while True:
        condition = False
        for index, line in enumerate(program, start=0):
            if line == "" or "END" in line:
                return result_list
            line = line.split()
            check = len(program)-1

            command = line[0]

            if command == "MOV":
                operand1 = line[1]
                operand2 = line[2]
                dict_of_var = mov(dict_of_var, operand1, operand2)

            elif command == "ADD":
                operand1 = line[1]
                operand2 = line[2]
                dict_of_var = add(dict_of_var, operand1, operand2)

            elif command == "SUB":
                operand1 = line[1]
                operand2 = line[2]
                dict_of_var = sub(dict_of_var, operand1, operand2)

            elif command == "MUL":
                operand1 = line[1]
                operand2 = line[2]
                dict_of_var = mul(dict_of_var, operand1, operand2)

            elif command == "PRINT":
                operand1 = line[1]
                result_list = print_(dict_of_var, result_list, operand1)

            elif command == "JUMP":
                operand1 = line[1]
                program = jump(copy, operand1)
                break

            elif command == "IF":
                operand1 = line[1]
                operand2 = line[2]
                operand3 = line[3]
                operand4 = line[4]
                operand5 = line[5]
                condition = comparing(
                    dict_of_var[operand1], operand2, is_numeric(dict_of_var, operand3))

                if condition:
                    program = jump(copy, operand5)
                    break

        if index == check and condition == False:
            break
    return result_list


if __name__ == "__main__":
    code = ""
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    result = run(program2)
    print(result)
