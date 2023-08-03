#!/usr/bin/env python3

# モジュールのインポート
import rospy
from std_msgs.msg import String

# クラスの定義
class Talker():
    # コンストラクタの定義
    def __init__(self):
        # パブリッシャの生成
        # トピック名、メッセージの型、キューサイズ
        self.text_pub = rospy.Publisher("/text", String, queue_size=10)
    
    # メッセージをパブリッシュする関数
    def publish(self):
        # 送るメッセージの定義
        string = String()
        string.data = "Hello world"
        
        # メッセージを送る
        self.text_pub.publish(string)
        
        # 画面に表示
        rospy.loginfo(f"Published {string.data}")

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("talker_node")
    
    # クラスのインスタンス化
    talker = Talker()
    
    # ループの周期
    # この場合1Hz、1秒に1回
    rate = rospy.Rate(1)
    
    # ROSが立ち上がっている間は...
    while not rospy.is_shutdown():
        # メッセージをパブリッシュする
        talker.publish()
        
        # 定義した周期になるように一定時間待つ
        rate.sleep()
