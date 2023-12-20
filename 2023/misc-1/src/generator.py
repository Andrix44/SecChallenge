flag = open("flag.txt", 'r').read()

menu = {10: "Rice Krispie Treat",
        20: "Ice Cream",
        40: "Cookies",
        80: "Cake"}

side = {1: "Whipped Cream",
        2: "Chocolate",
        3: "Caramel",
        4: "Sugar topping",
        5: "Gold foil"}

menu_vals = menu.keys()
side_vals = side.keys()
TakeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))

calculation = ""
for i, c in enumerate(flag):
    print(f"--{c}--")
    i += 1
    val = ord(c)
    curr = ""

    if(val in menu_vals):
        curr += f"Person {i} would like the {menu[val]}.\n"
    else:
        closest = TakeClosest(val, menu_vals)
        diff = val - closest

        if(abs(diff) in side_vals):
            if(diff < 0):
                curr += f"Person {i} would like the {menu[closest]}, hold the {side[abs(diff)]}.\n"
            else:
                curr += f"Person {i} would like the {menu[closest]} with {side[diff]}.\n"
        else:
            curr += f"Person {i} would like the {menu[closest]}.\n"
            val -= closest
            while(val != 0):
                closest = TakeClosest(val, menu_vals)
                diff = val - closest

                if(abs(diff) in side_vals):
                    if(diff < 0):
                        curr += f"Person {i} would also like the {menu[closest]}, hold the {side[abs(diff)]}.\n"
                    else:
                        curr += f"Person {i} would also like the {menu[closest]} with {side[diff]}.\n"
                    val = 0
                elif(abs(diff) > max(side_vals)):
                    curr += f"Person {i} would also like the {menu[closest]}.\n"
                    if(diff < 0):
                        curr += f"Person {i} needs {abs(diff)} dollars less for his order!\n"
                    else:
                        curr += f"Person {i} needs {diff} dollars more for his order!\n"
                    val = 0
                else:
                    curr += f"Person {i} would also like the {menu[closest]}.\n"
                    val -= closest

    if(curr):
        print(curr)
        calculation += curr
        calculation += f"Person {i} will pay for his order!\n"
    else:
        print(f"{i}: {ord(c)}")

out = "Hi, welcome to SecChallenge-2023. Here is a menu.\n\n"
for item in menu:
    out += f"{menu[item]}: ${item}\n"
out += "\nHere are your sides.\n\n"
for item in side:
    out += f"{side[item]}: ${item}\n"
out += "\nMay I take your order?\n\n"
out += calculation
out += "Just wait while we decide...\n\nOK, that will be $20.23. Thanks for coming!"

open("chall.txt", 'w').write(out)