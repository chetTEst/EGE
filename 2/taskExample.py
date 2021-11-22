print("(x /\ y) -> (!x /\ !z")
for x in range (2):
  for y in range (2):
    for z in range(2):
        if ((x * y) <= (not(x) * (not(z)))):
          print(x,y,z)