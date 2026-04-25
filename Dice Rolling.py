import random
import time
import sys
def roll_single_die():
    return random.randint(1, 6)
def roll_dice_pair():
    return roll_single_die(), roll_single_die()
def animate_rolling():
    frames = ["🎲 ⚀", "🎲 ⚁", "🎲 ⚂", "🎲 ⚃", "🎲 ⚄", "🎲 ⚅"]
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(0.05)
    print("\r", end="")
def display_dice_art(value):
    dice_art = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"]
    }
    return dice_art[value]
def print_side_by_side(die1, die2):
    art1 = display_dice_art(die1)
    art2 = display_dice_art(die2)
    print("\n")
    for line1, line2 in zip(art1, art2):
        print(f"  {line1}        {line2}")
    print("\n")
def get_user_choice():
    while True:
        choice = input("\n🎲 Roll again? (y / n / stats / exit): ").strip().lower()
        if choice in ['y', 'n', 'stats', 'exit']:
            return choice
        print("❌ Invalid input. Please enter 'y', 'n', 'stats', or 'exit'.")
def display_statistics(history):
    if not history:
        print("\n📊 No rolls recorded yet.")
        return
    total_rolls = len(history)
    totals = [sum(roll) for roll in history]
    avg_total = sum(totals) / total_rolls
    most_common_total = max(set(totals), key=totals.count)
    doubles = sum(1 for d1, d2 in history if d1 == d2)
    seven_count = totals.count(7)
    print("\n" + "=" * 50)
    print("📊 SESSION STATISTICS")
    print("=" * 50)
    print(f"🎲 Total rolls: {total_rolls}")
    print(f"📈 Average total: {avg_total:.2f}")
    print(f"⭐ Most frequent total: {most_common_total}")
    print(f"🔄 Doubles rolled: {doubles} times ({doubles/total_rolls*100:.1f}%)")
    print(f"🎯 Sevens rolled: {seven_count} times ({seven_count/total_rolls*100:.1f}%)")
    print("\n📊 Total Distribution:")
    for total in range(2, 13):
        count = totals.count(total)
        bar_length = int(count / total_rolls * 30)
        bar = "█" * bar_length + "░" * (30 - bar_length)
        print(f"  {total:2}: {bar} {count} ({count/total_rolls*100:.1f}%)")
    print("=" * 50)
def main():
    print("\n" + "=" * 50)
    print("🎲 WELCOME TO ADVANCED DICE ROLLING GAME 🎲")
    print("=" * 50)
    print("Instructions:")
    print("  • Press 'y' to roll again")
    print("  • Press 'n' to quit")
    print("  • Press 'stats' to view session statistics")
    print("  • Press 'exit' to quit immediately")
    print("=" * 50)
    roll_history = []
    roll_count = 0
    while True:
        input("\n⚡ Press ENTER to roll the dice...")
        print("\n🎲 Rolling dice", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        animate_rolling()
        die1, die2 = roll_dice_pair()
        roll_count += 1
        roll_history.append((die1, die2))
        total = die1 + die2
        print_side_by_side(die1, die2)
        print(f"📊 Roll #{roll_count}: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")
        if die1 == die2:
            print("🎉 DOUBLE! 🎉")
        elif total == 7:
            print("✨ LUCKY 7! ✨")
        elif total == 2:
            print("💀 SNAKE EYES! 💀")
        elif total == 12:
            print("🎯 BOX CARS! 🎯")
        if total >= 10:
            print("🔥 HIGH ROLLER! 🔥")
        elif total <= 4:
            print("🍀 BETTER LUCK NEXT TIME 🍀")
        choice = get_user_choice()
        if choice == 'stats':
            display_statistics(roll_history)
            continue
        elif choice == 'n' or choice == 'exit':
            print("\n" + "=" * 50)
            print(f"📊 Final Statistics for {roll_count} roll(s):")
            display_statistics(roll_history)
            print("\n👋 Thanks for playing! Goodbye!")
            print("=" * 50)
            break
        elif choice == 'y':
            continue
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)