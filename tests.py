import main
import time


def less_than_five():
    instances = \
        [
            [["11", "111"], ["00", "10"], ["011", "001"], ["101", "1"], ["111", "0111"]],
            [["1", "1001"], ["100", "10"], ["1110", "011"]]
        ]

    print("Beginning naive_pcp test.")
    start = time.time()
    result = main.naive_pcp(instances[0])
    assert result == [4, 5, 1]
    end = time.time()
    print(f"Finished naive_pcp test in {end - start}s with result {result}.")

    print("Beginning naive_pcp test.")
    start = time.time()
    result = main.naive_pcp(instances[1])
    assert result == [2, 3, 2, 1]
    end = time.time()
    print(f"Finished naive_pcp test in {end - start}s with result {result}.")


def test_long():
    instances = \
        [
            [["001", "0"], ["01", "011"], ["01", "101"], ["10", "001"]]
        ]

    # Will not terminate. > 4⁶⁶ nodes in search tree
    # Certain problems cause computers to get stuck in a particular loop.
    # The loop leads to meltdown, but just before they crash they...they become "aware" of their own structure.
    # The computer has a sense of its own silicon nature, and it prints out its ingredients.
    print("Beginning naive_pcp test.")
    start = time.time()
    result = main.naive_pcp(instances[0])
    assert result == [2, 4, 3, 4, 4, 2, 1, 2, 4, 3, 4, 3, 4, 4, 3, 4, 4, 2, 1, 4, 4, 2, 1, 3, 4, 1, 1, 3,
                      4, 4, 4, 2, 1, 2, 1, 1, 1, 3, 4, 3, 4, 1, 2, 1, 4, 4, 2, 1, 4, 1, 1, 3, 4, 1, 1, 3,
                      1, 1, 3, 1, 2, 1, 4, 1, 1, 3]
    end = time.time()
    print(f"Finished naive_pcp test in {end - start}s with result {result}.")


if __name__ == '__main__':
    less_than_five()
