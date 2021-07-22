'''This is a little bit tricky question but it can be done by two pointer solution, by prev and i pointer, we just have to
look at 4 cases 1. L..L -> LLLL 2. R...R -> RRRR 3. L..R -> L..R 4. R..L -> we then have to look at odd, even places by
doing divmod '''


def pusingDomino(dominoes):
    dominoes = 'L'+dominoes+'R'
    n = len(dominoes)
    ans = ''
    prev = 0

    for i in range(1,n):
        diff = i-prev-1

        if dominoes[i] == '.':
            continue

        if dominoes[i] == dominoes[prev]:
            ans += dominoes[i]*diff

        elif dominoes[i] == 'L' and dominoes[prev] == 'R':
            q,r = divmod(diff,2)
            ans += 'R'*q + '.'*r +'L'*q

        else:
            ans += '.'*diff

        prev = i
        ans += dominoes[i]

    return ans[:-1]

dominoes = ".L.R...LR..L.."
print(pusingDomino(dominoes))