# pair-plot
Excelファイルの中身を基にペアプロットを出力する程度の能力

ファイル内のimportを基に適宜インストールしてください（Python 3.9.5）
matplotlib, pandas, seaborn, openpyxlが必要です（2021/8/9現在）

1つ目の引数にはExcelファイル名、2つ目の引数（任意）には色分けに使いたい列名を指定してください
> pair_plot_from_excel.py example.xlsx
> pair_plot_from_excel.py example.xlsx species

Excelファイルからの読み込みは現在以下の通りです。
複数シート読み込みやheader, indexのカスタマイズが必要であればpd.read.excelのオプションを参照。
· 最初のシートのみ読み込み
· 最初の行がheader
· どの列もindexでない
