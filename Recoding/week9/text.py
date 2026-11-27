seed = id(object()) & 0xffffffff
def irand():
  global seed
  seed ^= (seed<<13)&0xffffff
  seed ^= (seed>>17)
  seed ^= (seed<<5)&0xffffff
  return float(seed)/((2 ** 32) -1)

items = [((n%7)+1, ['B', 'O', '+', '*','T'][n%5]) for n in range(20)]


def shuffle(items):
    for i in range(len(items)):
       j = int(irand() * (i+1))
       items[i],items[j] = items[j],items[i]
    return items
# print(shuffle(items))

def share(items):
  #  market =  items[10:]
   player_one = []
   player_two =[]
   for _ in range(5):
      player_one.append(items.pop())
      player_two.append(items.pop())
    
   if player_one.pop(1):
      if player_one.pop(1) in player_two:
         player_two.pop(player_one.pop(1))
      else:
         player_two.append(items[0])
   if not player_one and player_two:
      return "player_one won"
   elif not player_two and player_one:
      return "player_two won"

print(share(items))
   


      