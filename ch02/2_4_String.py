string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])
print("python"+"program")
print("python-" + str(3.7) + ".exe")
print("-"*30)

oneLine = "this is one line string"
print('t : ', oneLine.count('t'))
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))
print(oneLine.replace('this','that'))

multiLine = """this is
multi line
string"""
sent=multiLine.split('\n')
print(sent)

words = oneLine.split(' ')
print(words)

sent2 = ','.join(words)
print(sent2)