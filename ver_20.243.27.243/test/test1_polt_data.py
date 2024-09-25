import matplotlib.pyplot as plt
from typing import List
from matplotlib.ticker import MaxNLocator, FixedFormatter
import os


def plot_speed_and_power(speed: List[int], power: List[int], filename: str = None):
    """
    Plots speed and power data in two side-by-side subplots and optionally saves the plot to a file.

    Args:
        speed (List[int]): A list of speed values to plot.
        power (List[int]): A list of power values to plot.
        filename (str, optional): The filename to save the plot. Defaults to None.
    """
    fig, axs = plt.subplots(1, 2, figsize=(13.45, 3.0), dpi=100)

    # Common x-axis configuration
    x_ticks = [0.5 * i for i in range(11)] 
    x_tick_labels = [int(x) if x.is_integer() else x for x in x_ticks]
    print("x_tick_labels: ", x_tick_labels) # [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

    # Plot speed data
    axs[0].plot(speed, linestyle='-', color='#5C8ACC')
    axs[0].fill_between(range(len(speed)), speed, color='#EAEEFF', alpha=0.5)
    axs[0].spines['top'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    axs[0].spines['left'].set_visible(False)
    axs[0].spines['bottom'].set_visible(False)
    axs[0].tick_params(axis='both', which='both', length=0, labelcolor='#B1B4B7')
    axs[0].grid(False)
    axs[0].xaxis.set_tick_params(pad=-2)  # 調整 x 軸刻度標籤位置
    axs[0].yaxis.set_tick_params(pad=-10)   # 調整 y 軸刻度標籤位置

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
    axs[1].xaxis.set_tick_params(pad=2)  # 調整 x 軸刻度標籤位置
    axs[1].yaxis.set_tick_params(pad=-10)  # 調整 y 軸刻度標籤位置

    axs[1].set_xticks(range(0, 50, 5))
    axs[1].set_xticklabels(x_tick_labels[:10])

    # 移動 x 軸刻度標籤
    # plt.subplots_adjust(left=0, right=1, bottom=0.2, top=0.8)

    plt.tight_layout()

    # Remove axis and margins
    # plt.axis('off')
    fig = plt.gcf()
    fig.set_size_inches(13.45, 3.0)  # dpi = 300, output = 700*700 pixels
    # plt.gca().xaxis.set_major_locator(plt.NullLocator()) # 移除 x 軸的刻度標記
    # plt.gca().yaxis.set_major_locator(plt.NullLocator())  # 移除 y 軸的刻度標記
    # plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0) # 調整子圖邊界，確保圖形填滿整個圖像區域
    plt.margins(0, 0) # 移除邊緣空白區域

    if filename:
        # 建立 imgs 目錄（如果不存在）
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename, format='png')

    plt.show()


if __name__ == '__main__':
    speed = [327, 209, 267, 85, 296, 136, 211, 334, 326, 123, 133, 68, 345, 341, 136, 65, 136, 179, 321, 183, 212, 333, 228, 322, 216, 333, 86, 203, 157, 44, 319, 101, 216, 174, 81, 108, 296, 215, 174, 223, 157, 76, 291, 183, 230, 140, 298, 18, 298, 85]
    power = [69, 18, 7, 82, 15, 33, 97, 77, 21, 51, 32, 13, 66, 42, 8, 22, 85, 4, 54, 81, 38, 47, 95, 11, 86, 29, 91, 86, 79, 73, 34, 30, 17, 13, 87, 16, 36, 90, 25, 15, 20, 73, 7, 21, 84, 41, 4, 10, 71, 78] 
    print("Speed:", speed, " len(speed): ", len(speed))
    print("Power:", power, "len(power): ", len(power))

    plot_speed_and_power(speed, power, filename=f"imgs/plot_test.png")

