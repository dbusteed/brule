import random

# male first names
ma = ['Alan']
mb = ['Bobby','Barton','Billy']
mc = ['Curtis','Charles','Charlie','Karl','Carl']
md = ['Donald','Deryl', 'Darvin','Danny']
me = ['Eddy']
mf = ['Franky','Phillip']
mg = ['Gary','Jerry','Gerald']
mh = ['Harry']
mj = ['Jimmy', 'Jerry','Johnny']
mk = ['Kevin, Kenny']
ml = ['Larry']
mm = ['Mikey','Michael']
mn = ['Norman']
mo = ['Oscar']
mp = ['Paul']
mr = ['Richie', 'Randy', 'Ronnie', 'Ronald']
ms = ['Sammy', 'Stevie']
mt = ['Tony','Timmy','Tommy','Teddy']
mw = ['Walter', 'Willy']
mOther = ['Jimmy', 'Johnny']
mAll = [ma, mb, mc, md, me, mf, mg, mh, mj, mk, ml, mm, mn, mo, mp, mr, ms, mt, mw]

#female
fa = ['Amy']
fb = ['Betty']
fc = ['Cindy','Cyntia']
fd = ['Doris','Debbie']
fe = ['Emily']
ff = ['Frannie','Francis']
fg = ['Gretchen', 'Gina']
fh = ['Hannah']
fj = ['Jenny']
fk = ['Katie']
fl = ['Lucy']
fm = ['Mary']
fn = ['Nancy']
fp = ['Paulie']
fr = ['Rita']
fs = ['Sally', 'Sarah']
ft = ['Tiffany', 'Tina', 'Tracy']
fw = ['Wanda', 'Wendy']
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
]

noRsuffix = [
    'ingus',
    'angus',
    'ungus',
    'ingle',
    'angle',
    'amble',
]
vowelSuffix = ['Bringle','Brangus','Drangus','Brungus']


def name(first='', last='', gender=''):
    if(first==''):
        first = input('Enter first name: ')
    if(last==''):
        last = input('Enter last name: ')
    if(gender==''):
        gender = input('Male of female? [m/f]: ')

    if(gender == 'm'):
        if(first[0].lower() == 'a'):
            bFirst = ma[random.randint(0,len(ma)-1)]
        elif(first[0].lower() == 'b'):
            bFirst = mb[random.randint(0,len(mb)-1)]
        elif(first[0].lower() == 'c'):
            bFirst = mc[random.randint(0,len(mc)-1)]
        elif(first[0].lower() == 'd'):
            bFirst = md[random.randint(0,len(md)-1)]
        elif(first[0].lower() == 'e'):
            bFirst = me[random.randint(0,len(me)-1)]
        elif(first[0].lower() == 'f'):
            bFirst = mf[random.randint(0,len(mf)-1)]
        elif(first[0].lower() == 'g'):
            bFirst = mg[random.randint(0,len(mg)-1)]
        elif(first[0].lower() == 'h'):
            bFirst = mh[random.randint(0,len(mh)-1)]
        elif(first[0].lower() == 'j'):
            bFirst = mj[random.randint(0,len(mj)-1)]
        elif(first[0].lower() == 'k'):
            bFirst = mk[random.randint(0,len(mk)-1)]
        elif(first[0].lower() == 'l'):
            bFirst = ml[random.randint(0,len(ml)-1)]
        elif(first[0].lower() == 'm'):
            bFirst = mm[random.randint(0,len(mm)-1)]
        elif(first[0].lower() == 'n'):
            bFirst = mn[random.randint(0,len(mn)-1)]
        elif(first[0].lower() == 'o'):
            bFirst = mo[random.randint(0,len(mo)-1)]
        elif(first[0].lower() == 'p'):
            bFirst = mp[random.randint(0,len(mp)-1)]
        elif(first[0].lower() == 'r'):
            bFirst = mr[random.randint(0,len(mr)-1)]
        elif(first[0].lower() == 's'):
            bFirst = ms[random.randint(0,len(ms)-1)]
        elif(first[0].lower() == 't'):
            bFirst = mt[random.randint(0,len(mt)-1)]
        elif(first[0].lower() == 'w'):
            bFirst = mw[random.randint(0,len(mw)-1)]
        else:
            bFirst = mOther[random.randint(0,len(mOther)-1)]
    elif(gender == 'f'):
        if(first[0].lower() == 'a'):
            bFirst = fa[random.randint(0, len(fa)-1)]
        elif(first[0].lower() == 'b'):
            bFirst = fb[random.randint(0, len(fb)-1)]
        elif(first[0].lower() == 'c'):
            bFirst = fb[random.randint(0, len(fb)-1)]
        elif(first[0].lower() == 'd'):
            bFirst = fd[random.randint(0, len(fd)-1)]
        elif(first[0].lower() == 'e'):
            bFirst = fe[random.randint(0, len(fe)-1)]
        elif(first[0].lower() == 'f'):
            bFirst = ff[random.randint(0, len(ff)-1)]
        elif(first[0].lower() == 'h'):
            bFirst = fh[random.randint(0, len(fh)-1)]
        elif(first[0].lower() == 'j'):
            bFirst = fj[random.randint(0, len(fj)-1)]
        elif(first[0].lower() == 'k'):
            bFirst = fk[random.randint(0, len(fk)-1)]
        elif(first[0].lower() == 'l'):
            bFirst = fl[random.randint(0, len(fl)-1)]
        elif(first[0].lower() == 'm'):
            bFirst = fm[random.randint(0, len(fm)-1)]
        elif(first[0].lower() == 'n'):
            bFirst = fn[random.randint(0, len(fn)-1)]
        elif(first[0].lower() == 'p'):
            bFirst = fp[random.randint(0, len(fp)-1)]
        elif(first[0].lower() == 's'):
            bFirst = fs[random.randint(0, len(fs)-1)]
        else:
            bFirst = fOther[random.randint(0, len(fOther)-1)]


    vowels = ['a','e','i','o','u']
    badWithR = ['r', 'j', 'w', 'm', 'n']

    if(last[0].lower() in vowels):
        bLast = vowelSuffix[random.randint(0, len(vowelSuffix)-1)]
    elif(last[0].lower() in badWithR):
        bLast = last[0].upper() + noRsuffix[random.randint(0, len(noRsuffix)-1)]
    else:
        bLast = last[0].upper() + suffix[random.randint(0, len(suffix)-1)]

    print(bFirst + ' ' + bLast)

def randomName(gender=''):
    if(gender=='m'):
        print('')
    elif(gender=='f'):
        print('')
    else:
        genList = allFirst[random.randint(0,1)]
        nameList = genList[random.randint(0, len(genList)-1)]
        bFirst = nameList[random.randint(0, len(nameList)-1)]

        bLast = vowelSuffix[random.randint(0, len(vowelSuffix)-1)]

    print(bFirst + ' ' + bLast)
