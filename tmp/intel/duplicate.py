import requests

URL="https://jsonplaceholder.typicode.com/posts"

# output:
# Duplicate userid Found:
# userid:1 - Count: 10

def find_duplicate(data):
    results = {}
    for i in data:
        #print(i['userId'])
        if i["userId"] in results:
            results[i['userId']]+=1
        else:
            results[i['userId']]=1
    print(results)




if __name__ == '__main__':
    response = requests.get(URL)
    data = response.json()
    find_duplicate(data)