#THIS CODE IS BASIC DICTIONARY
#HASH TABLE USAGE IN PYTHON 
#IN THE EXAMPLE, A TELEPHONE PHONEBOOK HAS BEEN IMPLEMENTED
phone = {'name':'John',2:25,'number' : ['326 66 44', '328 17 18'] }
phone2 = {'name':'Jessie','number' : ['326 66 44', '328 17 18'] }
phone['city'] = 'San Fransisco'


#x = phone.pop(2)
#phone.update({'name':'Jack','number':['326 66 44','328 17 18','888 88 88']})

#print(len(phone))
#print(phone.keys())
#print(phone.values())
#del phone[2]
#print(phone)
#print(phone.items())
#for value in phone.items():
    #print(value)
#*******************************ADDING A PHONE TO THE PHONELIST****************************************
class PhoneBook:

    def __init__(self):
        self.phoneList = list([])

    def addContact(self,name,number):
        new_phone = {'name':name,'numbers':[number]}
        self.phoneList.append(new_phone)

    def removeContact(self,name):
        for i in self.phoneList:
            if(name == i['name']):
                self.phoneList.remove(i)
                return
        print("There is already no person like that")

    def showAllContact(self):
        for i in self.phoneList:
            print(i)
    
    def searchContact(self,name):
        for i in self.phoneList:
            if(name == i['name']):
                print(i)
                return
        print("There is no person like that in this phonebook")

    def searchNumber(self,number):
        for i in self.phoneList:
            if(number == i['numbers']):
                print(i)
                return
        print("There is no number like that in this phonebook")

    def addNumberToContact(self,name,new_number):
        for i in self.phoneList:
            if(name == i['name']):
                i['numbers'].append(new_number)
                return
        print("There is no contact like that in the phonebook")
    
    def removeNumberFromContact(self,name,old_number):
        for i in self.phoneList:
            if(name == i['name']):
                for x in i['numbers']:
                    if old_number == x:
                        i['numbers'].remove(old_number)
                        return
        #print("There is no number like that in the phonebook")

    def addInfoToContact(self,name,category,info):
        for i in self.phoneList:
            if(name == i['name']):
                i[category] = info
                return

    def removeInfoFromContact(self,name,category):
        for i in self.phoneList:
            if(name == i['name']):
                deleted = i.pop(category)
                return



p = PhoneBook()
p.addContact('Jessie','236 33 33')
p.addContact('James','123 23 45')
p.showAllContact()
print("************************")

p.addNumberToContact('James','456 12 12')
p.removeNumberFromContact('James','1231231')
#p.searchContact('James')
p.addInfoToContact('James','City','Chicago')
p.removeInfoFromContact('James','City')
p.showAllContact()