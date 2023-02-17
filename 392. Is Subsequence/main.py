def isSubs(sub,ori):
    if len(sub)==0:
        return True
    else:
        for i in range(len(ori)):
            if sub[0] == ori[i]:
                return isSubs(sub[1:],ori[i+1:])
        return False
sub="axc"
ori="ahbgdc"
print(isSubs(sub,ori))
    