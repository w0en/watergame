class Entry:
    def __init__(self, color, hidden):
        self.color = color #hexstring, value of -1 if empty
        self.hidden = hidden #boolean
        
    def __repr__(self):
        if self.hidden:
            return "?"
        else:
            return f"{self.color}"

    def __str__(self):
        if self.hidden:
            return "?"
        else:
            return f"{self.color}"
    
    def __eq__(self, other):
        """Simple check if two Entrys are equal. They are equal if neither is empty and they have the same color"""
        if self.hidden or other.hidden == True:
            return False
        else:
            if self.color == other.color:
                return True
            return False
        
        
    def __hash__(self):
        """Simple override of hash function for equality checks"""
        if self.hidden:
            return hash(self.color)
        else:
            return hash(self.color + 16777216)
        
    def unhide(self):
        """Sets the hidden property of Entry to False. Does nothing if the Entry is already not hidden."""
        self.hidden = False