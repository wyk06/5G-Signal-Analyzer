# 二本通信狗逆袭之作：5G信号强度分析  
import numpy as np  
import matplotlib.pyplot as plt  

def plot_signal():  
    # 伪造基站信号数据（必须学会！）  
    x = np.linspace(0, 10, 100)  
    y = np.sin(x) + np.random.normal(0, 0.1, 100)  

    plt.plot(x, y)  
    plt.title("5G Signal Strength (by 二本逆袭狗)")  
    plt.savefig("signal.png")  
