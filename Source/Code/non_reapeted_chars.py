def non_Repeat_Character(s):
    # Initialising an empty list.
    order = []
    # Initialising an empty dictionary
    counts = {}

    for x in s:
        # creating an dictionary which stores "key" as character and value as count.
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
        # appending the character into list in order
            order.append(x)
    print("The character count list is")
    print(counts)
    print("The order of characters in the string \n")
    print(order)
    for x in order:
        if counts[x] == 1:
             return x
    return None


non_Repeat_Character("deep data structure")
print(f'The first non reapeted character is:  {non_Repeat_Character("deep data structure")}')