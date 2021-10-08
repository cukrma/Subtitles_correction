import codecs


print("Program pro opravu českých titulků.\n")
print("Níže zadejte cestu a název souboru bez přípony. Pokud je soubor ve stejné složce, stačí pouze název souboru.\n")
file_name = input("Zadejte cestu a název souboru: ")
print("\n\n1) Titulkový soubor (.srt)\n2) Textový soubor (.txt)\n")
file_type = int(input("Typ souboru (uveďte číslo): "))

# rozliseni typu souboru
if file_type == 1:
    file = codecs.open(file_name + ".srt", "r", "ANSI")
else:
    file = codecs.open(file_name + ".txt", "r", "ANSI")
text = file.read()
file.close()

my_dict = [ ["ì", "ě"], ["Ì", "Ě"], ["ù", "ů"], ["Ù", "Ů"], ["è", "č"],
		["È", "Č"], ["ø", "ř"], ["Ø", "Ř"], ["ï", "ď"], ["Ï", "Ď"],
        ["ò", "ň"], ["Ò", "Ň"], [chr(157), "ť"] ]

# nahrazeni vadnych symbolu za spravne
for i in range(len(my_dict)):
    text = text.replace(my_dict[i][0], my_dict[i][1])

if file_type == 1:
    file = codecs.open(file_name + "-fixed.srt", "w", "utf-8")
else:
    file = codecs.open(file_name + "-fixed.txt", "w", "utf-8")
file.write(text)
file.close()
