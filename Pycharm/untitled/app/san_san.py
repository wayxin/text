from time import sleep
import unittest
from appium import webdriver
class ce(unittest.TestCase):
    d = {
                  "device": "android",
                  "platformName": "Android",
                  "platformVersion": "8.1.0",
                  "deviceName": "b13249e2",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity",
                  "noReset":"True"
            }

    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
    sleep(10.0)

    def join(self,name,password):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)

    #退出登录
    def guanbi(self):
        #find_element_by_class_name()定位一个class属性的元素，要求该元素唯一
        #find_elements_by_class_name()定位多个class属性的元素，元素是多个
        a=self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        print(a)

    # def fenbian_lv(self,id):
        a[3].click()
        sleep(5.0)
    def shang_hua(self):
        size = self.dr.get_window_size()
        x1 = size['width'] * 0.5  # 坐标50
        y1 = size['height'] * 0.25  # 起始y坐标
        y2 = size['height'] * 0.75
        for i in range(2):
            self.dr.swipe(x1, y2, x1, y1)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
    def tuichu(self):
        self.dr.quit()


if __name__ == '__main__':
    # unittest.main()
    go=ce()
    # sleep(10.0)
    go.join('17630926181','woshengri0902')
    go.guanbi()
    go.shang_hua()
    go.tuichu()
