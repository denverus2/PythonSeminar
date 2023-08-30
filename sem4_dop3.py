# Даны два многочлена, которые вводит пользователь. как две строки.
# Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0


def multi_dick_summ(lib1, lib2):
    lib_out = {}
    maximum = max(max(list(lib1.keys())), max(list(lib2.keys())))
    for i in reversed(range(maximum + 1)):
        if i in lib1 and i in lib2:
            lib_out[i] = lib1[i] + lib2[i]
        elif i in lib1:
            lib_out[i] = lib1[i]
        elif i in lib2:
            lib_out[i] = lib2[i]

    return lib_out


def multi_dick_to_lib(str1):
    str1 = str1.replace(" = 0", "")
    str1 = str1.replace("+ ", "+")
    str1 = str1.replace("- ", "-")
    str1 = str1.replace("*", "")
    sp1 = str1.split()
    lib = {}
    for i in sp1:
        if ("^" not in i) and "x" not in i:
            lib[0] = int(i.replace("+", ""))
        elif ("^" not in i) and "x" in i:
            lib[1] = int(i.replace("+", "").replace("x", ""))
        else:
            lib[int(i.replace("+", "").split("^")[1])] = int(
                i.replace("+", "").split("^")[0].replace("x", "")
            )
    return lib


def multi_dick_to_str(lib):
  string = ""
  for i in lib:
    if i>0:
      if lib[i]>1:
        string=string+f' + {str(abs(lib[i]))}x^{str(i)}'
      elif lib[i]==1:
        string=string+f' + {str(abs(lib[i]))}x'
      elif lib[i]==0:
        string=string+f''
      elif lib[i]<0:
        string=string+f' - {str(abs(lib[i]))}x^{str(i)}'
    else:
      if lib[i]>0:
        string=string+f' + {str(abs(lib[i]))}'
      else:
        string=string+f' - {str(abs(lib[i]))}'
        
        
  if string.startswith(" + "):
    string = string[3:]
  string= string.replace("1x","x")
  string= string.replace("^1","")
  return string + " = 0"


str1 = "2x^2 + 4x + 5 = 0"
str2 = "5x^3 - 3*x^2 - 12 = 0"
lib1 = multi_dick_to_lib(str1)
lib2 = multi_dick_to_lib(str2)

lib_final = multi_dick_summ(lib1, lib2)
print(multi_dick_to_str(lib_final))
