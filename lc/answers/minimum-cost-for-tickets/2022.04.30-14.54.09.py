class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_to_next_index = [0]
        prev = 0
        for i, day in enumerate(days):
            day_to_next_index += [i] * (day - prev)
            prev = day

        @cache
        def get_cheapest(curr_index):
            res = float("inf")
            for j, coverage in enumerate([1, 7, 30]):
                nxt = days[curr_index] + coverage
                nxt = None if nxt >= len(day_to_next_index) else day_to_next_index[nxt]
                res = min(res, costs[j] if nxt is None else costs[j] + get_cheapest(nxt))
            return res
        return get_cheapest(0)
