from impl.parser import parse

if __name__ == '__main__':
    circles = parse("../data/0406PT-000070.dxf")
    for circle in circles:
        print(circle)
        print()
    # locator("data/dwg.png", 90, (30, 60))
