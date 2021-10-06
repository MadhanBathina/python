o=open ("myfile.txt","a")
for i in range(10):
    o.write("This is line %d\r\n" % (i+1))
o.close
