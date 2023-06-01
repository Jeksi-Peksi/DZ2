# Задача №20. Скрабл

w = str(input("Введите слово английскими буквами верхнего регистра: "))
word = []
count = 0
for c in w:
    word.append(c)
    if c == 'Q':
        count += 10
    else:
        if c == 'Z':
            count += 10
        else:
            if c == 'J':
                count += 8
            else:
                if c == 'X':
                    count += 8
                else:
                    if c == 'K':
                        count += 5
                    else:
                        if c == 'Y':
                            count += 4
                        else:
                            if c == 'W':
                                count += 4
                            else:
                                if c == 'V':
                                    count += 4
                                else:
                                    if c == 'H':
                                        count += 4
                                    else:
                                        if c == 'F':
                                            count += 4
                                        else:
                                            if c == 'P':
                                                count += 3
                                            else:
                                                if c == 'M':
                                                    count += 3
                                                else:
                                                    if c == 'C':
                                                        count += 3
                                                    else:
                                                        if c == 'B':
                                                            count += 3
                                                        else:
                                                            if c == 'G':
                                                                count += 2
                                                            else:
                                                                if c == 'D':
                                                                    count += 2
                                                                else:
                                                                    count += 1
                         
        
print(count)
