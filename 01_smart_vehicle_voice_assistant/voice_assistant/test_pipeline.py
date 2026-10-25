# test_pipeline.py

from modules.llama_brain import ask_brain
from modules.tools import run_tool


def test_input(text, state):
    print("\n========================================")
    print("🔵 User:", text)

    # Step 1 — Brain decides what to do
    brain = ask_brain(text, state)
    print("🧠 Brain output:", brain)

    # Step 2 — Apply any state changes
    state_changes = brain.get("state_changes", {})
    for key, value in state_changes.items():
        state[key] = value

    tool = brain.get("tool", "none")
    args = brain.get("args", {})

    # Step 3 — If brain says no tool → answer directly
    if tool == "none":
        print("AI Response:", brain.get("response"))
        return

    # Step 4 — Run the tool
    print("🛠 Calling tool:", tool)
    tool_result = run_tool(tool, args, state)
    print("🛠 Tool result:", tool_result)


def main():
    # Shared assistant state
    state = {
        "driving_mode": False,
        "current_destination": None
    }

    # Test commands (you can add more)
    test_commands = [
        "hello",
        "activate driving mode",
        "navigate to monastir train station",
        "where am i",
        "turn on the light",
        "turn off the light",
        "check speed",
        "check temperature",
        "is there any accident ahead",
        "deactivate driving mode",
        "exit"
    ]

    print("=== Starting Pipeline Simulation ===")
    for command in test_commands:
        test_input(command, state)
    print("\n=== Simulation Finished ===")


if __name__ == "__main__":
    main()
