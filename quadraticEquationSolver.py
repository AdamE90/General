def solve(a, b, c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0 or a == 0:
        return None
    x = []
    x.append((-b + discriminant**0.5)/(2*a))
    if discriminant != 0 : x.append((-b - discriminant**0.5)/(2*a))
    return x

if __name__ == "__main__":
    # x^2+2x+1
    print(solve(1, 2, 1)) # [-1]
