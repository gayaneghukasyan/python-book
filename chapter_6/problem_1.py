
'''
Գրել ծրագիր, որն արտածում է մուտքագրված տողում 'a' սիմվոլի բոլոր ինդեքսները:
'''
str = input('Enter a text')

for i in range(len(str)):
    if str[i]=='a':
        print(i)
