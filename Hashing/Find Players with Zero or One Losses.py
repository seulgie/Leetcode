class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_loss = set()

        for winner, loser in matches:

            # First, add winner
            if (winner not in one_loss) and (winner not in more_loss):
                zero_loss.add(winner)
            # Then, add or remove loser
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_loss.add(loser)
            elif loser not in more_loss:
                one_loss.add(loser)
            else: continue

        return [sorted(list(zero_loss)), sorted(list(one_loss))]
        
