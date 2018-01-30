import random

# male first names
ma = ['Alan', 'Albert', 'Adam', 'Alvin', 'Arthur']
mb = ['Bobby','Barton','Billy', 'Barney', 'Bart', 'Benny', 'Bill', 'Buster', 'Bruce', 'Brian', 'Barry']
mc = ['Curtis','Charles','Charlie','Karl','Carl', 'Calvin', 'Chuck', 'Craig', 'Cletus', 'Croobus']
md = ['Dan', 'Donny', 'Donald','Deryl', 'Darvin','Danny', 'Dale', 'Douglas', 'Doyle', 'Diego', 'Delbert']
me = ['Eddy', 'Eddie', 'Ernie', 'Earl', 'Elbert', 'Eric', 'Elmo', 'Elvis', 'Edgar', ]
mf = ['Franky','Phillip', 'Fabio', 'Frank', 'Fred', 'Freddy', 'Franklin', 'Floyd', 'Francis']
mg = ['Gary','Jerry','Gerald', 'Garfield', 'Greg', 'Gus', 'Glen', 'George',]
mh = ['Harry', 'Hank', 'Harold', 'Howard', 'Homer', 'Huey',]
mi = ['Ian', 'Irwin', 'Ivan', 'Isaac']
mj = ['Jimmy', 'Jerry','Johnny', 'Jeffry',]
mk = ['Kevin', 'Kenny', 'Karl', 'Kyle', 'Kirby', 'Kenneth', 'Keith']
ml = ['Larry', 'Lloyd', 'Louie', 'Leroy', 'Lester', 'Lenny']
mm = ['Mickey','Michael','Marcus', 'Melvin', 'Marivn', ]
mn = ['Norman', 'Norbert', 'Nick', 'Nelson', 'Ned']
mo = ['Oscar','Omar', 'Owen', 'Otis']
mp = ['Paul', 'Pablo', 'Patrick', 'Peter', 'Perry', 'Pedro']
mq = ['Quinton', 'Quoogis', 'Qubith']
mr = ['Richie', 'Roy', 'Randy', 'Ronnie', 'Ronald', 'Rufus', 'Robbie', 'Reggie', 'Rudolph']
ms = ['Sammy', 'Stevie', 'Scotty', 'Stewary', 'Stanley', ]
mt = ['Tony','Timmy','Tommy','Teddy', 'Terry']
mv = ['Vance', 'Vern', 'Vinny', 'Victor']
mw = ['Walter', 'Willy', 'Wallace', 'Willis']
mOther = ['Jimmy', 'Johnny', 'Rufus', 'Tony', 'Randy', ]
mAll = [ma, mb, mc, md, me, mf, mg, mh, mi, mj, mk, ml, mm, mn, mo, mp, mq, mr, ms, mt, mv, mw]

#female
fa = ['Amy', 'Abby', 'Ally', 'Anna']
fb = ['Betty', 'Beverly', 'Babara', 'Betsy', 'Bonny']
fc = ['Cindy','Cyntia', 'Carly', 'Carol']
fd = ['Doris','Debbie', 'Daisy', 'Dolores', ]
fe = ['Emily', 'Erica', 'Edna']
ff = ['Frannie','Francis', 'Fanny',]
fg = ['Gretchen', 'Gina', 'Gloria',]
fh = ['Hannah', 'Honey', 'Herma', 'Helen',]
fj = ['Jenny', 'Jacky', 'Jessie']
fk = ['Katie', 'Kathy', 'Kelly', ]
fl = ['Lucy', 'Lisa', 'Lora', 'Lindsay']
fm = ['Mary', 'Martha', 'Margo']
fn = ['Nancy', 'Nicky', 'Norma', ]
fp = ['Paulie', 'Patty', 'Penny']
fr = ['Rita', 'Roxanne', 'Rosy']
fs = ['Sally', 'Sarah', 'Sharla', 'Shawna']
ft = ['Tiffany', 'Tina', 'Tracy', 'Toni', ]
fw = ['Wanda', 'Wendy', 'Wilma']
fOther = ['Sally','Cindy','Doris']
fAll = [fa, fb, fc, fd, fe, ff, fg, fh, fj, fl, fm, fn, fp, fr, fs, ft, fw]

allFirst = [mAll, fAll]

suffix = [
    'ingus',
    'ringus',
    'rangus',
    'angus',
    'rungus',
    'ungus',
    'ringle',
    'ingle',
    'rangle',
    'ramble',
    'rungo',
]

noRsuffix = [
    'ingus',
    'angus',
    'ungus',
    'ingle',
    'angle',
    'amble',
    'umble',
]

vowelSuffix = [
    'Bringle',
    'Brangus',
    'Bringo',
    'Bingus',
    'Brungus',
    'Brangle',
    'Brungo',
    'Bramble',
    'Crangus',
    'Drangus',
    'Dangus',
    'Dingus',
    'Dringus',
    'Jangles',
    'Jangus',
    'Pringle',
    'Rangus',
    'Ringus',
]

