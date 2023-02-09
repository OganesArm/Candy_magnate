from random import randint


class Arena:
    waiting=[] #очередь
    combats=[]
    print(waiting)
    def __init__(self):
        self.new_duel()

    def new_duel(self):
        self.waiting.append(Duel(150))

    def __str__(self):
        return f'В ожидании: {self.waiting} | в бою: {self.combats}'
        
          


class Duel:
    def __init__(self, total: int):
        self.first_id=0
        self.second_id=0
        self.total=total
        self.full=False
        self.current=0

    def add(self, user_id:int):  # Добавляем второй т.к. первй не равен нулю
        if self.first_id != 0:
            self.second_id=user_id
            self.full=True
        else:
            self.first_id=user_id

    def get_total(self):
        return self.total

    def set_total(self,count):
        self.total -=count

    def first(self):
        return self.first_id

    def second(self):
        return self.second_id

    def current_move(self):
        return self.current

    def switch(self):
        if self.current==self.first_id:
            self.current=self.second_id
        else: self.current=self.first_id

    def enemy(self):
        if self.current==self.first_id:
            return self.second_id
        else: 
            return self.first_id

    def first_move(self):
        coin=randint(0,1)
        if coin:
            self.current=self.first_id
        else:
            self.current=self.second_id


    def __str__(self):
        return f'Да начнется великая битва!\n{self.first_id} против {self.second_id}'