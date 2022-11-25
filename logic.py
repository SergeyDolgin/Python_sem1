# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание 
# ⋁ - логическое "Или" 
# ⋀ - логическое "И"

xpred = [1, 0]
ypred = [1, 0]
zpred = [1, 0]
for x in xpred:
    for y in xpred:
        for z in xpred:
            print('x=', x, 'y=', y, 'z=',z)
            statement1 = not (x or y or z)
            statement2 = (not x) and (not y) and (not z)
            print (statement1 == statement2)
           