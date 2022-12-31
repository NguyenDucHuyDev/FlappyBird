from os import remove
import pygame,sys, random
from pygame.transform import rotate

def draw_floor(): # vẽ sàn
        screen.blit(floor,(floor_x_pos,800))   #  hiển thị sàn thứ nhất ra màn hình tạo độ mặt đất cách x = 0  và  y = 800 .... sàn 1
        screen.blit(floor,(floor_x_pos+558, 800))   # hiển thị sàn thứ2 ra màn hình cách 1 khung cửa với x = 558  y= 800 sàn 2

def create_pipe():      # hàm tạo hình ống ngẫu nhiên
        random_pipe_pos = random.choice(pipe_height)  # chọn ngẫu nhiên chiều cao đã cho sẵn của ống
        bottom_pipe = pipe_surface.get_rect(midtop = (558, random_pipe_pos))   # vị trí ống dưới
        top_pipe = pipe_surface.get_rect(midtop = (558, random_pipe_pos-700))   # ví trí ống trên
        return top_pipe , bottom_pipe  # trả về vị trí ở trên và dưới của ống
    
def move_pipe(pipes):  # hàm di chuyển ống sang trái 
        for pipe in pipes : # lặp qua từng phần tử ống
            pipe.centerx -= 3 # cứ mỗi khi chạy -3 tức di chuyển sang trái
        return pipes  # trả về vị trí ống

def draw_pipe(pipes):   # hàm vẽ ống
        for pipe in pipes : # lặp qua từng phần tử ống
            if pipe.bottom:  # nếu như mặc định có ống này 
                 screen.blit(pipe_surface,pipe)  # sẽ hiện thị ra ống (tức vẽ)


def create_apple():  # hàm tạo hình ảnh táo ngẫu nhiên
    random_apple_pos =random.choice(apple_random)   # chọn ngẫu nhiên vị trí táo xuát hiện
    new_apple = apple_surface.get_rect(midtop = (650, random_apple_pos))  # lấy vị trí táo xuất hiện ngẫu nhiên
    return new_apple  # trả về vị trí táo ngẫu nhiên

def move_apple(apples): # hàm di chuyển sang trái đối với táo
    for apple in apples:  # Lặp qua từng phần tử táo
        apple.centerx -= 3  # cứ mỗi khi chạy -3 sang trái
    return apples   # trả về vị trí táo

def draw_apple(apples):  # vẽ táo
    for apple in apples: # Lặp qua từng phần tử táo
        screen.blit(apple_surface,apple)  # hiển thị ra màn hình quả táo

def check_collision(pipes):  # ham va cham cột
    for pipe in pipes: # lặp qua từng phần tử ống
        if panda_rect.colliderect(pipe):    #  nếu va chạm với cái ống sẽ dừng
            hit_sound.play()    # kèm âm thanh mỗi khi va chạm ống
            return False    # sẽ va chạm sẽ trả về false
        if panda_rect.top <= 0 or panda_rect.bottom >=800:     # neu <= 0  va > 825 thi se chet
            return False    # sẽ va chạm sẽ trả về false

    return True  # không pha chạm sẽ trả về true

def score_pipe(pipes): # hàm tính điểm khi qua cột
    for pipe in pipes:  # lặp qua từng phần tử ống
        if pipe.centerx - panda_rect.centerx == 61:  # nếu như tạo độ x theo trục hoành  của cái cột - chim ==61 thì được cộng điểm khi con chim đi qua ở giữa cái cột 
             score_sound.play()
             return True   
        
def check_apple(apples): # hàm tính điểm táo
    for apple in apples:  # lặp qua từng quả táo
        if panda_rect.colliderect(apple):    # nếu panda đụng trúng táo
             apples.remove(apple)  # xóa đi quả tảo vừa bị đụng trúng
             apple_sound.play() # kèm âm thanh
             return True 
        
