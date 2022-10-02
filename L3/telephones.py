"""https://open.kattis.com/problems/telephones"""
while (cmd := input().split()) != ['0', '0']:
    calls, intervals = map(int, cmd)
    phones = list()
    for call in range(calls):
        _, _, start, dur = map(int, input().split())
        phones.append((start, start + dur))
    for interval in range(intervals):
        start, dur = list(map(int, input().split()))
        toPrint = 0
        for callStart, callEnd in phones:
            if callStart <= start < callEnd or start <= callStart < start + dur:
                toPrint += 1
        print(toPrint)