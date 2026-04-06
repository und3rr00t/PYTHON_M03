import random


def gen_player_achievements() -> set[str]:
    achievements_pool: list[str] = [
        "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
        "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
        "Hidden Path Finder", "First Steps", "Collector Supreme",
        "Untouchable", "Sharp Mind", "Boss Slayer"
    ]

    num: int = random.randint(3, 8)
    chosen: list[str] = random.sample(achievements_pool, num)
    res: set[str] = set()
    for c in chosen:
        res = res.union({c})
    return res


def main() -> None:
    print("=== Achievement Tracker System ===")

    set_alice: set[str] = gen_player_achievements()
    set_bob: set[str] = gen_player_achievements()
    set_charlie: set[str] = gen_player_achievements()
    set_dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {set_alice}")
    print(f"Player Bob: {set_bob}")
    print(f"Player Charlie: {set_charlie}")
    print(f"Player Dylan: {set_dylan}")

    all_dist: set[str] = (
        set_alice.union(set_bob).union(set_charlie).union(set_dylan)
    )
    print(f"All distinct achievements: {all_dist}")

    common: set[str] = (
        set_alice.intersection(set_bob)
        .intersection(set_charlie)
        .intersection(set_dylan)
    )
    print(f"Common achievements: {common}")

    only_alice: set[str] = set_alice.difference(
            set_bob.union(set_charlie).union(set_dylan)
        )
    only_bob: set[str] = set_bob.difference(
            set_alice.union(set_charlie).union(set_dylan)
        )
    only_charlie: set[str] = set_charlie.difference(
            set_alice.union(set_bob).union(set_dylan)
        )
    only_dylan: set[str] = set_dylan.difference(
            set_alice.union(set_bob).union(set_charlie)
        )

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    miss_alice: set[str] = all_dist.difference(set_alice)
    miss_bob: set[str] = all_dist.difference(set_bob)
    miss_charlie: set[str] = all_dist.difference(set_charlie)
    miss_dylan: set[str] = all_dist.difference(set_dylan)

    print(f"Alice is missing: {miss_alice}")
    print(f"Bob is missing: {miss_bob}")
    print(f"Charlie is missing: {miss_charlie}")
    print(f"Dylan is missing: {miss_dylan}")


if __name__ == "__main__":
    main()
