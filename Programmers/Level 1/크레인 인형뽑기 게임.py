def solution(board, moves):
    answer = []
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if stack[-1:] == stack[-2:-1]:
                    answer += stack[-1:]
                    stack = stack[:-2]
                break
    return len(answer)*2