class ContextManager:
    """
    Class that is contolling the context of the selected function
    """

    def __init__(self) -> None:
        pass

    def __enter__(self):    
        print("Entering ContextManager")

    def __exit__(self, *args):
        print("Exiting ContextManager")