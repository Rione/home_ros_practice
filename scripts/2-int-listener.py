#!/usr/bin/env python3

# モジュールのインポート
import rospy
from std_msgs.msg import Int32

# クラスの定義
class Listener():
    # コンストラクタの定義
    def __init__(self):
        # サブスクライバの生成
        # トピック名、メッセージの型、データを受け取ったら実行する関数
        self.text_sub = rospy.Subscriber("/number", Int32, self.callback)
    
    # コールバック関数の定義
    def callback(self, msg):
        # 受け取ったメッセージを2倍にして、numberに代入する
        number = msg.data * 2
        
        # 受け取ったメッセージを画面に表示
        rospy.loginfo(f"Subscribed {number}")

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("int_listener_node")
    
    # クラスのインスタンス化
    listener = Listener()
    
    # Ctrl-Cが押されるまで実行
    rospy.spin()
