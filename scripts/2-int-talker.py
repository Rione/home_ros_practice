#!/usr/bin/env python3

# モジュールのインポート
import rospy
from std_msgs.msg import Int32

# クラスの定義
class Talker():
    # コンストラクタの定義
    def __init__(self):
        # パブリッシャの生成
        # トピック名、メッセージの型、キューサイズ
        self.number_pub = rospy.Publisher("/number", Int32, queue_size=10)
        self.number = 0
    
    # メッセージをパブリッシュする関数
    def publish(self):
        # 送るメッセージの定義
        int32 = Int32()
        int32.data = self.number
        
        # メッセージを送る
        self.number_pub.publish(int32)
        
        # 画面に表示
        rospy.loginfo(f"Published {int32.data}")
        
        # numberを1増やす
        self.number += 1

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("int_talker_node")
    
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
