import class_entry

class Tube:
    # tube is a stack
    def __init__(self, capacity, entries):
        
        self.capacity = capacity
        self.entries = entries #list of instances of Entry; hexstrings to represent color
        self.size = len(entries)
        self.solved = self.is_solved()
        self.score = self.calculate_score()
            
        assert self.size <= self.capacity
        assert all(isinstance(entry, class_entry.Entry) for entry in self.entries)
        if self.size > 0:
            for i in range(self.size):
                if not self.entries[i].hidden:
                    assert all(not entry.hidden for entry in self.entries[i:-1])
        
    def __repr__(self):
        return f"Tube: Entries: {self.entries}, Solved: {self.solved}"

    def __str__(self):
        return f"Tube: Entries: {self.entries}\nCapacity: {self.capacity}, Solved: {self.solved}"
    
    
    def __eq__(self, other):
        """Simple check to see if two instances of Tube are equal. Two instances of tube are equal if they have the same entries in the same order.

        Args:
            other (Tube): Other instance of Tube to check equality with

        Returns:
            _type_: Boolean
        """
        assert self.solved ==  other.solved
        assert self.score == other.score
        
        if (self.size != other.size) or (self.capacity != other.capacity):
            return False
        else:
            for i in range(len(self.entries)):
                if self.entries[i] != other.entries[i]:
                    return False
            return True
    
    def calculate_score(self):
        """Number of entries in the tube of the same color as the top of the stack. Does not count empty entries. The top n items being the same gives a score of n - 1.

        Returns:
            int: Score of the instance of Tube.
        """
        if self.size == 0:
            score = 1
        else:
            color = self.entries[-1].color
            score = 1
            for entry in reversed(self.entries):
                if entry.color != color or entry.hidden:
                    break
                score += 1
        return 2 ** score
        
    def is_empty(self):
        """Check to see if instance of Tube is empty. Returns true if there are no entries.

        Returns:
            Boolean: Status of instance of Tube being empty.
        """
        if self.size == 0:
            return True
        return False
        
    def is_solved(self):
        """Check for Tube being solved. A tube is solved when:
            1) the tube is empty OR
            2) the tube has no hidden entries AND every entry is the same.

        Returns:
            Boolean: True if the Tube has been solved. False otherwise.
        """
        solved = False
        if self.is_empty(): #Tube has no entries
            #print("Tube has no entries. It is trivially solved.")
            solved = True
        elif any(entry.hidden for entry in self.entries): #Tube has hidden entries
            #print("Tube has at least 1 hidden entry. It is not solved.")
            solved = False
        elif len(set(self.entries)) == 1: #Tube has no hidden entries and is only 1 color
            #print("Tube has no hidden entries and all entries are the same color. It is solved.")
            solved = True
        else: #Tube has no hidden entries and has more than 1 color
            #print("Tube has no hidden entries but has at least 2 different colors. It is not solved. There may be further cases unaccounted for.")
            solved = False
        return solved


    def update(self):
        self.size = len(self.entries)
        self.solved = self.is_solved()
        if self.size >= 1:
            self.entries[-1].unhide()
        self.score = self.calculate_score()
    

def is_valid_move(source, destination):
    if source.is_empty():
        #print("Source is empty. Move is trivially invalid.")
        return False
    else:
        if destination.is_empty():
            #print("Source is not empty and Destination is empty. Move is trivially valid.")
            source_color = source.entries[-1].color
            #print(f"Color attempted to be poured is {source_color}.")
            return True
        else:
            #print("Source is not empty and Destination is not empty. Checking for color compatibility.")
            destination_color = destination.entries[-1].color
            #print(f"Valid color to be poured is {destination_color}.")
            source_color = source.entries[-1].color
            #print(f"Color attempted to be poured is {source_color}.")
            if source_color == destination_color:
                #print("Source color is the valid color. Move is valid.")
                return True
            else:
                #print("Source color is not the valid color. Move is invalid.")
                return False
    