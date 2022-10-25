W,H =(input()).split()
B =float(W)/(float(H)*float(H))
print(format(B, ".3f"), end='\n')
if B < 18.5:
  print("Underweight")
elif B < 23.0:
  print("Normal")
elif B < 25.0:
  print("Overweight")
else:
  print("Obese")
