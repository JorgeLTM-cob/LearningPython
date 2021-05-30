pi = 3.141516
l1 = ["Number","Letter",[23,pi,278],"variable"]
print (l1.index("variable"))
#
# 3
#
l1 = ["Number","Letter",[23,pi,278],"variable"]
l1.append("constant")
print (l1)
#
# ["Number","Letter",[23,pi,278],"variable","constant"]
# 
l1 = ["Number","Letter",[23,pi,278],"variable"]
print (l1.count("variable"))
#
# 1
#
l1 = ["Number","Letter",[23,pi,278],"variable"]
l1.insert(2,"New value")
print(l1)
#
# ["Number","Letter","New Value",[23,pi,278],"variable"]
#
l1 = ["Number","Letter",[23,pi,278],"variable"]
l2 = ["Cesar","Mario","Octavio"]
l1.extend(l2)
print(l1)
#
# ["Number","Letter",[23,pi,278],"variable","Cesar","Mario","Octavio"]
#
l1 = ["Number","Letter",[23,pi,278],"variable"]
l1.pop(2)
print (l1)
#
# ["Number","Letter","variable"]
#
l1 = ["Number","Letter","Number","variable"]
l1.remove("Number")
print (l1)
#
# ["Letter",[23,pi,278],"variable"]
#
l1 = ["Number","Letter",[23,pi,278],"variable"]
l1.reverse()
print(l1)
#
#l1 = ["variable",[23,pi,278],"Letter","Number"]
#
