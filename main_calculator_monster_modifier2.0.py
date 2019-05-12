######INPUTS######
######pary input######


charnumber = int(input("Number of characters in the party? "))
count = 0
charlevels = [0,0,0,0,0,0,0,0,0,0]

while count < charnumber and charnumber > 1:
  print("Character %d is what level? " % (count +1))
  charlevels[count] = int(input(" "))
  count += 1
if charnumber < 2:
  print("The character is what level? ")
  charlevels[count] = int(input(" "))


######monster input######


totalmonsters = int(input("Total number of monsters? "))
if totalmonsters > 1:
  monsterleaders = int(input("Of the total monsters, how many are leaders? "))
else:
  monsterleaders = 1


######advantage input######


advantage = int(input("How many player advantages? "))
disadvantage = int(input("How many monster advantages? "))

print("1: Easy 2: Medium 3: Hard 4: Deadly")
input_difficulty = int(input("Choose difficulty "))


######BODY######
######environment difficulty modifier######


environment = advantage - disadvantage

holder = input_difficulty + environment

if holder <= 0:
    holder = 0

if holder >= 5:
    holder = 5


######calc xp threshold######


very_easy = [17, 33, 50, 83, 167, 200, 233, 300, 367, 400, 533, 666, 733, 833, 933, 1066, 1333, 1400, 1600, 1866]
easy = [25, 50, 75, 125, 250, 300, 350, 450, 550, 600, 800, 1000, 1100, 1250, 1400, 1600, 2000, 2100, 2400, 2800]
medium = [50, 100, 150, 250, 500, 600, 750, 900, 1100, 1200, 1600, 2000, 2200, 2500, 2800, 3200, 3900, 4200, 4900, 5700]
hard = [75, 150, 225, 375, 750, 900, 1100, 1400, 1600, 1900, 2400, 3000, 3400, 3800, 4300, 4800, 5900, 6300, 7300, 8500]
deadly = [100, 200, 400, 500, 1100, 1400, 1700, 2100, 2400, 2800, 3600, 4500, 5100, 5700, 6400, 7200, 8800, 9500, 10900, 12700]
very_deadly = [150, 300, 600, 750, 1650, 2100, 2550, 3150, 3600, 4200, 5400, 6750, 7600, 8550, 9600, 10800, 13200, 14250, 16350, 19050]


difficulty = [very_easy, easy, medium, hard, deadly, very_deadly]


count = 0
total_party_xpthresh = 0
while count < charnumber:
  total_party_xpthresh += (difficulty[holder][charlevels[count]-1])
  count += 1


######multipler######

 
multiplier = [0.50, 0.75, 1, 1.25, 1.50, 1.75, 2, 2.25, 2.50, 2.75, 3, 3.25, 3.50, 3.75, 4, 4.25, 4.50, 4.75, 5]
#game neutrally starts at 1 so 2rd position#

position = 2 + (4 - charnumber) #party size

if charnumber >= 6:   #if party is 6+ then set to 0.50#
    position = 0


######monster number######


if totalmonsters == 2:
    position += 2

if totalmonsters >= 3 and totalmonsters <= 6:
    position += 4
    
if totalmonsters >= 7 and totalmonsters <= 10:
    position += 6

if totalmonsters >= 11 and totalmonsters <= 14:
    position += 8

if totalmonsters >= 15:
    position += 12
    

######deviding xp among monsters######


raw_xp_total = total_party_xpthresh / (multiplier[position])
divided_xp = raw_xp_total / ((monsterleaders * 2) + (totalmonsters - monsterleaders))
divided_leader_xp = (divided_xp * 2)
divided_monster_xp = divided_xp


######MONSTER MODIFIER######


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


######finding range between XP intervals######


if totalmonsters > 1:
  print("")
  print("Each of the %s Leaders has: " % monsterleaders)
if totalmonsters <= 1:
  print("The monster has: ")

count = 0
cr_count = cr_fun(count, 0)
cr_count_back = cr_fun(count - 1, 0)
while divided_leader_xp > xp_fun(count, cr_count) :
    cr_count = cr_fun(count, 0)
    cr_count_back = cr_fun(count - 1, 0)
    count += 1


