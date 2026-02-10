test_dict={'Codingal':2,'is':10,'best':2,'for':2,'Coding':1}
print("The Orignal Dictionary"+ str(test_dict))

K=int(input("Enter the frequency number:"))
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1

print("Frequency is :" + str(res))