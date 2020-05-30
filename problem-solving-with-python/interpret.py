# https://codingbat.com/prob/p234011
# Write a simple interpreter which understands "+", "-", and "*" operations.
# Apply the operations in order using command/arg pairs starting with the initial value of `value`.
# If you encounter an unknown command, return -1.
#
# interpret(1, ['+'], [1]) → 2
# interpret(4, ['-'], [2]) → 2
# interpret(1, ['+', '*'], [1, 3]) → 6
def interpret(value, commands, args):
    for i in range(len(commands)):
        if commands[i] == "+":
            value += args[i]
        elif commands[i] == "-":
            value -= args[i]
        elif commands[i] == "*":
            value *= args[i]
        else:
            return -1
    return value

value = 1
commands = ["+", "*"]
args = [1, 3]
result = interpret(value, commands, args)
print(result)