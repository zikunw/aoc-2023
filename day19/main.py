
class Workflow:
    def __init__(self, workflow):
        workflow = workflow.split("{")
        self.name = workflow[0]
        ops = workflow[1].split(",")
        self.comparisons = [Comparison(c) for c in ops[:-1]]
        self.result = ops[-1][:-1]
        
    def process(self, part):
        for comp in self.comparisons:
            result = comp.process(part)
            if result:
                return result
        return self.result
        
    def __str__(self):
        return f"Name: {self.name}, Comparisons: {self.comparisons}, Result: {self.result}"
    
    def __repr__(self):
        return self.__str__()
        
class Comparison:
    def __init__(self, comparison):
        self.attribute = comparison[0]
        self.operator = comparison[1]
        self.value = int(comparison[2:].split(":")[0])
        self.goto_workflow = comparison[2:].split(":")[1]
        
    def process(self, part):
        if self.operator == ">":
            if getattr(part, self.attribute) > self.value:
                return self.goto_workflow
        elif self.operator == "<":
            if getattr(part, self.attribute) < self.value:
                return self.goto_workflow
        return None
        
    def __str__(self):
        return f"({self.attribute} {self.operator} {self.value} : {self.goto_workflow})"
    
    def __repr__(self):
        return self.__str__()
    
class Part:
    def __init__(self, part):
        part = part[1:-1].split(",")
        self.x = int(part[0][2:])
        self.m = int(part[1][2:])
        self.a = int(part[2][2:])
        self.s = int(part[3][2:])
        
    def __str__(self):
        return f"({self.x},{self.m},{self.a},{self.s})"
    
    def __repr__(self):
        return self.__str__()

def main():
    with open('day19/input.txt') as f:
        data = f.read().splitlines()
    
    workflows = {}
    parts = []
    for line in data:
        if line == "": continue
        if line[0] != "{": 
            w = Workflow(line)
            workflows[w.name] = w
        else:
            parts.append(Part(line))
            
            
    # print(workflows)
    # print(parts)
    
    rating = 0
    for part in parts:
        workflow = workflows["in"]
        while True:
            result = workflow.process(part)
            if result == "A":
                rating += part.x + part.m + part.a + part.s
                break
            if result == "R":
                break
            workflow = workflows[result]
    
    print(rating)

    
       
if __name__ == '__main__':
    main()
    
    # w = Workflow("px{a<2006:qkq,m>2090:A,rfg}")
    # p = Part("{x=3000,m=2655,a=3000,s=2876}")
    # print(w.process(p))