ratio = (divided_leader_xp - xp_fun(count - 1, 0)) / (xp_fun(count, 0) - xp_fun(count - 1, 0))


#print('CR: ', round((ratio * (cr_fun(count, cr_count) - cr_fun(count - 1, cr_count_back))) + cr_fun(count - 1,cr_count_back)))
print('XP: ', round((ratio * (xp_fun(count, cr_count) - xp_fun(count - 1, cr_count_back))) + xp_fun(count - 1,cr_count_back)))
print('PROF. B: ', round((ratio * (pb_fun(count, cr_count) - pb_fun(count - 1, cr_count_back))) + pb_fun(count - 1,cr_count_back)))
print('AC: ', round((ratio * (ac_fun(count, cr_count) - ac_fun(count - 1, cr_count_back))) + ac_fun(count - 1,cr_count_back)))
print('HP: ', round((ratio * (hp_fun(count, cr_count) - hp_fun(count - 1, cr_count_back))) + hp_fun(count - 1,cr_count_back)))
print('ATTACK B: ', round((ratio * (ab_fun(count, cr_count) - ab_fun(count - 1, cr_count_back))) + ab_fun(count - 1,cr_count_back)))
print('DAMAGE: ', round((ratio * (da_fun(count, cr_count) - da_fun(count - 1, cr_count_back))) + da_fun(count - 1,cr_count_back)))
print('DC: ', round((ratio * (dc_fun(count, cr_count) - dc_fun(count - 1, cr_count_back))) + dc_fun(count - 1,cr_count_back)))
print('SAVE: ', round((ratio * (sa_fun(count, cr_count) - sa_fun(count - 1, cr_count_back))) + sa_fun(count - 1,cr_count_back)))


if totalmonsters > 1:
  print("")
  print("Each of the %s Minions has: " % (totalmonsters - monsterleaders))
  count = 0
  cr_count = cr_fun(count, 0)
  cr_count_back = cr_fun(count - 1, 0)
  while divided_monster_xp > xp_fun(count, cr_count) :
      cr_count = cr_fun(count, 0)
      cr_count_back = cr_fun(count - 1, 0)
      count += 1


ratio = (divided_monster_xp - xp_fun(count - 1, 0)) / (xp_fun(count, 0) - xp_fun(count - 1, 0))

if totalmonsters > 1:
  #print('CR: ', round((ratio * (cr_fun(count, cr_count) - cr_fun(count - 1, cr_count_back))) + cr_fun(count - 1,cr_count_back)))
  print('XP: ', round((ratio * (xp_fun(count, cr_count) - xp_fun(count - 1, cr_count_back))) + xp_fun(count - 1,cr_count_back)))
  print('PROF. B: ', round((ratio * (pb_fun(count, cr_count) - pb_fun(count - 1, cr_count_back))) + pb_fun(count - 1,cr_count_back)))
  print('AC: ', round((ratio * (ac_fun(count, cr_count) - ac_fun(count - 1, cr_count_back))) + ac_fun(count - 1,cr_count_back)))
  print('HP: ', round((ratio * (hp_fun(count, cr_count) - hp_fun(count - 1, cr_count_back))) + hp_fun(count - 1,cr_count_back)))
  print('ATTACK B: ', round((ratio * (ab_fun(count, cr_count) - ab_fun(count - 1, cr_count_back))) + ab_fun(count - 1,cr_count_back)))
  print('DAMAGE: ', round((ratio * (da_fun(count, cr_count) - da_fun(count - 1, cr_count_back))) + da_fun(count - 1,cr_count_back)))
  print('DC: ', round((ratio * (dc_fun(count, cr_count) - dc_fun(count - 1, cr_count_back))) + dc_fun(count - 1,cr_count_back)))
  print('SAVE: ', round((ratio * (sa_fun(count, cr_count) - sa_fun(count - 1, cr_count_back))) + sa_fun(count - 1,cr_count_back)))
