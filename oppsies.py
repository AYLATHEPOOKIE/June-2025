class chair():
    def __init__(self,colour,comfyness,height,price):
        self.colour=colour
        self.comfiness=comfyness
        self.height=height
        self.price=price
    
    def show(self):
        print(f"{self.colour},{self.comfiness},{self.height},{self.price}")

chai1=chair("red","not very comfy","quite small","idk £20?")
chai1.show()
