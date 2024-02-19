def max_square(field):
    n, m = len(field), len(field[0])
    '''
    Create a matrix dp that will store the maximum side length
    of a square filled with carrots for each cell on the field.
    '''
    dp = [[0 for _ in range(m)] for _ in range(n)]
    #fill the dp matrix
    for i in range(n):
        for j in range(m):
            #If a cell contains a carrot, its maximum side length is 1
            #If a cell does not contain a carrot, its maximum side length is 0
            if field[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    '''
                    If a cell contains a carrot and its neighbors also contain carrots,
                    its maximum side length is the minimum of its neighbors'
                    maximum side lengths + 1
                    '''
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    max_side = 0
    #Find the maximum side length of a square in the dp matrix and output it
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                max_side = max(max_side, dp[i][j])
    return max_side


def main():
    n, m = map(int, input().split())
    field = []
    for _ in range(n):
        field.append(list(map(int, input().split())))
    print(max_square(field))

if __name__ == "__main__":
    main()