
import functools

def main():
   print(coin_challenge("$", range(5)))




def coin_challenge(coin, numbers):
    return (functools.reduce(lambda x, y: x + y, [coin + str(numbers[x]) + ", " for x in range(numbers[-1] + 1)]))
    
        


if __name__ == "__main__":
    main()