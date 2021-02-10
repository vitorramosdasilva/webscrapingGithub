

def ready_txt():
    filepath = 'repositories.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    return line

ready_txt()