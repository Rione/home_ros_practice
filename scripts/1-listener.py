#!/usr/bin/env python3

# モジュールのインポート
import rospy
from std_msgs.msg import String

# クラスの定義
class Listener():
    # コンストラクタの定義
    def __init__(self):
        # サブスクライバの生成
        # トピック名、メッセージの型、データを受け取ったら実行する関数
        self.text_sub = rospy.Subscriber("/text", String, self.callback)
    
    # コールバック関数の定義
    def callback(self, msg):
        # 受け取ったメッセージを画面に表示
        rospy.loginfo(f"Subscribed {msg.data}")

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("listener_node")
    
    # クラスのインスタンス化
    listener = Listener()
    
    # Ctrl-Cが押されるまで実行
    rospy.spin()
