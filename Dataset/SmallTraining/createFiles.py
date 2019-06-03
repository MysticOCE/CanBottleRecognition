import glob

fileList1 = (glob.glob("*.jpeg")) 
outFT = open("train.txt", "w")

for line in fileList1:
  # write line to output file
  outFT.write(line[:-5])
  outFT.write("\n")

fileList2 = glob.glob("*.jpg")
for line in fileList2:
  # write line to output file
  outFT.write(line[:-4])
  outFT.write("\n")

outFT.close()

# fileList2 = (glob.glob("*.jpeg")) 
# outFV = open("val.txt", "w")

# for line in fileList2:
#   # write line to output file
#   outFV.write(line[:-5])
#   outFV.write("\n")
# outFV.close()

