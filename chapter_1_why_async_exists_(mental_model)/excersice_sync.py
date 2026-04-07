import time

def fake_api_call(id):
    time.sleep(2)
    return 2

def main():
    total = 0
    total += fake_api_call(1)
    total += fake_api_call(2)
    total += fake_api_call(3)
    total += fake_api_call(4)
    total += fake_api_call(5)

    print(total)

main()