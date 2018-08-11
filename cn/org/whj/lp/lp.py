import numpy as np
import pandas as pd
import time

np.random.seed(2)  # 产生伪随机数列

N_STATES = 6  # 距离宝藏的距离
ACTIONS = ['left', 'right']  # 可移动的方向
EPSILON = 0.9  # 选择动作90%选择最优动作
ALPHA = 0.1  # 选择动作10%随机选择
LAMBDA = 0.9  # 未来奖励--衰减值
MAX_EPISODES = 13  # 训练次数
FRESH_TIME = 0.1  # 移动时间频率


def build_q_table(n_status, actions):
    table = pd.DataFrame(
        np.zeros((n_status, len(actions))),  # q_table initial values
        columns=actions,  # actions`s name
    )
    # print(table)  # show table
    return table

    # build_q_table(N_STATES, ACTIONS)


def choose_action(state, q_table):
    # This is how to choose an action : 选择动作，根据所在的状态和q_table里面的值进行选择左右移动
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()
    return action_name


def get_env_feedback(S, A):
    # This is how agent will interact with the environment : 获取下一个动作和奖励
    if A == 'right':  # move right
        if S == N_STATES - 2:  # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:  # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # this is how environment be updated : 让方块在一维空间左右移动
    env_list = ['-'] * (N_STATES - 1) + ['🕳️']  # '-------ok' our environment
    if S == 'terminal':
        interaction = '第 %s 次训练 ！ total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r              ', end='')
    else:
        env_list[S] = '🐍'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    # main part of RL loop
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminal = False
        update_env(S, episode, step_counter)
        while not is_terminal:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.iloc[S_, :].max()
            else:
                q_target = R
                is_terminal = True

            q_table.ix[S, A] += ALPHA * (q_target - q_predict)
            S = S_

            update_env(S, episode, step_counter + 1)
            step_counter += 1
    return q_table


if __name__ == '__main__':
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
