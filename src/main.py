from Controller import Controller

if __name__ == '__main__':
    controller = Controller()
    
    for i in range(20):
        controller.simulate_step()
