import os
import random
import time
import json

# === Simulasi pilihan aksi agent ===
# 0 = default (jalan normal)
# 1 = aktifkan caching
# 2 = skip sebagian test
# 3 = jalankan paralel (simulasi)
actions = {
    0: "default",
    1: "enable_cache",
    2: "skip_tests",
    3: "parallel_build"
}

def choose_action():
    # sementara random dulu (nanti bisa diganti model RL PPO/DQN)
    return random.choice(list(actions.keys()))

def main():
    # agent pilih aksi
    action = choose_action()
    action_name = actions[action]

    print(f"[RL Agent] Chosen action: {action_name}")

    # Simulasi efek aksi
    start_time = time.time()

    if action_name == "default":
        build_time = 20
        test_time = 10
        success = 1
    elif action_name == "enable_cache":
        build_time = 10
        test_time = 10
        success = 1
    elif action_name == "skip_tests":
        build_time = 15
        test_time = 2
        success = random.choice([1, 0])  # kadang gagal karena test diskip
    elif action_name == "parallel_build":
        build_time = 8
        test_time = 12
        success = 1
    else:
        build_time, test_time, success = 20, 10, 1

    # simulasi runtime
    time.sleep(1)  # supaya kelihatan ada proses
    duration = time.time() - start_time + build_time + test_time

    # log hasil ke file json (bisa dipakai untuk training RL)
    result = {
        "action": action_name,
        "duration": duration,
        "success": success
    }

    os.makedirs("logs", exist_ok=True)
    logfile = "logs/ci_metrics.json"

    if os.path.exists(logfile):
        with open(logfile, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(result)

    with open(logfile, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[RL Agent] Logged result: {result}")


if __name__ == "__main__":
    main()
