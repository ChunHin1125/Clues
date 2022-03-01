
msg = input("Enter message to be decoded (do not put space): ")
msg = list(msg)
decoded_msg = [None]*len(msg)

for counter, letter in enumerate(msg):
    if (counter % 2 == 0):
        if counter + 3 > len(msg):
            decoded_msg[len(msg)-counter-1] = letter
        else:
            decoded_msg[counter+3] = letter
    elif (counter % 2 == 1):
        if counter + 1 >= len(decoded_msg):
            decoded_msg[len(msg)-counter-1] = letter
        else:
            decoded_msg[counter+1] = letter

print (decoded_msg)