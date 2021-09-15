class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_mapping = {name: i for i, name in enumerate(list1)}
        list2_mapping = {name: i for i, name in enumerate(list2)}
        common_names = set(list1).intersection(set(list2))
        ret = []
        best = len(list1) + len(list2)
        scores = {}
        for name in common_names:
            score = list1_mapping[name] + list2_mapping[name]
            scores[name] = score
            best = min(best, score)
        final_list = []
        for name, score in scores.items():
            if score == best:            
                final_list.append(name)
        return final_list