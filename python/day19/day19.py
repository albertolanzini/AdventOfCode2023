from typing import List, Tuple, Optional

class PartDispenser:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        self.start = 'in'

    def _handle_input(self, inputfile: str) -> List[List[str]]:
        with open(inputfile, 'r') as f:
            content = f.read().strip().split('\n\n')
        res = []
        for line in content:
            res.append(line.split('\n'))
        workflows_rules, parts = [], []
        for line in res[0]:
            workflows_rules.append(self.convert_to_hashmap_workflow(line))
        workflows = {}
        for workflow in workflows_rules:
            for key, rules in workflow.items():
                workflows[key] = rules
        for line in res[1]:
            parts.append(self.convert_to_hashmap_part(line))
        return workflows, parts
    
    @staticmethod
    def convert_to_hashmap_workflow(element):
        key, conditions = element.split('{', 1)
        conditions = conditions[:-1]
        conditions = conditions.split(',')
        hashmap = {key: []}
        for condition in conditions:
            if ':' in condition:
                condition_key, condition_value = condition.split(':')
                hashmap[key].append({condition_key: condition_value})
            else:
                hashmap[key].append({condition: True})
        return hashmap
    
    @staticmethod
    def convert_to_hashmap_part(element):
        conditions = element[1:-1]
        conditions = conditions.split(',')
        hashmap = {}
        for condition in conditions:
            key, value = condition.split('=')
            hashmap[key] = int(value)
        return hashmap
    
    @staticmethod
    def process_part_sequentially(part, workflows, start_workflow):
        visited_workflows = set()
        current_workflow = start_workflow

        while current_workflow not in visited_workflows:
            visited_workflows.add(current_workflow)
            rules = workflows[current_workflow]

            for rule in rules:
                for condition, action in rule.items():
                    if isinstance(action, bool):
                        if action:
                            if condition == 'A':
                                return "Accepted"
                            elif condition == 'R':
                                return "Rejected"
                            elif condition in workflows:
                                current_workflow = condition
                                break
                        else:
                            return "Rejected"

                    attr, threshold = condition.split('<') if '<' in condition else condition.split('>')
                    threshold = int(threshold)

                    if (('<' in condition and part.get(attr, float('inf')) < threshold) or 
                        ('>' in condition and part.get(attr, float('-inf')) > threshold)):
                        if action == 'R':
                            return "Rejected"
                        elif action == 'A':
                            return "Accepted"
                        else:  # Move to another workflow
                            current_workflow = action
                            break
                else:
                    continue
                break
            else:
                break

    def _process_parts_p1(self):
        workflows, parts = self.data
        total = 0

        for part in parts:
            if self.process_part_sequentially(part, workflows, self.start) == "Accepted":
                for char, val in part.items():
                    total += val

        return total
    
    def _process_n_p2(self):
        pass

def main():
    part_dispenser = PartDispenser('input.txt')
    print(part_dispenser._process_parts_p1())

if __name__ == "__main__":
    main()