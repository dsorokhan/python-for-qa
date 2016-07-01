with open("d:/alice_in_wonderland.txt") as f:
    data = f.read()
    print "number of sentences", data.count(".") + data.count("...")
