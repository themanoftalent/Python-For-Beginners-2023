import datetime

class usertwo:

    def __init__(self,fname,birthday):
        self.fname=fname
        self.birthday=birthday

        #lets split name and surname
        name_pieces=fname.split()
        self.name=name_pieces[0]
        self.lastname=name_pieces[-1]

    def age(self):
        today=datetime.date(2020,1,13)
        yyyy=int(self.birthday[0:4])
        mm=int(self.birthday[4:6])
        dd=int(self.birthday[6:8])
        
        dob=datetime.date(yyyy,mm,dd)
        age_in_days=(today-dob).days
        print('Days in life',age_in_days)
        age_in_years=age_in_days//365
        return 'Years in life ',age_in_years


user2=usertwo('Dave Poole','19820101')
# print(user2.fname,user2.birthday)
# print(user2.fname)

# print(user2.name)
# print(user2.lastname)
# print(user2.birthday)
print(user2.age())

