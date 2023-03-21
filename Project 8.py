import csv

print("You have two options: \n1) DIY PC build\n2) Budget suggestions")

us1 = int(input())
if us1 == 1:
    print("Cool")
    u1 = input("Processor:")
    u2 = input("Motherboard:")
    u4 = input("Graphics Card:")
    u5 = input("Power Supply:")
    ux = input("Cabinet:")


    rm_input = int(input("How much RAM do you want ?"))
    config_input = int(input("How much memory do you want in each RAM ?:"))
    rm_sticks = rm_input / config_input
    u3 = input("Choose your RAM:")
    


    us3 = input("Do you want a different Cooler (y/n)?")
    if us3 == 'y':
        us4 = int(input("Select your cooler type:\n1) Air\n2) Liquid\n3) A.I.O"))
        if us4 == 1:
            uxi = input("Enter the Air Cooler:")
        elif us4 == 2:
            u12 = input("Enter you Liquid Cooler:")
        elif us4 == 3:
            u13 = input("Enter you AIO:")


    st_input = int(input("How many storage devices do you want ?:\n"))
    var = 0
    while (var <= st_input):
        print("Choose your Storage type")
        us2 = int(input("1) SSD\n2) Hard Drive"))
        if us2 == 1:
            u6 = input("Enter the Storage:")
        elif us2 == 2:
            u7 = input("Enter the Storage")
            var += 1







elif us1 == 2:
    print("Cool")