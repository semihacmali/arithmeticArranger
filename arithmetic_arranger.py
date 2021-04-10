def exceptions(nu1, nu2, op):
    try:
        int(nu1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(nu2)
    except:
        return "Error: Numbers must only contain digits." 
    try:
        if(len(nu1) > 4 or len(nu2) > 4):
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    try:
        if(op != "+" and op != "-"):
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""

def arithmetic_arranger(problems, display=False):
  start = 1
  spaces = "    "
  str1 = str2 = str3 = str4 = ""
  
  try:
      if(len(problems) > 5):
          raise BaseException
  except:
      return "Error: Too many problems."
  for islem in problems:
      islemler = islem.split(" ")
      nu1 = islemler[0]
      op = islemler[1]
      nu2 = islemler[2]
      
      exps = exceptions(nu1, nu2, op)
      if(exps != ""):
          return exps
      no1 = int(nu1)
      no2 = int(nu2)
      
      space = max(len(nu1), len(nu2))
      
      if(start == 1):
          str1 += nu1.rjust(space + 2)
          str2 += op + ' ' + nu2.rjust(space)
          str3 += '-' * (space + 2)
          if(display == True):
              if(op == "+"):
                  str4 += str(no1 + no2).rjust(space + 2)
              else:
                  str4 += str(no1 - no2).rjust(space + 2)
          start = 0
      else:
          str1 += nu1.rjust(space + 6)
          str2 += op.rjust(5) + ' ' + nu2.rjust(space)
          str3 += spaces + '-' * (space + 2)
          if (display == True):
              if(op == "+"):
                  str4 += spaces + str(no1 + no2).rjust(space + 2)
              else:
                  str4 += spaces + str(no1 - no2).rjust(space + 2)
  if (display == True):
      return str1 + "\n" + str2 + "\n" + str3 + "\n" + str4
  else:
      return str1 + "\n" + str2 + "\n" + str3 