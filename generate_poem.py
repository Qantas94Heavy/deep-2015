
from random import randint

def limerick():
  f = open("inputnew.txt")
  gender = 1
  pc = ''
  lines = f.readlines()
  poem = []
  line1 = "There was "
  templine1 = lines[randint(0,25)]
  #templine1.rstrip()

  if line1[0] == 'h':
    gender = 1
  elif line1[0] == 's':
    gender = 2
  else:
    gender = 3

  line1 += templine1[1:]
  line1 = line1.rstrip()
  line1 += " from "
  templine1_2 = lines[randint(26,39)]
  pc= templine1_2[0]
  line1 += templine1_2[1:]

  line2 = "All the while "
  if gender == 1:
    line2 += "he "
  elif gender == 2:
    line2 += "she "
  else:
    line2 += "it "

  if pc == 'a':
    line2 += lines[randint(40,46)]
  elif pc == 'b':
    line2 += lines[randint(47,54)]
  elif pc == 'c':
    line2 += lines[randint(55,63)]
  elif pc == 'd':
    line2 += lines[randint(64,70)]
  elif pc == 'e':
    line2 += lines[randint(71,83)]
  elif pc == 'f':
    line2 += lines[randint(84,89)]
  elif pc == 'g' or pc == 'h':
    line2 += lines[randint(90,98)]
  elif pc == 'i':
    line2 += lines[randint(99,105)]
  elif pc == 'j':
    line2 += lines[randint(106,111)]
  elif pc == 'k':
    line2 += lines[randint(112,116)]
  elif pc == 'l' or pc == 'm':
    line2 += lines[randint(117,128)]
  elif pc == 'n':
    line2 += lines[randint(129,136)]
  elif pc == 'o':
    line2 += lines[randint(137,143)]

  line3 = ""
  if gender == 1:
    line3 += "So he "
  elif gender == 2:
    line3 += "So she "
  elif gender == 3:
    line3 += "So it "
  templine3 = lines[randint(75,86)]
  line3 += templine3

  line4 = "and " + lines[randint(88,100)]
  if templine1[1] == 'a' and templine1[2] == 'n':
    line5 = "That " + templine1[4:].rstrip() + " that came from " + templine1_2[1:]
  else:
    line5 = "That " + templine1[3:].rstrip() + " that came from " + templine1_2[1:]
  return line1 + line2 + line3 + line4 + line5

def free_verse():
    f = open("inputfree.txt")
    lines = f.readlines()
    temp1 = "I " + lines[randint(0,93)]
    temp2 = "the " + lines[randint(94,265)]
    temp3 = "that " + lines[randint(0,93)]
    temp4 = "the " + lines[randint(94,265)]

    temp5 = "it will probably\n"
    temp6 = lines[randint(0,93)].rstrip() + " it\n"
    temp7 = "for the " + lines[randint(94,265)]

    temp8 = "they were " + lines[randint(266,352)]
    temp9 = "so " + lines[randint(266,352)]
    temp10 = "so " + lines[randint(266,352)] + "..."

    temp11 = "and so " + lines[randint(266,352)] + "."

    return temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11
