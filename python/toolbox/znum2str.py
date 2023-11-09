def num2str(x,k):
    assert x < 10**k, 'Problem with znum2str'
    s = str(x)
    res=''
    for i in range(0,k-len(s)):
        res+= '0'
    return res + s