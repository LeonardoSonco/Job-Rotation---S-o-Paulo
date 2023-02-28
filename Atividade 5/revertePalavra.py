entrada = "Leonardo"

# começa no ultimo caractere e vai decrecendo -1, e terminando no -1, onde não havera letra 
stringInvertida= ""
for i in range(len(entrada) - 1, -1, -1):
    stringInvertida += entrada[i]

print("A string invertida ficou assim:", stringInvertida)
