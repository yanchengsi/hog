"""The Game of Hog."""

from dice import six_sided, make_test_dice
import random
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    total=0
    sow_sad = False
    for _ in range (num_rolls) :
        roll =dice()
        if roll == 1 :
            sow_sad= True
        total += roll
    return 1 if sow_sad  else  total
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # Get the tens digit of the opponent's score
    opponent_tens = opponent_score // 10 %  10
    # Get the ones digit of the player's score
    player_ones = player_score % 10  
    # Calculate the absolute difference
    difference = abs(opponent_tens - player_ones)  
    
    # Calculate the score
    score = max(3 * difference, 1)  
    
    return score
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    def num_factors(n):  
        """  
        计算正整数n的因子数量  
        
        Args:  
            n (int): 要计算因子的正整数  
        
        Returns:  
            int: n的因子总数  
        """  
        # Initialize the factor counter
        factors = 0  
            
        # Iterate through all possible factors from 1 to n
        for i in range(1, n + 1):  
                # If i can divide n, count it as a factor
                if n % i == 0:  
                    factors += 1  
            
        return factors
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # Initialize scores
    score0 = 0  
    score1 = 0  
    who = 0  # Starting player  

    while score0 < goal and score1 < goal:  
        if who == 0:  
            # Player 0's turn
            dice_num = strategy0(score0, score1)  
            score0 = update(dice_num, score0, score1, dice)  
        else:  
            # Player 1's turn
            dice_num = strategy1(score1, score0)  
            score1 = update(dice_num, score1, score0, dice)  

        # Switch player
        who = 1 - who  

    # Return final scores
    return score0, score1
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def always_roll(n):  
        """Return a strategy function that always returns n. This means n dice will be rolled each turn."""  
        def strategy(player_score, opponent_score):  
            return n  
        return strategy  

    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    first_roll = strategy(0, 0)  # Start with 0 points and 0 points
    for player_score in range(goal):  
        for opponent_score in range(goal):  
            if strategy(player_score, opponent_score) != first_roll:  
                return False  # If any combination returns a different result, return False
    return True  # If all combinations return the same result, return True

# Example strategies
def always_roll_5(player_score, opponent_score):  
    return 5  

def always_roll_3(player_score, opponent_score):  
    return 3  

def mixed_strategy(player_score, opponent_score):  
    if player_score < 50:  
        return 5  
    else:  
        return 3  

# Test
goal = 100  
print(is_always_roll(always_roll_5, goal))      # Output: True  
print(is_always_roll(always_roll_3, goal))      # Output: True  
print(is_always_roll(mixed_strategy, goal))      # Output: False
    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def make_averaged(original_function, times_called=40):  
        """Return a function that calls original_function times_called times with given arguments and returns the average result."""  
        def averaged_function(*args):  
            total = 0  
            for _ in range(times_called):  
                total += original_function(*args)  # 使用 *args 将参数传递给 original_function  
            return total / times_called  # 返回平均值  
        return averaged_function
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    import random  

def make_averaged(original_function, num_samples=10000):  
    """返回一个可以计算平均值的函数，该函数在 num_samples 次调用后返回平均值。"""  
    def averaged_function(*args):  
        total = 0  
        for _ in range(num_samples):  
            total += original_function(*args)  
        return total / num_samples  
    return averaged_function  

def roll_dice(num_rolls, dice):  
    """Roll dice num_rolls times and return the total score."""  
    total = 0  
    for _ in range(num_rolls):  
        total += dice()  # 调用骰子获取点数  
    return total  

def max_scoring_num_rolls(dice):  
    """  
    Run experiments to determine the number of dice rolls (from 1 to 10) that gives the maximum average score.
    
    Args:  
    dice: Dice function that generates random dice outcomes  

    Returns:  
    The number of dice rolls (1-10) that gives the maximum average score  
    """  
    # 使用 make_averaged 创建一个计算平均值的函数  
    averaged_roll = make_averaged(roll_dice)  

    # 初始化最大分数和对应的掷骰子数量  
    max_score = float('-inf')  
    max_num_rolls = 1  

    # 遍历 1 到 10 的掷骰子数量  
    for num_rolls in range(1, 11):  
        # 计算当前数量的平均得分  
        current_score = averaged_roll(num_rolls, dice)  

        # 更新最大分数和数量，处理并列情况  
        if current_score > max_score or (current_score == max_score and num_rolls < max_num_rolls):  
            max_score = current_score  
            max_num_rolls = num_rolls  

    return max_num_rolls  

# 示例骰子函数  
def six_sided():  
    """Return a random outcome from a six-sided dice"""  
    return random.randint(1, 6)  

