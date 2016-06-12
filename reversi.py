import numpy as np
def create_board():
    a = np.zeros(64, dtype=int)
    a[27] = a[36] = 1
    a[28] = a[35] = 2
    return a
def print_board(a):
    print('  a b c d e f g h')
    for i in range(8):
        print(i+1, end=' ')
        print(' '.join('.*o'[j] for j in a[i*8:][:8]))
def put_piece(a, p, w, puton=True, chk=True):
    t, x, y = 0, p%8, p//8
    for di, fi in zip([-1, 0, 1], [x, 7, 7-x]):
        for dj, fj in zip([-8, 0, 8], [y, 7, 7-y]):
            if not di == dj == 0:
                b = a[p+di+dj::di+dj][:min(fi, fj)]
                n = (b==3-w).cumprod().sum()
                if b.size <= n or b[n] != w: n = 0
                t += n
                if puton:
                    b[:n] = w
    if puton:
        if chk: assert(a[p] == 0 and t > 0)
        a[p] = w
    return t
def best(a, w):
    from math import exp
    for i in range(64):
        if b[i] != 0: continue
        t = put_piece(b, i, w, True, False)
        if t == 0:
            b[i] = 0
            continue
        u = sum(b[j]==0 and put_piece(b, j, 3-w, False) > 0 for j in range(64))
        r.append((t-c*u+np.random.rand()*0.5, i))
        b = a.copy()
    return sorted(r)[-1][1] if r else -1
if __name__ == '__main__':
    a = create_board()
    w = 1
    while np.count_nonzero(a) < 64:
        print_board(a)
        s = input('> ')
        if not s or s=='q': break
        if s == 'p':
            try:
                x, y = ord(s[0])-97, int(s[1])-1
                put_piece(a, x+8*y, w)
            except:
                continue
        p = best(a, 3-w)
        if p >= 0:
            put_piece(a, p, 3-w)
    n1, n2 = (a==1).sum(). (a==2).sum()
    print('%d - %d %s' % (n1, n2,
        'You win' if n1 > n2
        'You loass' elif n1 < n2 else 'Draw')

