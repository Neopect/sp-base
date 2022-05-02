# x = '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?),'
# print(x)
# y = x*3
# print(y)

# z= 'Insert into ' + y
# print(z)

# a = 'sdf'
# b = 'sdfggg'
# b += a
# print(b)

# item = '("Cheers - De "Cheers"", "Angello Conti Orquesta y Coros", "149720", "False", "5QzKiiOjCQtyRy9dFDz8E2", "https://p.scdn.co/mp3-preview/d047350f0500a038377afb7667af13dcba53dc01?cid=2f3935102c944c5aa5fbebf15a2dde0b", "5QzKiiOjCQtyRy9dFDz8E2", "Tyler")'
# if '"' in item:
#                 item = item.replace('"',"")
#                 print('yes')
# print(item)


# import configs
# print(configs.numbers)

def test(lt):
    del lt[0]
    return lt

lst = [3, 5, 6, 4, 6, 1, 0, 6]
lst = test(lst)
print(lst)
print(lst[1:44])

