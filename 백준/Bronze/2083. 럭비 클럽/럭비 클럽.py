while True:
  name, age, weight = map(str, input().split())
  age=int(age)
  weight=int(weight)

  if name=='#' and age==0 and weight==0:
    exit(0)
  elif age>17 or weight>=80:
    print(name, 'Senior')
  else:
    print(name, 'Junior')