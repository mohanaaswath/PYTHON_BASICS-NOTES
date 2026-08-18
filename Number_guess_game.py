target = 99
for i in range(1,7):
                T = int(input("Enter a number: "))
                if T == target:
                        print("You won the game\n")
                        print("The End")
                        break
                elif T > target:
                        print("Target is less than input\n")
                elif T < target:
                        print("Target is greater than input\n")
                else:
                        print("play again")
                        break;
if (T == target):
        print(f"You guessed it in {i} attempts")