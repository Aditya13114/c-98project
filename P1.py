def swapFileData():
    d1 = input("Enter The File Name")
    d2 = input("Enter The File Name")

    with open(d1, 'r') as x:
        data_x = x.read()



    with open(d2, 'r') as d:
        data_d = d.read()


    with open(d1, 'w') as x:
        x.write(data_d)


    with open(d2, 'w') as d:
        d.write(data_x)




swapFileData()





   