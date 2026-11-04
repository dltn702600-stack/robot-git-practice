from config import MAX_SPEED, ROBOT_NAME


def move_forward(speed):
    if speed > MAX_SPEED:
        print(f"최대 속도 {MAX_SPEED}를 초과했습니다.")
        return

    print(f"{ROBOT_NAME}이(가) 속도 {speed}로 전진합니다.")


if __name__ == "__main__":
    move_forward(0.15)
    move_forward(0.3)