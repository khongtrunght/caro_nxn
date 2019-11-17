from IPython.display import clear_output
from os import system, name
import random
from typing import List, Any


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class boards(object):
    
    def __init__(self,n):
        self.boards_init = [[' ']*n for i in range(n)]
        self.n = n
        self.boards1 = self.boards_init

    def lay_o_danh(self,plr):
        vi_tri = '0'
        while int(vi_tri) not in range(1,self.n ** 2 + 1 ) or  self.check_mark(int(vi_tri)) :
            vi_tri = input("Bạn %s chọn ô nào để đánh : " %(plr.name))
        i = int(vi_tri) // (self.n -1)
        j = int(vi_tri) - i*(self.n -1)
        self.boards1[i][j] = plr.marked

    def check_win(self,i,j):
        pass

    def check_full(self):
        if ' ' not in self.boards :
            return True
        return False
    
    def check_mark(self, x):
        i = x // (self.n -1)
        j = x - i*(self.n -1)
        if self.boards1[i][j] == ' ' :
            return False
        return True
    
    def show_up(self,i,j) :
        if self.boards1[i][j]  != ' ' :
            return self.boards1[i][j]
        return str(i*(self.n-1)+j)
        

    def show_boards(self):
        clear()
        for i in range(self.n):
            print (' ')
            for j in range(self.n ):   
              #hom sau sua lai theo error except 
                if self.show_up(i,j) not in ('X','O') :
                    print( format(int(self.show_up(i,j)),'03d') + ' | '  , end = '')
                else :
                    print( ' ' + self.show_up(i,j) + ' ' + ' | '  , end = '')
            print('\n' + '-'*self.n*9)


        





class player(object):
    def __init__(self):
        self.marked = ' '
        self.name = input("Tên của người chơi là gì ? :  ")
        self.marked = input("Chọn kí hiệu cho %s :  " %(self.name)) 

    def pick_o(self,bod):
        #i = x // (bod.n -1)
        #j = x - i*(bod.n -1)
        bod.lay_o_danh(self)




class bot_player(player):
    
    def __init__(self):
        self.name = "Bot"
        #chon bieu tuong cua bot 

def coop_mode() :
    global bang 
    bang = boards(20)
    global players 
    global luot
    players = []
    players.append( player())
    players.append( player())
    import random
    pick_first = random.randint(0,1)
    print("Xin chúc mừng bạn %s đã được đánh trước !! " %(players[pick_first])) 
    global on_game
    luot = pick_first
    while on_game :
        bang.show_boards()
        players[luot].pick_o(bang)
        if bang.check_win :
            print("Chúc mừng %s đã chiến thắng !!  "%(players[luot].name))
            on_game = False
        else:
            if bang.check_full():
                print("Không ai thắng cả :(( ")
                on_game = False
            else:
                Luot = abs(luot -1 )

        



    

def main() :
    while True :
        print(" Chào mừng bạn đến với trò chơi caro v2 <3 !!! \n")
        Select_mode = input(" Mời bạn chọn chế độ chơi : Bot hay Coop (B/C)")
        global on_game
        on_game = True 
        while on_game :  
            if Select_mode == 'C' :
                coop_mode()
            else :
                print('Not yet developed')
                on_game = False
            # bot_mode()
        choi_tiep = input(" Ban co muon choi tiep : Y / N : ")
        if choi_tiep == 'N':
            exit(0)

main()

