import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
        parts: list[str] = user_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        error_found: bool = False
        for p in parts:
            try:
                float(p.strip())
            except ValueError as err:
                print(f"Error on parameter '{p.strip()}': {err}")
                error_found = True
                break

        if error_found:
            continue

        return (
            float(parts[0].strip()),
            float(parts[1].strip()),
            float(parts[2].strip())
        )


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center: float = math.sqrt((pos1[0]**2) + (pos1[1]**2) + (pos1[2]**2))
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_pts: float = math.sqrt(
                                ((pos2[0] - pos1[0])**2) +
                                ((pos2[1] - pos1[1])**2) +
                                ((pos2[2] - pos1[2])**2)
                            )
    print(f"Distance between the 2 sets of coordinates: {round(dist_pts, 4)}")


if __name__ == "__main__":
    main()
