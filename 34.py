# Задача №34. Есть ритм = Парам пам-пам. Нет ритма = Пам парам.

stih = "я-хочу-решить-дзшку-да-да-да"
stishki = stih.split()
 
print(stishki)
 
a = [sum(x in 'у е ы а о э я и ю' for x in b)
 for b in stishki]
 
if len(set(a)) == 1 :
    ritm = "Парам пам-пам"  
else: ritm = "Пам парам"
 
print(ritm)