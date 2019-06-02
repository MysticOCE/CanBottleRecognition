import glob

# fileList1 = glob.glob("*.png")
# fileList1.extend(glob.glob("*.jpeg")) 
# outFT = open("train.txt", "w")

# for line in fileList1:
#   # write line to output file
#   outFT.write(line)
#   outFT.write("\n")
# outFT.close()

fileList2 = (glob.glob("*.png")) 
outFV = open("val.txt", "w")

for line in fileList2:
  # write line to output file
  outFV.write(line[:-4])
  outFV.write("\n")
outFV.close()

