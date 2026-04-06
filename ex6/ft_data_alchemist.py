import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
        'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    cap_all: list[str] = [p.capitalize() for p in initial_players]
    print(f"New list with all names capitalized: {cap_all}")

    only_cap: list[str] = [p for p in initial_players if p[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    score_dict: dict[str, int] = {p: random.randint(0, 1000) for p in cap_all}
    print(f"Score dict: {score_dict}")

    total: int = sum([score_dict[k] for k in score_dict])
    count: int = len(score_dict)
    avg: float = total / count if count > 0 else 0.0
    print(f"Score average is {round(avg, 2)}")

    high_scores: dict[str, int] = {
        k: score_dict[k] for k in score_dict if score_dict[k] > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
