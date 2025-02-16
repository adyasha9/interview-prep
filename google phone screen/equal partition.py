# You are given a list of vote power and states


# votesPower = [1,5,7,8,9,10,20]
# states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]


# And you have two candidates C1 and C2, you need to return a List of List of states that we can make in such an order that both candidates receive the same amount of votes.


# Example: [["California", "Texas", "Florida", "Indiana", "Alaska"], ["Ohio", "Hawaii"]]
# The list can have different combinations, you need to return all the lists of combinations.


# What would be the optimal solution for this problem?

def equal_vote_partitions(votesPower, states):
    total_votes = sum(votesPower)
    if total_votes % 2 != 0:
        return []
    target = total_votes // 2
    results = []
    def backtrack(i,current_votes,current_states):
        if i >= len(states) or current_votes > total_votes:
            return 
        if current_votes == target:
            complement = [states[i] for i in range(len(states)) if states[i] not in current_states ]
            results.append([current_states[:],complement])
            return
        current_states.append(states[i])
        backtrack(i+1,current_votes+votesPower[i],current_states)
        current_states.pop()
        backtrack(i+1,current_votes,current_states)
    backtrack(0,0,[])
    return results
votesPower = [1, 5, 7, 8, 9, 10, 20]
states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]
print(equal_vote_partitions(votesPower, states))