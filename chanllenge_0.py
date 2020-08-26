import random

class Groups:
    
    def __init__(self, member_list, number_in_each):
        self.member= member_list
        self.count=number_in_each
        self.member=random.shuffle(member)
        
        
    def partition(self):
        for i in range(0, len(member), count):
            yield member[i:i + count]
        
##Total Members to be sorted    
member='Saul Daniel Alan Danial Michael \
        Jayson Mohammad Thuyen Triet Mahmood\
        Deep Iordanis Youssaf Rashedur Garima \
        Megan  Manoj Chunmei Zhao'.split()
        
##Number of members in each group
count=5

a=Groups(member,count)
print(list(a.partition()))
