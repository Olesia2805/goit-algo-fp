import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sums_count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    total_rolls = num_rolls
    probabilities = {key: value / total_rolls for key, value in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('The sum of the numbers on the dice')
    plt.ylabel('Probability')
    plt.title('The probability of the sum of the numbers on two dice')
    
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":

    for accuracy in [100, 1000, 10000, 100000]:

        probabilities = simulate_dice_rolls(accuracy)

        sum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        analytical = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

        programmatic = []

        for val in probabilities.values():
            val = 100 * val
            val = round(val, 2)
            programmatic.append(val)
    
        plot_probabilities(probabilities)

        print (f"|{'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} |")
        print (f"|{'Sum':<15} | {'Analytical(%)':<15} | {'Programmatic(%)':<15} | {'Difference':<15} |")
        print (f"|{'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} |")
        for i in range(len(sum)):
            difference = programmatic[i] - analytical[i]
            print(f"|{sum[i]:<15} | {analytical[i]:<15} | {programmatic[i]:<15} | {difference:<15.2f} |")

        print (f"|{'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} |")