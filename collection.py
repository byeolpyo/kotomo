class Collection():
    def __init__(self, vals):
        # pet attributes
        self.vals = vals
        self.current_index = 0
        self.size = len(vals)
            
    def insert_val(self, val):
        if self.size == 0:
            self.size = 1
            self.vals = [val]
            self.current = val
            return
        self.vals.append(val)
        self.size = self.size + 1

    def next_val(self):
        if self.size == 0:
            return
        self.current_index = self.current_index + 1 
        self.current_index = self.current_index % self.size
        self.current = self.vals[self.current_index]
    
    def change_val(self, index):
        if self.size == 0:
            return
        if index >= self.size:
            return
        self.current_index = index 
        self.current = self.vals[self.current_index]