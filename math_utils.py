def find_max_number(num1, num2, num3):
if num1>num2 and num1>num3:
      return num1
    elif num2>num1 and num2>num3:
      return num2
    elif num3>num1 and num3>num2:
      return num3 
    elif num1==num2 and num2==num3:
      return num1
    elif num1==num2 or num2==num3:
      return num2
    elif num1==num3:
      return num1
    else:
      return num1

def find_mean(num1, num2, num3):
    r=num1+num2+num3
    n=r/3
    return n

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    o=(((num1-n)+(num2-n)+(num3-n))/3)**0.5
    return o
