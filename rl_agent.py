import random, time, json, os

actions = ["default", "enable_cache", "skip_tests", "parallel_build"]

def main():
    action = random.choice(actions)
    print(f"[RL Agent] Action chosen: {action}")

    duration = random.randint(10, 50)
    success = random.choice([0, 1])

    result = {"action": action, "duration": duration, "success": success}
    os.makedirs("logs", exist_ok=True)

    logfile = "logs/ci_metrics.json"
    data = []
    if os.path.exists(logfile):
        with open(logfile) as f: data = json.load(f)
    data.append(result)

    with open(logfile, "w") as f: json.dump(data, f, indent=2)

    print(f"[RL Agent] Logged: {result}")

if __name__ == "__main__":
    main()
