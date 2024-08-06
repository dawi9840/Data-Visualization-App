import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
from client import get_rest_data
from matplotlib.ticker import MultipleLocator, MaxNLocator
import json
import os
import time
from datetime import datetime

def extract_speed_and_power(data: Dict[str, str]) -> Tuple[List[int], List[int]]:
    """
    Extracts the 'speed' and 'power' values from the given data dictionary.

    Args:
        data (Dict[str, str]): A dictionary containing at least 'speed' and 'power' keys
                               with string representations of lists.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists: 'speed' and 'power'.
                                     Returns (None, None) if an error occurs.
    """
    try:
        speed = json.loads(data['speed'].replace("'", '"'))
        power = json.loads(data['power'].replace("'", '"'))
        return speed, power
    except KeyError as e:
        print(f"KeyError: {e} not found in the data")
        return None, None
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e} while parsing the lists")
        return None, None

def plot_speed_and_power(speed: List[int], power: List[int], filename: str = None):
    """
    Plots speed and power data in two side-by-side subplots and optionally saves the plot to a file.

    Args:
        speed (List[int]): A list of speed values to plot.
        power (List[int]): A list of power values to plot.
        filename (str, optional): The filename to save the plot. Defaults to None.
    """
    fig, axs = plt.subplots(1, 2, figsize=(13.45, 3.0), dpi=100)

    request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 記錄並格式化當前的時間

    # Common x-axis configuration
    x_ticks = [0.5 * i for i in range(11)] 
    x_tick_labels = [int(x) if x.is_integer() else x for x in x_ticks]
    # print("x_tick_labels: ", x_tick_labels) # [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

    # Plot speed data
    axs[0].plot(speed, linestyle='-', color='#5C8ACC')
    axs[0].fill_between(range(len(speed)), speed, color='#EAEEFF', alpha=0.5)
    axs[0].spines['top'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    axs[0].spines['left'].set_visible(False)
    axs[0].spines['bottom'].set_visible(False)
    axs[0].tick_params(axis='both', which='both', length=0, labelcolor='#B1B4B7')
    axs[0].grid(False)
    # axs[0].xaxis.set_tick_params(pad=-2)  # 調整 x 軸刻度標籤位置
    # axs[0].yaxis.set_tick_params(pad=3)  # 調整 y 軸刻度標籤位置
    # axs[0].xaxis.set_major_locator(MaxNLocator(integer=True)) # 確保 x 軸刻度是整數
    # axs[0].xaxis.set_major_locator(plt.MaxNLocator(nbins='auto', integer=True)) # 自動調整刻度數量
    # -----------------------------------------------------------------------------------------------
    # new version
    axs[0].xaxis.set_tick_params(pad=2)   # 調整 x 軸刻度標籤位置
    axs[0].yaxis.set_tick_params(pad=-10) # 調整 y 軸刻度標籤位置
    axs[0].set_xticks(range(0, 50, 5))
    axs[0].set_xticklabels(x_tick_labels[:10])

    
    # Plot power data
    axs[1].plot(power, linestyle='-', color='#9D5ABD')
    axs[1].fill_between(range(len(power)), power, color='#F6E8FE', alpha=0.5)
    axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    axs[1].spines['left'].set_visible(False)
    axs[1].spines['bottom'].set_visible(False)
    axs[1].tick_params(axis='both', which='both', length=0, labelcolor='#B1B4B7')
    axs[1].grid(False)
    # axs[1].xaxis.set_tick_params(pad=2)  # 調整 x 軸刻度標籤位置
    # axs[1].yaxis.set_tick_params(pad=-10)  # 調整 y 軸刻度標籤位置
    # axs[1].xaxis.set_major_locator(MaxNLocator(integer=True)) # 確保 x 軸刻度是整數
    # axs[1].xaxis.set_major_locator(plt.MaxNLocator(nbins='auto', integer=True)) # 自動調整刻度數量
    # -----------------------------------------------------------------------------------------------
    # new version
    axs[1].xaxis.set_tick_params(pad=2)   # 調整 x 軸刻度標籤位置
    axs[1].yaxis.set_tick_params(pad=-10) # 調整 y 軸刻度標籤位置
    axs[1].set_xticks(range(0, 50, 5))
    axs[1].set_xticklabels(x_tick_labels[:10])


    plt.tight_layout()
    
    if filename:
        # 建立 imgs 目錄（如果不存在）
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # plt.savefig(filename, format='png')
        plt.savefig(filename, format='png', bbox_inches='tight', pad_inches=0)  # 調整邊界和填充
    
    plt.show()

def save_plot_speed_and_power(count:int):
    user_url:str = "http://20.78.3.60:8080/users"
    user_data: List[Dict[str, int]] = get_rest_data(user_url)
    print("len(user): ", len(user_data))
    print('---'*20, "\n")

    if(count <= len(user_data)):
        for i in range(len(user_data) - count, len(user_data)): # 計算倒數 count 張圖片
            print(f"Index[{i}]:\n{user_data[i]}\n")
            speed, power = extract_speed_and_power(user_data[i])
            plot_speed_and_power(speed, power, filename=f"imgs/plot_{i+1}.png")
    else:
        for i in range(0, len(user_data)): 
            print(f"Index[{i}]:\n{user_data[i]}\n")
            speed, power = extract_speed_and_power(user_data[i])
            plot_speed_and_power(speed, power, filename=f"imgs/plot_{i+1}.png")

def update_polt(count:int=100, update_time:int=30):
    while True:
        save_plot_speed_and_power(count)
        time.sleep(update_time)  # 每 update_time 秒重新抓取數據並刷新圖表

def plot_data(data: List[int], line_color: str = '#5B8BD3', fill_color: str = '#EAEEFE'):
    """
    Plots a line chart for the given speed data and fills the area under the curve.

    Args:
        speed (List[int]): A list of speed values to plot.
        line_color (str): Color for the line. Default is a custom color.
        fill_color (str): Color for the filled area under the line. Default is light blue.
    """
    # 設定 x 軸為時間長度
    x = list(range(len(data)))

    # 繪製折線圖
    plt.figure(figsize=(10, 5))
    plt.plot(x, data, linestyle='-', color=line_color, label='Speed')
    
    # 填充折線圖下方的區域
    plt.fill_between(x, data, color=fill_color, alpha=0.5)

    # 隱藏外圍框線
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # 隱藏刻度線，只顯示數字
    ax.tick_params(axis='both', which='both', length=0)

    plt.grid(False)
    plt.show()

def test_plot_speed_and_power():
    user_url:str = "http://20.78.3.60:8080/users"
    user_data: List[Dict[str, int]] = get_rest_data(user_url)

    print("len(user): ", len(user_data))
    # 提取 'speed' 和 'power' 的值
    speed, power = extract_speed_and_power(user_data[19])
    print("Speed:", speed, " len(speed): ", len(speed))
    print("Power:", power, "len(power): ", len(power))

    # plot_data(speed, '#5C8ACC', '#EAEEFF')
    # plot_data(power, '#9D5ABD','#F6E8FE')
    plot_speed_and_power(speed, power, filename=f"imgs/plot_test.png")

if __name__ == '__main__':
    # save_plot_speed_and_power(1)
    # update_polt(5, 5)
    test_plot_speed_and_power()
