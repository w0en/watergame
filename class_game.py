import random
import pprint as pp
import class_entry
import class_tube

class Game:
    def __init__(self, colors, tubes, slots): #maybe a different constructor for games with tubes with different number of slots
        assert tubes >= 0
        assert colors >= 0
        assert slots >= 0
        
        self.solved = False
        
        if tubes <= colors:
            #game is unsolvable except for the trivial game if tubes = colors and always if tubes < colors, so this should be turned into a try catch maybe
            pass
        elif tubes == colors + 1:
            #some games are solvable, not all
            print("Are you sure you only want 1 more tube than there are colors? The game may not be solvable!")
            pass
        else:
            self.slots = slots #future improvements could give different tubes different numbers of slots
            all_entries = []
            for i in range(1, colors + 1):
                all_entries.append([i] * slots)
            flat_list = list()
            for sub_list in all_entries:
                flat_list += sub_list
            all_entries = flat_list
            random.shuffle(all_entries);
        assert len(all_entries) == (tubes - 2) * slots
        tube_list = []
        chunk_size = 4
        for i in range(0, len(all_entries), chunk_size):
            tube = class_tube.Tube(all_entries[i:i + chunk_size])
            tube_list.append(tube)
        for i in range(len(tube_list), tubes):
            tube_list.append(class_tube.Tube([0] * slots))
        self.tubes = tube_list

    def __init__(self, tube_list): #TODO: NOT DONE
        for tube in tube_list:
            assert tube.size >= 0
        self.tubes = tube_list
        assert len(self.tubes) > 0
        self.solved = self.is_solved()
        self.colors = list(set([entry.color for tube in tube_list for entry in tube.entries]))
        
    def __repr__(self):
        return f"Game:\n    Solved: {self.solved}\n    Number of tubes: {len(self.tubes)}\n    Colors: {self.colors}"

    def __str__(self):
        return f"Game:\n    Solved: {self.solved}\n    Number of tubes: {len(self.tubes)}\n    Colors: {self.colors}"

    def is_solved(self):
        if all(tube.is_solved() for tube in self.tubes): #This will break if for a particular color, there are more entries of that color than any tube can hold (e.g. 6 blues, but the biggest capacity of any tube is 4)
            if len(list(filter(lambda tube: not tube.is_empty(), self.tubes))) == len(self.colors):
                self.solved = True
                return True
        else:
            self.solved = False
            return False
        
    def update(self):
        self.solved = self.is_solved()
        
    
    def pour(self, source, destination):
        
        #print(f"Source: {source}\nDestination: {destination}")
        
        if class_tube.is_valid_move(source, destination):
            
            limit = destination.capacity - destination.size
            move_color = source.entries[-1].color # it might be safer to do based off destination instead of source, but this deals with the case of empty destination
            move_size = 0
            
            for entry in reversed(source.entries):
                if entry.color != move_color or entry.hidden:
                    break
                move_size += 1
                if move_size == limit:
                    break
                
            print(f"Move - Color: {move_color}; Size: {move_size}")
            for i in range(move_size):
                destination.entries.append(source.entries.pop())
                
            source.update()
            destination.update()
            self.update()
        else:
            
            print("Move is not valid")
            self.update()
            
        print(f"Source: {source}\nDestination: {destination}")
        
    
    
        
