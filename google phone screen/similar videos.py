# Given a list of 𝑁 videos, each associated with k tags, determine all similar videos
#  for a given video 𝑖 by checking the videos from index 0 to 𝑖 − 1 .
#  Two videos are considered similar if they share at least one tag in common.


# Keep in mind N>>>>>k.
# videos = [
#     ["sports", "fitness"],  # Video 0
#     ["cooking", "food"],    # Video 1
#     ["sports", "health"],   # Video 2 (shares "sports" with Video 0)
#     ["fitness", "health"],  # Video 3 (shares "fitness" with Video 0, "health" with Video 2)
#     ["technology"]          # Video 4 (no common tags with previous videos)
# ]

def findSimilarVideos(videos):
    n = len(videos)
    hashmap = {}
    res = [[] for _ in range(n)]
    for i,video in enumerate(videos):
        current_tags = set(video)
        similar_set = set()
        for tag in current_tags:
            if tag in hashmap:
                similar_set.update(hashmap[tag])
            hashmap.setdefault(tag,[]).append(i)
        res[i] = sorted(similar_set)
    return res


videos = [
    ["sports", "fitness"],  # Video 0
    ["cooking", "food"],    # Video 1
    ["sports", "health"],   # Video 2 (shares "sports" with Video 0)
    ["fitness", "health"],  # Video 3 (shares "fitness" with Video 0, "health" with Video 2)
    ["technology"]          # Video 4 (no common tags)
]

print(findSimilarVideos(videos))

        

    

