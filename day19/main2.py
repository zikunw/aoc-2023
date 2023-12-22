attrMap = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}

class Workflow:
    def __init__(self, workflow):
        workflow = workflow.split("{")
        self.name = workflow[0]
        ops = workflow[1].split(",")
        self.comparisons = [Comparison(c) for c in ops[:-1]]
        self.result = ops[-1][:-1]
        
    def processSegment(self, segment):
        results = []
        for comp in self.comparisons:
            seg1, seg2 = comp.process(segment)
            results.append(seg1)
            segment = seg2
        results.append([self.result] + segment)
        return results
            
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
        
    def process(self, segment):
        if self.operator == ">":
            i = attrMap[self.attribute]
            seg1 = segment.copy()
            seg1[i] = [max(seg1[i][0], self.value+1), seg1[i][1]]
            seg1 = [self.goto_workflow] + seg1
            seg2 = segment.copy()
            seg2[i] = [seg2[i][0], min(seg2[i][1], self.value)]
            return seg1, seg2
        elif self.operator == "<":
            i = attrMap[self.attribute]
            seg1 = segment.copy()
            seg1[i] = [seg1[i][0], min(seg1[i][1], self.value-1)]
            seg1 = [self.goto_workflow] + seg1
            seg2 = segment.copy()
            seg2[i] = [max(seg2[i][0], self.value), seg2[i][1]]
            return seg1, seg2
        raise Exception("Invalid operator")

        
    def __str__(self):
        return f"({self.attribute} {self.operator} {self.value} : {self.goto_workflow})"
    
    def __repr__(self):
        return self.__str__()
    

def main():
    with open('day19/input.txt') as f:
        data = f.read().splitlines()
    
    workflows = {}
    for line in data:
        if line == "": continue
        if line[0] != "{": 
            w = Workflow(line)
            workflows[w.name] = w
            
            
    print(workflows)
    
    total = 0
    num_seg = [
        "in",
        [1, 4000], # x
        [1, 4000], # m
        [1, 4000], # a
        [1, 4000]  # s
    ]
    stack = []
    stack.append(num_seg)
    while stack != []:
        seg = stack.pop()
        
        # check illegal
        for i in range(1, len(seg)):
            if seg[i][0] > seg[i][1]:
                continue
        
        # check if done
        if seg[0] == "A":
            total += (seg[1][1]-seg[1][0]+1) * (seg[2][1]-seg[2][0]+1) * (seg[3][1]-seg[3][0]+1) * (seg[4][1]-seg[4][0]+1)
            continue
        if seg[0] == "R":
            continue
        
        workflow = workflows[seg[0]]
        results = workflow.processSegment(seg[1:])   
        stack.extend(results)     
    
    print(total)
       
if __name__ == '__main__':
    main()
    # w = Workflow("px{a<2006:qkq,m>2090:A,rfg}")
    # num_seg = [
    #     [1, 4000], # x
    #     [1, 4000], # m
    #     [1, 4000], # a
    #     [1, 4000]  # s
    # ]
    # results = w.processSegment(num_seg)
    # for r in results:
    #     print(r) 
    
    # 167409079868000
    # 60833083306830