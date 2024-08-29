import os
import sys
# 將上一層資料夾的路徑加入 sys.path，這樣 Python 就能找到並匯入上一層資料夾中的 BB.py 檔案中的函數。
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Dict
import matplotlib.pyplot as plt
from datetime import datetime
import time
import pytz
from flask import Flask, render_template, send_file, jsonify, url_for
from client import get_rest_data
from data_visual_util import extract_speed_and_power
from shutil import move

import matplotlib
matplotlib.use('Agg')

html_file:str = 'vue_index_v3.html'

app = Flask(__name__)

# 全局變量來存儲上一次的數據和時間
last_user_data: List[Dict[str, int]] = []
last_request_times: List[str] = []

# static_img_dir = os.path.join(app.static_folder, 'imgs') # 在應用程式啟動時建立目錄
# if not os.path.exists(static_img_dir):
#     os.makedirs(static_img_dir)
#     print(f"Created directory: {static_img_dir}")

def get_utc_2_taipei_time_zone(time_formate: str) -> str:
    """
    Converts the current UTC time to Taipei time zone and formats it.

    Args:
        time_format (str): A format string for datetime, e.g., '%Y-%m-%d %H:%M' or '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: The formatted date and time string in Taipei time zone.
    """
    utc_time = datetime.now(pytz.utc)                               # 設定 UTC 時區
    taipei_time = utc_time.astimezone(pytz.timezone('Asia/Taipei')) # 將 UTC 時間轉換為 Asia/Taipei 時區
    return taipei_time.strftime(time_formate)                       

def create_plot(speed: List[int], power: List[int], request_time: str, filename: str = None):
    """
    創建並保存圖片，使用固定的檔案名稱。
    
    :param speed: 速度數據列表
    :param power: 功率數據列表
    :param index: 圖片索引 (1, 2, or 3)
    """
    try:
        print(f"Creating plot {filename}...")

        fig, axs = plt.subplots(1, 2, figsize=(13.40, 3.0), dpi=100)
        # request_time = get_utc_2_taipei_time_zone('%Y-%m-%d %H:%M:%S')

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
        # -----------------------------------------------------------------------------------------------
        axs[0].xaxis.set_tick_params(pad=2)   # 調整 x 軸刻度標籤位置
        axs[0].yaxis.set_tick_params(pad=-10) # 調整 y 軸刻度標籤位置
        axs[0].set_xticks(range(0, 50, 5))
        axs[0].set_xticklabels(x_tick_labels[:10])

        # 顯示請求時間在子圖左上角 # 0.05, 0.99
        axs[0].text(-0.02, 1.10, f"{request_time}", transform=axs[0].transAxes, fontsize=8, color='black', ha='left', va='top')

        # Plot power data
        axs[1].plot(power, linestyle='-', color='#9D5ABD')
        axs[1].fill_between(range(len(power)), power, color='#F6E8FE', alpha=0.5)
        axs[1].spines['top'].set_visible(False)
        axs[1].spines['right'].set_visible(False)
        axs[1].spines['left'].set_visible(False)
        axs[1].spines['bottom'].set_visible(False)
        axs[1].tick_params(axis='both', which='both', length=0, labelcolor='#B1B4B7')
        axs[1].grid(False)
        # -----------------------------------------------------------------------------------------------
        axs[1].xaxis.set_tick_params(pad=2)   # 調整 x 軸刻度標籤位置
        axs[1].yaxis.set_tick_params(pad=4)   # 調整 y 軸刻度標籤位置
        axs[1].set_xticks(range(0, 50, 5))
        axs[1].set_xticklabels(x_tick_labels[:10])

        # Remove the last y-axis tick label on axs[1]
        yticks = axs[1].yaxis.get_major_ticks()
        if yticks:
            yticks[-1].label1.set_visible(False)

        # 顯示請求時間在子圖左上角 # 0.05, 0.99
        axs[1].text(-0.05, 1.10, f"{request_time}", transform=axs[1].transAxes, fontsize=8, color='black', ha='left', va='top') 

        plt.tight_layout() # 調整佈局

        # Remove axis and margins
        fig = plt.gcf()
        fig.set_size_inches(13.45/1.26, 3.0/1.8)
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0.1)  # 調整子圖邊界和子圖之間的間距，wspace 增加以調整右邊子圖的位置
        plt.margins(0, 0) # 移除邊緣空白區域

        full_path = os.path.join(app.static_folder, 'imgs', filename) # 確保目錄存在
        print(f"Saving plot to: {full_path}")
        plt.savefig(full_path, format='png', bbox_inches='tight', pad_inches=0)  # 保存圖片, and調整邊界和填充

        plt.close(fig)    # 確保關閉圖形以釋放記憶體，關閉當前圖形
        plt.close('all')  # 關閉所有圖形

        if os.path.exists(full_path):  # 打印確認信息
            print(f"Image saved successfully: {full_path}")
        else:
            print(f"Failed to save image: {full_path}")

    except Exception as e:
        print(f"Error in create_plot: {str(e)}")

