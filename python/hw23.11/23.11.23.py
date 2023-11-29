# count = 0
# while count < 10:
#     print(count)
#     count = count + 1 
# else:
#     print(count)


# count = 0
# while count < 8:
#     print(count)
#     if count == 5:
#         count = count + 1
#         continue
# print(count)
# count = count + 1


# i = 0
# while i <= 10:
#     if i ==5:
#         i += 1
#         continue
#     print(i,end="")
#     if i == 8:
#         break
#     i+= 1

# i = 0 
# while i <= 10:
#     if i%2 ==0:
#         i +=1
#         continue
#     print(i,end=" ")
#     i +=1


number = [0,1,2,3,4,5]
for i in number:
    print(i,end=" ")


Person = {
    'ferst name':"Assabeneh",
    'last_nam':'Yetayeh',
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for i in Person:
    if i == "skills":
     for j in i:
        print(j)
