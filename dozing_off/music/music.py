#-*- cording: utf-8 -*-

import wave

import pyaudio

# チャンク数を指定
CHUNK: int = 1024
filename: str = r'kitten_quest.wav'

music_file = wave.open(filename, 'rb')

# PyAudioのインスタンスを生成
player = pyaudio.PyAudio()

# Streamを生成
stream = player.open(format=player.get_format_from_width(music_file.getsampwidth()),
                channels=music_file.getnchannels(),
                rate=music_file.getframerate(),
                output=True)

"""
    format: ストリームを読み書きする際のデータ型
    channels: モノラルだと1、ステレオだと2、それ以外の数字は入らない
    rate: サンプル周波数
    output: 出力モード
"""

# データを1度に1024個読み取る
data = music_file.readframes(CHUNK)

# 実行
while data != '':
    # ストリームへの書き込み
    stream.write(data)
    # 再度1024個読み取る
    data = music_file.readframes(CHUNK)

# ファイルが終わったら終了処理
stream.stop_stream()
stream.close()

player.terminate()
