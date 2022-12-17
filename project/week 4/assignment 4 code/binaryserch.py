def binary_search(keys, query):
    if len(keys)==1 and keys[0]!=query:
        return -1
    m=int((len(keys)/2))
    if keys[m]==query:
        return m
    elif keys[m]>query:
        return m- binary_search(keys[0:m],query)
    else:
        return m+2+ binary_search(keys[m+1:len(keys)],query)
    
        
    

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')