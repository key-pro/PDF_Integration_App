### PDF統合ソフト　管理部専用仕様

### exe方法

①pyinstaller --onefile main.py

③pyinstaller main.spec

⑥作成されたdistのフォルダーにexeがあるので問題ないか確認する

コマンド実行中にESETがウイルスの誤検知する場合はESETの検出除外の設定して下さい。

### ファイル名命名ルール

- 例えば、もしパスが C:\Documents\Reports\202401_Panorama_月次報告書.pdf であれば、以下のように生成されます:
path_parts[-3] → Reports
path_parts[-4] → Documents
path_parts[-2] → 202401_Panorama
結果として、ファイル名は 【Reports】_Documents_202401_Panorama.pdf
