#
# https://www.hackerrank.com/challenges/the-minion-game/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
# 
################################################             TIME LIMIT EXCEEDED             ########################################################
def minion_game(string):
  kevin = {}
  stuart = {}
  string = string.lower()
  
  # Kevin Words
  for i in range(len(string)):
    for j in range(i+1,len(string)+1):
      if string[i] in ["a","e","i","o","u"]:
        kevin[string[i:j]] = kevin.get(string[i:j],0) + 1
        
  # Stuart Words
  for i in range(len(string)):
    for j in range(i+1,len(string)+1):
      if string[i] not in ["a","e","i","o","u"]:
        stuart[string[i:j]] = stuart.get(string[i:j],0) + 1

  if sum(kevin.values()) > sum(stuart.values()):
    print("Kevin",sum(kevin.values()))
  elif (sum(stuart.values()) > sum(kevin.values())):
    print("Stuart",sum(stuart.values()))
  else:
    print('Draw')
#
#####################################################################################################################################################
#
def minion_game(s):
  s = s.lower()
  kevin_score = 0
  stuart_score = 0
  for i in range(len(s)):
    if s[i] in "aeiou":
      kevin_score += len(s) - i
    else:
      stuart_score += len(s) - i

  if kevin_score > stuart_score:
    print("Kevin", kevin_score)
  elif kevin_score < stuart_score:
    print("Stuart", stuart_score)
  else:
    print("Draw")
