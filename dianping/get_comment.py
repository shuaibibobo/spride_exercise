
import time,random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + a * t
        v = v0 + a * t
        # 移动距离 x = v0*t + 1/2 * a * t^2
        move = v0 * t + 0.5 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track


def _handle_ban():
    try:
        driver = webdriver.Chrome()
        driver.get('http://www.dianping.com/shop/G85MfSgR7HCkqHMx/review_all/p2')
        time.sleep(3)
        button = driver.find_element_by_id('yodaBox')
        ActionChains(driver).move_to_element(button).perform()
        move_x_offset = driver.find_element_by_id('yodaBoxWrapper').size['width']
        print("move_x_offset")
        time.sleep(3)
        track=get_track(move_x_offset)
        print(track)
        ActionChains(driver).click_and_hold(button).perform()
        for x in track:
            print(x)
            ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()

        time.sleep(1)
        driver.get('http://www.dianping.com/shop/G85MfSgR7HCkqHMx/review_all/p2')
        print(driver.title)
    except:
        pass
if __name__ == "__main__":
    # s=get_track(232)
    #
    # print(s)
    _handle_ban()
