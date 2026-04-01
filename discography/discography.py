def main():
   data=dict()
   try:
      with open("artists.txt","r") as inf:
         for line in inf:
            line=line.strip()
            if not line:
               continue
            parts=line.split(";")
            code=parts[0]
            fileName=parts[1]

            try:
               with open(fileName,"r") as inf:
                  for line in inf:
                     line=line.strip()
                     if not line:
                        continue
                     parts=line.split(";")
                     year=parts[0]
                     songName=parts[1]

                     if year not in data:
                        data[year]=[]
                     data[year].append((songName,code))

                     
                        
            except OSError:
               exit("error opening the file. ")
               return

   except OSError:
      exit("error opening the file!")
      return
   for year in sorted(data):
      print(year,":")
      for songName, code in data[year]:
         print(f"{songName:<30} {code}")
      print()
         

if __name__=="__main__":
   main()