def tower_of_hanai(n,s,h,d):
    if n==1:
        print(f"move 1st disk from {s} to {d}")
        return
    tower_of_hanai(n-1,s,d,h)
    print(f"move disk num {n} disk from {s} to {d}")
    tower_of_hanai(n-1,h,s,d)

tower_of_hanai(3,"s","h","d")