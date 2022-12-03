import random


class student:
    def __init__(self, name):
        self.name = name
        self.balance = 200
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.gladness1 = random.randint(1, 2)
        self.workexp = 0

    def to_work(self):
        print("Half-time work")
        if self.gladness1 == 1:
            self.workexp += 10
            self.balance += 30
            self.progress += 10
        if self.gladness1 == 2:
            self.balance += 20
            self.gladness -= 2

    def to_study(self):
        print('Time to study!...')
        self.progress += 0.65
        self.gladness -= 1.10
        self.workexp += 2
        self.balance += 1

    def to_sleep(self):
        print('Time to sleep!...')
        self.progress -= 0.15
        self.gladness += 2.10

    def to_chill(self):
        print('Time to chill!...')
        self.progress -= 0.12
        self.gladness += 5.40
        self.balance -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print("He was excluded...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion")
            self.to_chill()
        elif self.progress > 5:
            print("He finish the collage")
            self.alive = True
            self.gladness = +50
        elif self.balance <= 0:
            self.alive = False


    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Balance = {self.balance}$')
        print(f'Workexperience = {self.workexp}')

    def live(self, day):
        day = "Day " + str(day) + ' of ' + self.name + " life"
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_study()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

sasha = student(name="Sasha")
for day in range(365):
    if sasha.alive == False:
        break
    sasha.live(day)
