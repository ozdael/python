word="bottles"
for beer_num in range(5,0,-1):
    print(beer_num,word,"of beer left")
    print("Please take one")
    if beer_num == 1:
        print("No more bottles of beer left")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num,word,"of beer left")
    print()

              
