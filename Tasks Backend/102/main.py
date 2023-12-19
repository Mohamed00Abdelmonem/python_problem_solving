import datetime


def birthday(*args):
    s = datetime.date(2003, 7, 26)

    print(s.strftime('%A'))
    print(f"my name is a : xxxx and my age is a : {(datetime.date.today() - args[0]) / 365} years ")


birthday(datetime.date(2003, 7, 26))

print("#" * 40)

#
# myBirthDay = datetime.datetime(2003, 10, 25)
# dateNow = datetime.datetime.now()
#
# print(f"My Birthday is {myBirthDay} And ", end="")
# print(f"Date Now Is {dateNow}")
#
# print(f" I Lived For {dateNow - myBirthDay}")
# print(f" I Lived For {(dateNow - myBirthDay).days} year.")