@app.route('/')
def index():
    plot()                  # 調用 plot 函數生成圖片
    return render_template(html_file)

@app.route('/plot')
def plot():
    global last_user_data, last_request_times
    user_data: List[Dict[str, int]] = get_rest_data("http://20.78.3.60:8080/users")
    current_time = get_utc_2_taipei_time_zone('%Y-%m-%d %H:%M:%S')

    try:
        for i in range(min(3, len(user_data))): # 遍歷 user_data 中最多前三個使用者資料
            speed, power = extract_speed_and_power(user_data[i])
            
            if i >= len(last_request_times): # 如果 last_request_times 的長度小於當前使用者索引，則新增當前時間
                last_request_times.append(current_time)
            
            create_plot(speed, power, last_request_times[i], filename=f"plot_{i+1}.png")

    finally:
        plt.close('all')  # 確保關閉所有圖形

    last_user_data = user_data[:3] # 更新全局變量，僅保存前三個使用者的資料

    return render_template(html_file)  # 渲染 HTML 模板並返回

@app.route('/image/<filename>')
def image(filename):
    return send_file(os.path.join('static/imgs', filename))

@app.route('/update_plots')
def update_plots():
    global last_user_data, last_request_times
    
    user_data: List[Dict[str, int]] = get_rest_data("http://20.78.3.60:8080/users")
    current_time = get_utc_2_taipei_time_zone('%Y-%m-%d %H:%M:%S')
    
    data_changed = False
    
    try:
        # 檢查數據是否有變化
        if len(user_data) > 0 and (len(last_user_data) == 0 or extract_speed_and_power(user_data[0]) != extract_speed_and_power(last_user_data[0])):
            data_changed = True

        if data_changed:
            # 移動現有的圖片
            for i in range(2, 0, -1):
                old_file = os.path.join(app.static_folder, 'imgs', f'plot_{i}.png')
                new_file = os.path.join(app.static_folder, 'imgs', f'plot_{i+1}.png')
                if os.path.exists(old_file):
                    move(old_file, new_file)

            # 更新時間列表
            if len(last_request_times) >= 3:
                last_request_times = [current_time] + last_request_times[:2]
            else:
                last_request_times = [current_time] + last_request_times

            # 創建新的圖片
            if len(user_data) > 0:
                speed, power = extract_speed_and_power(user_data[0])
                create_plot(speed, power, current_time, filename="plot_1.png")

            # 更新 last_user_data
            last_user_data = user_data[:3]
        
    finally:
        plt.close('all')  # 確保關閉所有圖形
    
    timestamp = int(time.time())
    
    return jsonify({
        'plot_3': url_for('static', filename='imgs/plot_3.png') + f'?t={timestamp}',
        'plot_2': url_for('static', filename='imgs/plot_2.png') + f'?t={timestamp}',
        'plot_1': url_for('static', filename='imgs/plot_1.png') + f'?t={timestamp}',
        'data_changed': data_changed
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)