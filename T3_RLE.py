# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb" - >....stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

with open("T3_text.txt", "r") as f:
    text = f.read()

print(text)

def rleText(text):
    newtext=''
    count=0
    for i in range(0,len(text)-1):
        
        if text[i]==text[i+1]:
            count+=1
            
        else:
            if count==0:
                newtext=newtext+text[i]
            else:
                newtext=newtext+str(count+1)+text[i]
                count=0

    if count==0:
        newtext=newtext+text[-1]
    else:
        newtext=newtext+str(count+1)+text[-1]
    return newtext

def isNumber(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def unRleText(newtext):
    unpackingText=''
    number=''

    for i in range(0,len(newtext)):
        if isNumber(newtext[i]):
            number+=newtext[i]
        else:
            if number.isdigit():      
                for j in range(int(number)):
                    unpackingText+=newtext[i]
                number=''    
            else:
                unpackingText+=newtext[i]
    return unpackingText



packingText=rleText(text)
print(packingText)

unpackingText=unRleText(packingText)

print(unpackingText)
   