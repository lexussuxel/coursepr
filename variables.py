BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 1000
HEIGHT = 600
G = 9.8
FPS = 60

score = 0
count_music = 0
prev_c = 0

ball_size = (80, 80)
ball_start_pos = (200, 400)
basket_size = (220, 220)
basket_start_pos = (WIDTH - basket_size[0], 100)
basket_left_line = [[800, 170], [800, 300]]
basket_middle_line = [[920, 170], [920, 300]]
basket_right_line = [[980, 100], [980, 320]]
line_pos = [[0, ball_start_pos[1] + ball_size[0]], [WIDTH, ball_start_pos[1] + ball_size[0]]]


