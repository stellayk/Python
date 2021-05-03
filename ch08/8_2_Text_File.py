import os
print('\nDirectory Path: ', os.getcwd())

try:
    ftest1=open('C:/Users/user/Documents/ftest.txt', mode='r')
    print(ftest1.read())

    ftest2=open('C:/Users/user/Documents/ftest.txt', mode='w')
    ftest.write('my first text is...')

    ftest3=open('C:/Users/user/Documents/ftest.txt', mode='a')
    ftest3.write('\nmy second text is...')

except Exception as e:
    print('error: ', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()




try:
    ftest=open('C:/Users/user/Documents/ftest.txt', mode='r')
    full_text=ftest.read()
    print(full_text)
    print(type(full_text))

    ftest=open('C:/Users/user/Documents/ftest.txt', mode='r')
    lines=ftest.readlines()
    print(lines)
    print(type(lines))
    print('length of lines: ', len(lines))

    docs=[]
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)

    ftest=open('C:/Users/user/Documents/ftest.txt', mode='r')
    line=ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('error: ',e)
finally:
    ftest.close()