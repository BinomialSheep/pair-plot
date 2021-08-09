import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import sys





def main(args):
    # 引数処理
    # 引数の長さが1ならエラー終了（args[0]は実行ファイル名)
    if(len(args) == 1):
        print("引数を入力してください")
        sys.exit(1)
    # 引数の長さが2以上ならargs[1]がExcelファイル名
    excel = args[1]
    # 引数の長さが3以上ならargs[2]が色分けに使う列名
    hue = None
    if(len(args) >= 3):
        hue = args[2]
    # 最初のシートのみが読み込まれる（オプションを付ければ複数シートへ拡張可能）
    # 最初の行をheaderとし、どの列もindexとして指定しない（デフォルトを使用）
    df = pd.read_excel(excel)

    # ペアプロット
    sns.pairplot(df, hue = hue)
    # 表示
    plt.show()

if __name__ == "__main__":
    # 引数名はExcelファイル名、色分けに使いたい列名（任意）
    main(sys.argv)