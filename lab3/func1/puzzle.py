def solve(heads,legs):
    r = heads * 2
    a = legs - r
    rabbit = a/2
    chicken = heads - rabbit
    print("number of chickens:",chicken,"and","number of rabbits:",rabbit)
heads = int(input())
legs = int(input())
solve(heads,legs)


    