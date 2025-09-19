def main():
  earth_weight=0
  for i in range(10):
    earth_weight +=0.5
    moon_weight=earth_weight*0.165
    print("{}年地球上体重：{}kg".format(i+1,earth_weight))
    print("{}年月球上体重：{}kg".format(i+1,moon_weight))
    
