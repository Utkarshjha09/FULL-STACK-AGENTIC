from multiprocessing import Process
import time


def brew_chai(flavour):
    print(f"Start of {flavour} chai served")
    time.sleep(3)
    print (f"End of {flavour} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target= brew_chai, args=(f"Chai Maker #{i+1}"))
        for i in range(3)
    ]

    # Start all Process
    for p in chai_makers:
        p.start()

    # wait for all to complete 
    for p in chai_makers:
        p.join()