# 测试 max_scoring_num_rolls 函数  
best_rolls = max_scoring_num_rolls(six_sided)  
print(f"最佳掷骰子次数: {best_rolls}")
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2
def sus_points(score):  
    """  
    根据 Sus Fuss 规则计算新的分数  
    
    Args:  
        score (int): 当前分数  
    
    Returns:  
        int: 根据 Sus Fuss 规则计算后的新分数  
    """  
    # 如果分数是质数，则翻倍  
    if is_prime(score):  
        return score * 2  
    
    # 如果分数是质数的因子数，则加上因子数  
    if is_prime(num_factors(score)):  
        return score + num_factors(score)  
    
    return score  

def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):  
    """  
    Sus Fuss 策略函数  
    
    参数:  
    - score: 当前玩家分数  
    - opponent_score: 对手分数  
    - threshold: 需要增加的最小分数  
    - num_rolls: 默认掷骰子次数  
    
    返回:   
    要滚动的骰子数（0 或 num_rolls）  
    """  
    # 计算如果滚动 0 的新分数  
    score_if_rolling_0 = sus_points(score)  
    
    # 计算分数增量  
    score_increase = score_if_rolling_0 - score  
    
    # 判断是否满足阈值  
    if score_increase >= threshold:  
        return 0  # 选择滚动 0 次  
    else:  
        return num_rolls  # 使用默认掷骰子次数
def final_strategy(score, opponent_score):  
    """  
    最终策略：综合考虑多个因素的骰子滚动策略  
    
    策略考虑因素：  
    1. 分数差距  
    2. 接近胜利的程度  
    3. Boar Brawl 和 Sus Fuss 规则  
    4. 风险管理  
    """  
    # 定义常量  
    GOAL = 100  # 游戏目标分数  
    
    # 计算分数差距  
    score_difference = opponent_score - score  
    
    # 距离胜利的距离  
    distance_to_goal = GOAL - score  
    
    # 1. 如果非常接近获胜（20分内），采取风险较高的策略  
    if distance_to_goal <= 20:  
        # 尝试快速获胜  
        if boar_brawl(score, opponent_score) >= 10:  
            return 0  # 利用 Boar Brawl  
        return 8  # 高风险策略  
    
    # 2. 落后较多时，采取激进策略  
    if score_difference > 15:  
        return 6  # 中等风险策略  
    
    # 3. 利用 Sus Fuss 规则  
    if sus_points(score) - score >= 10:  
        return 0  # 利用 Sus Fuss  
    
    # 4. 正常情况下的策略  
    if score < 50:  
        # 早期阶段，保守策略  
        return 4  
    elif 50 <= score < 75:  
        # 中期阶段，平衡策略  
        return 5  
    else:  
        # 后期阶段，稍微激进  
        return 6  

# 辅助函数（如果未定义）  
def boar_brawl(player_score, opponent_score):  
    """Boar Brawl 规则得分计算"""  
    opponent_tens = opponent_score // 10 % 10  
    player_ones = player_score % 10  
    difference = abs(opponent_tens - player_ones)  
    return max(3 * difference, 1)  

def sus_points(score):  
    """Sus Fuss 规则得分计算"""  
    if is_prime(score):  
        return score * 2  
    if is_prime(num_factors(score)):  
        return score + num_factors(score)  
    return score  

def is_prime(n):  
    """判断是否为质数"""  
    if n < 2:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

def num_factors(n):  
    """计算数字的因子数"""  
    factors = 0  
    for i in range(1, n + 1):  
        if n % i == 0:  
            factors += 1  
    return factors

def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10

    """
    # BEGIN PROBLEM 10
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10

def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    "This strategy returns 0 dice when your score would increase by at least threshold."
    # BEGIN PROBLEM 11
    def boar_brawl(player_score, opponent_score):  
    "计算 Boar Brawl 规则下的得分。"
    # 假设的规则：玩家得分加上 4  
    return player_score + 4  # 示例逻辑  

def sus_update(score):  
    "根据 Sus Fuss 规则更新得分。"
    # 假设的规则：如果 score 达到一定条件，增加 5 分  
    if score % 7 == 0:  # 示例逻辑: 如果 score 是 7 的倍数  
        return score + 5  
    return score  

def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):  
    '结合 Boar Brawl 和 Sus Fuss 的策略函数。'
    
    参数:  
    - score: 当前玩家分数  
    - opponent_score: 对手分数  
    - threshold: 触发零滚动的最小分数增量  
    - num_rolls: 默认掷骰子次数  
    
    返回:   
return num_rolls  # Remove this line once implemented.
# END PROBLEM 11



def final_strategy(score, opponent_score):
    """
    # Write a brief description of your final strategy.

    "This strategy is a placeholder and always returns 6 dice rolls."
    
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    'Read in the command-line argument and calls corresponding functions.'
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()