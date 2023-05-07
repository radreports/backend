class Singleton:
 
    __shared_instance = 'GeeksforGeeks'
    __queue = {}
 
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        # return Singleton.__shared_instance
        return Singleton
 
    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            print("Already initialized")
            # raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
 