def score_display(game_state):
    if game_state == 'score apple' :  # if game dang chay sẽ hiển thị tổng số táo 
         score_surface = game_font.render(str(int(score_apple)), True, (255,255,255))
         score_rect = score_surface.get_rect(center = (100,120))
         screen.blit(score_surface, score_rect)

    if game_state == 'life panda' :  # hiển thị tổng số mạng sống của panda
         score_life = game_font.render(f': {int(score_revival_main)}', True, (255,255,255))
         score_life_rect = score_life.get_rect(center = (500,120))
         screen.blit(score_life, score_life_rect)

    if game_state == 'score game' :  # hiển thị điểm chính
         score_surface = game_font.render(str(int(score)), True, (255,255,255))
         score_rect = score_surface.get_rect(center = (288,100))
         screen.blit(score_surface, score_rect)

    if game_state == 'game over' :  # còn nếu kết thúc sẽ hiện hàm này gồm điểm , điểm táo và điểm cao nhất và số táo
         score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))  # số điểm hiện tại
         score_rect = score_surface.get_rect(center = (288,100)) # vị trí của số điểm
         screen.blit(score_surface, score_rect) # hiển thị ra màn hình

         hight_score_surface = game_font.render(f'High Score: {int(hight_score)}', True, (255,255,255)) # số điểm cao nhất 
         hight_score_rect = hight_score_surface.get_rect(center = (288,700)) # vị trí của số điểm cao nhất
         screen.blit(hight_score_surface, hight_score_rect) # hiển thị ra màn hình

         score_apple_surface = game_font.render(f': {int(score)}', True, (255,255,255)) # số điểm táo
         hight_score_apple = score_apple_surface.get_rect(center = (395,750)) # vị trí điểm táo
         screen.blit(score_apple_surface, hight_score_apple)


def update_score(score,hight_score): # hàm high score
    if score > hight_score:          # nếu như điểm lớn hơn điểm cao nhất
            hight_score = score     # gán điểm cao nhất cho điểm trong phiên
    return hight_score              # trả về điểm cao nhất

def revival_score(apples): # hàm tính điểm táo
    for apple in apples:  # lặp qua từng quả táo
        if panda_rect.colliderect(apple):    # nếu panda đụng trúng táo
             return True             # thì sẽ trả về true

pygame.mixer.pre_init(frequency=44100, size = -16, channels=2, buffer=512)
pygame.init()
screen=pygame.display.set_mode((558,852))  # tạo cửa sổ
clock = pygame.time.Clock() #fps 
game_font = pygame.font.Font('04B_19.ttf' , 40)

# tạo các biến cho trò chơi

# chèn background
bg = pygame.image.load('./asstes/image/background.jpg').convert_alpha()

# chèn sàn
floor =pygame.image.load('./asstes/image/base.png').convert()
floor_x_pos = 0  #vị trí ban đầu mặt sàn


# chèn icon gấu
panda = pygame.image.load('./asstes/image/panda.png').convert_alpha()
panda_rect = panda.get_rect(center= (80,426))

# trọng lực
gravity = 0.25
panda_movement = 0

game_active = True   # game se hoat dong neu true
score = 0   
hight_score = 0
score_apple = 0
score_revival = 0  # điểm phụ hồi sinh panda
score_revival_main = 1   # điểm chính hồi sinh panda

# tạo ống
pipe_surface = pygame.image.load('./asstes/image/pipe.png').convert()
pipe_list = []

# tạo timer
spawnpipe = pygame.USEREVENT 
pygame.time.set_timer(spawnpipe,1200)  # sau mỗi 1.2 sẽ xuất hiện ra ống mới
pipe_height = [325,350,375,400,425,450,475,500,525,550,575,600,625,650]  # tạo ra ống ngẫu nhiên trong 3 số này.
apple_random = [50,100,150,200,250,300,350,400,450,500,550,650,700,750,800]
 
# hàm chèn táo
apple_surface = pygame.image.load('./asstes/image/cherry.png').convert_alpha()
apple_list =[]
index_apple = 0

# tạo màn hình welcome
game_welcome = pygame.image.load('./asstes/image/welcome.png').convert_alpha()