vowels = ['a','e','i','o','u']
badWithR = ['r', 'j', 'w', 'm', 'n', 'h']

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def name(first='', last='', gender=''):

    badInput = True

    if(first==''):
        first = input('Enter first name: ')

    if((len(first) > 0) and (first[0].lower() in alpha)):
        badInput = False

    while badInput:
        try:
            first = input('Enter a valid first name: ')
            if((len(first) > 0) and (first[0].lower() in alpha)):
                badInput = False
                break
        except:
            pass

    badInput = True

    if(last==''):
        last = input('Enter last name: ')

    if((len(last) > 0) and (last[0].lower() in alpha)):
        badInput = False

    while badInput:
        try:
            last = input('Enter a valid last name: ')
            if((len(last) > 0) and (last[0].lower() in alpha)):
                badInput = False
                break
        except:
            pass

    badInput = True

    if(gender==''):
        gender = input('Male of female? [m/f]: ')

    if((len(gender) == 1) and gender.lower() in ['m', 'f']):
        badInput = False

    while badInput:
        try:
            gender = input("Enter a 'm' or 'f' for gender: ")
            if((len(gender) == 1) and gender.lower() in ['m', 'f']):
                badInput = False
                break
        except:
            pass

    def getName(xList):
        return xList[random.randint(0, len(xList) - 1)]

    # get random default names just in case
    genList = allFirst[random.randint(0,1)]
    nameList = genList[random.randint(0, len(genList)-1)]
    bFirst = nameList[random.randint(0, len(nameList)-1)]

    bLast = last[0].upper() + suffix[random.randint(0, len(suffix)-1)]

    if(gender.lower() == 'm'):
        if(first[0].lower() == 'a'):
            bFirst = getName(ma)
        elif(first[0].lower() == 'b'):
            bFirst = getName(mb)
        elif(first[0].lower() == 'c'):
            bFirst = getName(mc)
        elif(first[0].lower() == 'd'):
            bFirst = getName(md)
        elif(first[0].lower() == 'e'):
            bFirst = getName(me)
        elif(first[0].lower() == 'f'):
            bFirst = getName(mf)
        elif(first[0].lower() == 'g'):
            bFirst = getName(mg)
        elif(first[0].lower() == 'h'):
            bFirst = getName(mh)
        elif(first[0].lower() == 'i'):
            bFirst = getName(mi)
        elif(first[0].lower() == 'j'):
            bFirst = getName(mj)
        elif(first[0].lower() == 'k'):
            bFirst = getName(mk)
        elif(first[0].lower() == 'l'):
            bFirst = getName(ml)
        elif(first[0].lower() == 'm'):
            bFirst = getName(mm)
        elif(first[0].lower() == 'n'):
            bFirst = getName(mn)
        elif(first[0].lower() == 'o'):
            bFirst = getName(mo)
        elif(first[0].lower() == 'p'):
            bFirst = getName(mp)
        elif(first[0].lower() == 'q'):
            bFirst = getName(mq)
        elif(first[0].lower() == 'r'):
            bFirst = getName(mr)
        elif(first[0].lower() == 's'):
            bFirst = getName(ms)
        elif(first[0].lower() == 't'):
            bFirst = getName(mt)
        elif(first[0].lower() == 'v'):
            bFirst = getName(mv)
        elif(first[0].lower() == 'w'):
            bFirst = getName(mw)
        else:
            bFirst = getName(mOther)
    elif(gender.lower() == 'f'):
        if(first[0].lower() == 'a'):
            bFirst = getName(fa)
        elif(first[0].lower() == 'b'):
            bFirst = getName(fb)
        elif(first[0].lower() == 'c'):
            bFirst = getName(fc)
        elif(first[0].lower() == 'd'):
            bFirst = getName(fd)
        elif(first[0].lower() == 'e'):
            bFirst = getName(fe)
        elif(first[0].lower() == 'f'):
            bFirst = getName(ff)
        elif(first[0].lower() == 'h'):
            bFirst = getName(fh)
        elif(first[0].lower() == 'j'):
            bFirst = getName(fj)
        elif(first[0].lower() == 'k'):
            bFirst = getName(fk)
        elif(first[0].lower() == 'l'):
            bFirst = getName(fl)
        elif(first[0].lower() == 'm'):
            bFirst = getName(fm)
        elif(first[0].lower() == 'n'):
            bFirst = getName(fn)
        elif(first[0].lower() == 'p'):
            bFirst = getName(fp)
        elif(first[0].lower() == 's'):
            bFirst = getName(fs)
        else:
            bFirst = getName(fOther)

    if(last[0].lower() in vowels):
        blast = getName(vowelSuffix)
    elif(last[0].lower() in badWithR):
        bLast = last[0].upper() + getName(noRsuffix)
    else:
        bLast = last[0].upper() + getName(suffix)

    return bFirst + ' ' + bLast

def randomName(gender=''):
    if(gender.lower()=='m'):
        genList = allFirst[0]
    elif(gender.lower()=='f'):
        genList = allFirst[1]
    else:
        genList = allFirst[random.randint(0,1)]

    nameList = genList[random.randint(0, len(genList)-1)]
    bFirst = nameList[random.randint(0, len(nameList)-1)]

    bLast = vowelSuffix[random.randint(0, len(vowelSuffix)-1)]

    return bFirst + ' ' + bLast
    
def randomFirst(gender=''):
    if(gender.lower()=='m'):
        genList = allFirst[0]
    elif(gender.lower()=='f'):
        genList = allFirst[1]
    else:
        genList = allFirst[random.randint(0,1)]
        
    nameList = genList[random.randint(0, len(genList)-1)]
    bFirst = nameList[random.randint(0, len(nameList)-1)]
    
    return bFirst
    
def randomLast():
    bLast = vowelSuffix[random.randint(0, len(vowelSuffix)-1)]
    return bLast
    
def help():
    print('\nSteve Brule name generator\n')
    print('name() --> system queries for first, last, and gender as input')
    print("name() also can take arguments --> name('Richie', 'Jackson', 'm')")
    print('randomName() --> returns random brule name, can also take gender argument\n')
    print('randomFirst() --> returns a random first name, can take the gender argument\n')
    print('randomLast() --> returns a random last name, can take the gender argument\n')
    print('quote() --> returns a random quote from the doctor')
