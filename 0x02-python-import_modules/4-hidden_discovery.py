#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for j in range(len(name)):
        if name[j][0] != "_" and name[j][1] != "_":
            print(name[j])