# tọa  màn hình kết thúc
game_over_surface =  pygame.image.load('./asstes/image/game-over.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (279,426))

# chèn âm thanh 
flap_sound = pygame.mixer.Sound('./asstes/audio/wing.wav')  # âm thanh mỗi khi space
hit_sound = pygame.mixer.Sound('./asstes/audio/hit.wav')  # âm thanh mỗi khi va chạm cột
score_sound = pygame.mixer.Sound('./asstes/audio/point.wav')  # âm thanh mỗi khi ghi điểm
apple_sound = pygame.mixer.Sound('./asstes/audio/apple.wav')    # âm thanh khi lượm táo

# vòng lặp của trò chơi

while True:

    for event in pygame.event.get():     # lấy tất cả sự kiện pygame xảy ra
        if event.type == pygame.QUIT or( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ) :    # tạo một cái phím để người chơi nhấn vào là thoát chương trình
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:    # tạo nhấn phím sẽ đi lên
            if event.key == pygame.K_SPACE and game_active:  # Nhấn phím space và trạng thái game hoạt động
                panda_movement =  0 # khi vào space vào thì sẽ reset lại trọng lực bằng 0 ở vị trị hiện tại
                panda_movement = -6 # khi mà space vào thì sẽ trục y -6 là sẽ đi lên
                flap_sound.play()

            if event.key == pygame.K_SPACE and game_active == False:    # nếu nhấn space sẽ bắt đầu lại từ đầu
                  game_active = True
                  pipe_list.clear()
                  apple_list.clear()
                  panda_rect.center = (80,426)
                  panda_movement = 0  # trọng lực ban đầu
                  score = 0   
                  score_apple = 0
                  score_revival = 0
                  score_revival_main = 1

        if event.type == spawnpipe:    # giành cho ống sau mỗi 1.2 giây
            pipe_list.extend(create_pipe())      # cho pygame biết mình sẽ tạo ra những cái ống tiếp theo sau 1.2 giây
            apple_list.append(create_apple())  
                

    screen.blit(bg,(0,0)) # set bg    

    if game_active == True: # nếu như game hoạt động thì những tính năng của chim và ống sẽ được kích hoạt
    #chimz 
         screen.blit(apple_surface,(50,80)) 
         screen.blit(panda,(425,95)) 

        #  over_sound.stop()

         panda_movement += gravity    
         panda_rect.centery += panda_movement 

         screen.blit(panda,panda_rect) # hiển thị ra vị trí con chim

         if(revival_score(apple_list)):
             score_revival += 1

         if(score_revival == 2): # chạy song song với điểm táo nhưng bị ẩn
             score_revival_main += 1
             score_revival = 0

         if(check_apple(apple_list)): # if như đúng thì điểm táo +1 
             score_apple += 1   
              
         if(score_pipe(pipe_list)): # if như đúng thì điểm khi qua cột sẽ + 1
            score +=1

         confirm =  check_collision(pipe_list)
         if(game_active == True and score_revival_main <= 1 ):
            game_active = confirm # khi mà chim đụng cái ống thì sẽ chuyển ra màn hình kết thúc

         if(confirm == False and score_revival_main > 1):
             game_active = True
             panda_rect.center = (80,426)
             panda_movement = 0
             pipe_list.clear()
             apple_list.clear()
             score_revival_main  -= 1
    #ống
         pipe_list = move_pipe(pipe_list) # nó sẽ lấyy tất cả ống có trong pipeList và trả về pipeList mới 
         draw_pipe(pipe_list)

         apple_list = move_apple(apple_list)
         draw_apple(apple_list)
                  
         score_display('score game')
         score_display('score apple')
         score_display('life panda')
         
    if game_active == False:
         screen.blit(game_over_surface,game_over_rect)
         hight_score  = update_score(score,hight_score)  # cập nhật điểm high score
         score_display('game over')  
         screen.blit(apple_surface,(325,725)) # set bg       

    # sàn 
    floor_x_pos -=2              # cứ mỗi lần lặp là lùi 1 tức là chạy về bên trái
    draw_floor()     

    if floor_x_pos <= -558: # nếu như mặt sàn bé hơn hoặc -558 thì sẽ trở về không
       floor_x_pos = 0
         
    pygame.display.update()      # để hiện lại cửa sổ màn hình
    clock.tick(120)              #FPS 
