import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx: int = random.randint(0, len(event_list) - 1)
        item: tuple[str, str] = event_list.pop(idx)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list.append(next(event_stream))

    print(f"Built list of 10 events: {event_list}")

    consumer = consume_event(event_list)
    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
