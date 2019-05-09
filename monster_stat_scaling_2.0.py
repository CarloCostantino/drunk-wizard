from __future__ import division
from decimal import Decimal

def ac_boundary(wblock, scaled_stat):
    if scaled_stat >= (wblock + 3):
        scaled_stat = (wblock + 3)
    elif scaled_stat <= (wblock - 3):
        scaled_stat = (wblock - 3)
    return scaled_stat


def ab_dc_boundary(wblock, scaled_stat):
    if scaled_stat >= (wblock + 2):
        scaled_stat = (wblock + 2)
    elif scaled_stat <= (wblock - 2):
        scaled_stat = (wblock - 2)
    return scaled_stat


def hp_da_boundary(wblock, scaled_stat):
    if scaled_stat >= (wblock * 1.5):
        scaled_stat = (wblock * 1.5)
    elif scaled_stat <= (wblock * 0.5):
        scaled_stat = (wblock * 0.5)
    return scaled_stat



def xp_fun(count, cr_count):
  XP = [0, 10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000, \
        11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 75000, 90000, 105000, \
        120000, 135000, 155000]
  return XP[count]

def cr_fun(count, cr_count):
  CR = [0, 0, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, \
        24, 25, 26, 27, 28, 29, 30]
  return CR[count]

def pb_fun(count, cr_count):
  PB = [1, 2, 2, 2 ,2 , 2, 2, 2 ,2 , 3, 3, 3 ,3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9]
  return PB[count]

def ac_fun(count, cr_count):
  if (count) > 5:
    count = 6
  AC = [11, 12, 12, 13, 13, 13, float(13+((1/3) * cr_count))]
  return AC[count]

def hp_fun(count, cr_count):
    if (count) > 5 and (count) < 12:
      count = 6
    elif (count) > 11:
      count = 7
    HP = [1, 3, 9, 15, 24, 30, float((15 * cr_count)+15), float(15 * cr_count)]
    return HP[count]
  
def ab_fun(count, cr_count):
  if (count) > 5:
    count = 6
  AB = [1, 2, 3, 3, 4, 4, float(4 + ((1/2) * cr_count))]
  return AB[count]



def da_fun(count, cr_count):
    if (count) > 5 and (count) < 12:
      count = 6
    elif (count) > 11:
      count = 7
    DA = [0, 1, 3, 5, 8, 10, float(5+ (5 * cr_count)), float(5 * cr_count)]
    return DA[count]
  
def dc_fun(count, cr_count):
  if (count) > 5:
    count = 6
  DC = [8, 9, 10, 10, 11, 11, float(11+((1/2) * cr_count))]
  return DC[count]

def sa_fun(count, cr_count):
  if (count) > 5:
    count = 6
  SA = [0, 1, 2, 2, 3, 3, float(3+((1/2)*cr_count))]
  return SA[count]




print("Enter original statistics of a monster")
ori_xp = int(input("original xp: "))
want_xp = int(input("wanted xp: "))




#for finding what stat block should be
count = 0
cr_count = cr_fun(count, 0)
cr_count_back = cr_fun(count - 1, 0)
while ori_xp > xp_fun(count, cr_count) :
    count += 1
    cr_count = cr_fun(count, 0)
    cr_count_back = cr_fun(count - 1, 0)
    
    
ratio = (ori_xp - xp_fun(count - 1, 0)) / (xp_fun(count, 0) - xp_fun(count - 1, 0))



sblock_cr = float((ratio * (cr_fun(count, cr_count) - cr_fun(count - 1, cr_count_back))) + cr_fun(count - 1,cr_count_back))
sblock_xp = round((ratio * (xp_fun(count, cr_count) - xp_fun(count - 1, cr_count_back))) + xp_fun(count - 1,cr_count_back))
sblock_pb = round((ratio * (pb_fun(count, cr_count) - pb_fun(count - 1, cr_count_back))) + pb_fun(count - 1,cr_count_back))
sblock_ac = round((ratio * (ac_fun(count, cr_count) - ac_fun(count - 1, cr_count_back))) + ac_fun(count - 1,cr_count_back))
sblock_hp = round((ratio * (hp_fun(count, cr_count) - hp_fun(count - 1, cr_count_back))) + hp_fun(count - 1,cr_count_back))
sblock_ab = round((ratio * (ab_fun(count, cr_count) - ab_fun(count - 1, cr_count_back))) + ab_fun(count - 1,cr_count_back))
sblock_da = round((ratio * (da_fun(count, cr_count) - da_fun(count - 1, cr_count_back))) + da_fun(count - 1,cr_count_back))
sblock_dc = round((ratio * (dc_fun(count, cr_count) - dc_fun(count - 1, cr_count_back))) + dc_fun(count - 1,cr_count_back))
sblock_sa = round((ratio * (sa_fun(count, cr_count) - sa_fun(count - 1, cr_count_back))) + sa_fun(count - 1,cr_count_back))


