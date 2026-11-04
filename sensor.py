from config import SAFE_DISTANCE


def check_obstacle(distance):
    if distance < SAFE_DISTANCE:
        print(f"장애물 감지: 거리 {distance}m, 정지가 필요합니다.")
        return True

    print(f"주행 가능: 장애물까지 거리 {distance}m")
    return False


if __name__ == "__main__":
    check_obstacle(0.3)
    check_obstacle(0.8)