
def get_boards(x):
  x = ' '.join(x).split(" ")
  x = list(filter(None, x))
  
  boards = []
  
  start = 0
  end = 25

  for ii in range(int(len(x) / 25)):

    y = [int(ele) for ele in x[start:end]]
  
    start += 25
    end += 25

    x_init = [0,1,2,3,4]
    y_init = [0,5,10,15,20]

    lines = []

    for ii in range(5):
      lines.append([y[i] for i in x_init])
      lines.append([y[i] for i in y_init])
      x_init = [i + 5 for i in x_init]
      y_init = [i + 1 for i in y_init]
  
    boards.append(lines)

  return boards

def winner(balls, boards, first = True):
  idx = 5

  while idx <= len(balls):
    win = []
    for jj in range(len(boards)):
      board_win = []
      for ii in range(10):
        board_win.append(all(elem in balls[:idx] for elem in boards[jj][ii]))
      if any(board_win):
        win.append(True)
      else:
        win.append(False)
    if first:
      if any(win):
        break
    else:
      if all(win):
        break
      else:
        not_won = [i for i, x in enumerate(win) if not x]
      
    idx += 1

  if first:
    aa = [int(i) for i, x in enumerate(win) if x]
  else:
    aa = not_won
    
  bb = sum(boards[aa[0]], [])

  return sum(list(set(bb) - set(balls[:idx]))) * balls[idx-1]

# Setup

f = open("day_4.txt", "r")

input = f.read().splitlines()

f.close()

# Get balls and boards
balls = input[0].split(",")

balls = [int(ele) for ele in balls]

boards = get_boards(input[1:])

# Part 1 answer
print(winner(balls, boards))

# Part 2 answer
print(winner(balls, boards, first=False))
