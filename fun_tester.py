

divided_leader_xp = 500





def xp_fun(count, cr_count):
  XP = [0, 10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 75000, 90000, 105000, 120000, 135000, 155000]
  return XP[count]

def cr_fun(count, cr_count):
  CR = [0, 0, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
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





######finding range between XP intervals######
print("")
print("Leader(s):")
count = 0
cr_count = cr_fun(count, 0)
cr_count_back = cr_fun(count - 1, 0)
while divided_leader_xp > xp_fun(count, cr_count) :
    cr_count = cr_fun(count, 0)
    cr_count_back = cr_fun(count - 1, 0)
    count += 1



ratio = (divided_leader_xp - xp_fun(count - 1, 0)) / (xp_fun(count, 0) - xp_fun(count - 1, 0))


print('CR: ', float((ratio * (cr_fun(count, cr_count) - cr_fun(count - 1, cr_count_back))) + cr_fun(count - 1,cr_count_back)))
print('XP: ', float((ratio * (xp_fun(count, cr_count) - xp_fun(count - 1, cr_count_back))) + xp_fun(count - 1,cr_count_back)))
print('PROF. B: ', float((ratio * (pb_fun(count, cr_count) - pb_fun(count - 1, cr_count_back))) + pb_fun(count - 1,cr_count_back)))
print('AC: ', float((ratio * (ac_fun(count, cr_count) - ac_fun(count - 1, cr_count_back))) + ac_fun(count - 1,cr_count_back)))
print('HP: ', float((ratio * (hp_fun(count, cr_count) - hp_fun(count - 1, cr_count_back))) + hp_fun(count - 1,cr_count_back)))
print('ATTACK B: ', float((ratio * (ab_fun(count, cr_count) - ab_fun(count - 1, cr_count_back))) + ab_fun(count - 1,cr_count_back)))
print('DAMAGE: ', float((ratio * (da_fun(count, cr_count) - da_fun(count - 1, cr_count_back))) + da_fun(count - 1,cr_count_back)))
print('DC: ', float((ratio * (dc_fun(count, cr_count) - dc_fun(count - 1, cr_count_back))) + dc_fun(count - 1,cr_count_back)))
print('SAVE: ', float((ratio * (sa_fun(count, cr_count) - sa_fun(count - 1, cr_count_back))) + sa_fun(count - 1,cr_count_back)))



    
    

