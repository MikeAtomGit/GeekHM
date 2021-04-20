import time
class TrafficLight():
    __colour = ['red', 'yellow', 'green']

    def running(self, start):
        self.start = start
        colour = TrafficLight.__colour
        while True:
            if self.start == 'q':
                break
            else:
                for each in colour:    
                    if each == 'red':
                        print('You shall not pass!!!')
                        time.sleep(7)
                    elif each == 'yellow':
                        print('Wait a little bit')
                        time.sleep(2)
                    elif each == 'green':
                        print('You can go')
                        time.sleep(9)
                   

t1 = TrafficLight()

t1.running(input('Press Enter to start, q to quit'))
