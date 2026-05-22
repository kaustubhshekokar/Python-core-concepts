'''phone_no={
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848}

print(phone_no['Shyam'])

phone_no1={
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848,
    'Ram':1555
    }
print(phone_no1)
#lastly asigned will be given

phone_no=dict({
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848,
    'Ram':1555
    })
'''



'''data={
    1:'Jenny',
    2:'hi',
    0:'Mohn'
}
print(data[0])
'''
#we cannot use lists as they are immutable


'''
phone_no={
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848}
print(phone_no)
#phone_no['Mohan']=9999
#print(phone_no)
#phone_no['Moadhu']=9999,4254,4542
#phone_no['Shyam']={'hime':7878,'hii':989}
##########can add dictionary inside dictionaries 
#print(phone_no)
#print(phone_no.get['Shyam'])
#here its not case sensitive so it gives none
'''

'''
phone_no={
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848}
print(phone_no)
del phone_no['Ram']


print(phone_no.pop('Shyam'))
print(phone_no)

phone_no.clear()
print(phone_no)
'''

phone_no={
    'Ram':1234,
    'Shyam':8393,
    'Mohan':3848}
#print(phone_no)
#print(phone_no.keys())
#print(phone_no.values())
#print(print(phone_no.items()))

for i in phone_no:
    print(i)
    print(phone_no[i])

#phone_no2=phone_no.copy()


#print(phone_no2)
###print(len(phone_no2))
