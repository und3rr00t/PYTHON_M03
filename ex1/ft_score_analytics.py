import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    args_len: int = len(sys.argv)
    if args_len == 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores: list[int] = []
    i: int = 1
    while i < args_len:
        arg: str = sys.argv[i]
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        i += 1

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")

    avg: float = sum(scores) / len(scores)
    print(f"Average score: {avg}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
