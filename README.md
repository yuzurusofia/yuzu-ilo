# yuzu-ilo
yuzuru_sofiaによるyuzuru_sofiaのためのツール。  
自作しているdiscordのbot用の機能だったり自言語関連の機能だったりいろいろです。  
yuzu_ilo.pyが本体です。

# 機能
- dice
  - ダイスコードを入れるとさいころを振ってくれます。
- efia
  - unixtimeをefia数に変換できます。
  - unixtimeを省略したときは今日のefia数を確認できます。
- yuki_kekamu
  - efia数をyuki暦での日付に変換できます。
  - efia数を省略したときは今日のyuki暦での日付を確認できます。

# 既知の問題 (未検証のもの含む)
- float型でも「nanpa ala」と(たぶん)言われる。
- unixtimeをfloatからintに変換するときにint関数を使っているので、負の値だったときに(たぶん)1ずれる。
  - 現在のunixtimeが負の数のときの問題なので、自分で負の値をいれる分には問題なく動くはずです。
  - 1970年より前にタイムスリップしない限り大丈夫だと思います。
- 86から97行目
- 52行目
  - ただの消し忘れです
