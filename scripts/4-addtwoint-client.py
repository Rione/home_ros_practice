#!/usr/bin/env python3

# モジュールのインポート
import rospy
from ros_practice_msgs.srv import AddTwoInt

# クラスの定義
class Client():
    # コンストラクタの定義
    def __init__(self):
        # クライアントの定義
        # サービス名、メッセージの型
        self.client = rospy.ServiceProxy("/addtwoint", AddTwoInt)
    
    # サービスの呼び出しをする関数
    def call(self, x, y):
        # 指定したサービス名が使えるまで待つ
        rospy.wait_for_service("/addtwoint")
        
        # resにサービスで呼び出して返ってきた値を代入
        res = self.client(x, y)
        
        # サービスで呼び出した値を返す
        return res

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("addtwoint_client_node")

    # クラスのインスタンス化
    client = Client()
    
    # input関数で値を入力する
    x = int(input("xの値は? -> "))
    y = int(input("yの値は? -> "))

    # 画面に表示
    rospy.loginfo(f"Requesting x = {x} y = {y}")
    
    # resにサービスで呼び出して返ってきた値を代入
    res = client.call(x, y)
    
    # 画面に表示
    rospy.loginfo(f"Response z = {res.z}")