print("pb stat block: ", sblock_pb)
ori_pb = int(input("original pb: "))
print("ac stat block: ", sblock_ac)
ori_ac = int(input("original ac: "))
print("hp stat block: ", sblock_hp)
ori_hp = int(input("original hp: "))
print("ab stat block: ", sblock_ab)
ori_ab = int(input("original ab: "))
print("da stat block: ", sblock_da)
ori_da = int(input("original da: "))
print("dc stat block: ", sblock_dc)
ori_dc = int(input("original dc: "))
print("sa stat block: ", sblock_sa)
ori_sa = int(input("original sa: "))







  
#FINDING WANTED BLOCK
count = 0
cr_count = cr_fun(count, 0)
cr_count_back = cr_fun(count - 1, 0)
while want_xp > xp_fun(count, cr_count) :
    count += 1
    cr_count = cr_fun(count, 0)
    cr_count_back = cr_fun(count - 1, 0)
    
    
ratio = (want_xp - xp_fun(count - 1, 0)) / (xp_fun(count, 0) - xp_fun(count - 1, 0))


wblock_cr = float((ratio * (cr_fun(count, cr_count) - cr_fun(count - 1, cr_count_back))) + cr_fun(count - 1,cr_count_back))
wblock_xp = round((ratio * (xp_fun(count, cr_count) - xp_fun(count - 1, cr_count_back))) + xp_fun(count - 1,cr_count_back))
wblock_pb = round((ratio * (pb_fun(count, cr_count) - pb_fun(count - 1, cr_count_back))) + pb_fun(count - 1,cr_count_back))
wblock_ac = round((ratio * (ac_fun(count, cr_count) - ac_fun(count - 1, cr_count_back))) + ac_fun(count - 1,cr_count_back))
wblock_hp = round((ratio * (hp_fun(count, cr_count) - hp_fun(count - 1, cr_count_back))) + hp_fun(count - 1,cr_count_back))
wblock_ab = round((ratio * (ab_fun(count, cr_count) - ab_fun(count - 1, cr_count_back))) + ab_fun(count - 1,cr_count_back))
wblock_da = round((ratio * (da_fun(count, cr_count) - da_fun(count - 1, cr_count_back))) + da_fun(count - 1,cr_count_back))
wblock_dc = round((ratio * (dc_fun(count, cr_count) - dc_fun(count - 1, cr_count_back))) + dc_fun(count - 1,cr_count_back))
wblock_sa = round((ratio * (sa_fun(count, cr_count) - sa_fun(count - 1, cr_count_back))) + sa_fun(count - 1,cr_count_back))



ratio_pb = ori_pb / sblock_pb
ratio_ac = ori_ac / sblock_ac
ratio_hp = ori_hp / sblock_hp
ratio_ab = ori_ab / sblock_ab
ratio_da = ori_da / sblock_da
ratio_dc = ori_dc / sblock_dc
ratio_sa = ori_sa / sblock_sa




scaled_pb = wblock_pb * ratio_pb
scaled_ac = wblock_ac * ratio_ac
scaled_hp = wblock_hp * ratio_hp
scaled_ab = wblock_ab * ratio_ab
scaled_da = wblock_da * ratio_da
scaled_dc = wblock_dc * ratio_dc
scaled_sa = wblock_sa * ratio_sa

print(" ")
print("Proficency Bonus: ", scaled_pb)
print("Armor Class: ", ac_boundary(wblock_ac, scaled_ac))
print("Hit Points: ", hp_da_boundary(wblock_hp, scaled_hp))
print("Attack Bonus: ", ab_dc_boundary(wblock_ab, scaled_ab))
print("Damage: ", hp_da_boundary(wblock_da, scaled_da))
print("DC: ", ab_dc_boundary(wblock_dc, scaled_dc))
print("Saves: ", scaled_sa)


