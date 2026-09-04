# schedule-weather-mailer
- 気象庁の公開APIから東京の天気予報を取得し、毎日決まった時刻に自動でメール通知するPythonツールです。


# Demo

## console出力
### 通常実行時
```bash
2026-08-27 20:27:00 INFO serverへ接続開始
2026-08-27 20:27:01 INFO メール送信完了
```

### 天気データ取得失敗時
```bash
2026-08-27 20:27:00 ERROR dataの取得に失敗しました
```
(このとき処理は sys.exit() により安全に停止し、以降のメール送信処理は実行されません)

## 受信メール例
```
件名: 天気予報のお知らせ
本文:
東京の天気は、くもり 所により 雨 で 雷を伴うです
予想気温は、['25', '31']です
```


# Features
- 天気データ自動取得: 気象庁の公開API(登録不要)から、東京地方の天気予報・気温を取得します。

- メール自動送信: 取得した天気情報を、Gmail(smtplib)経由で指定の宛先に自動送信します。

- 定期実行(スケジューリング): APSchedulerの`cron`トリガーにより、毎日決まった時刻に自動実行されます。

- 認証情報の安全な管理: メールアドレス・アプリパスワードなどの秘密情報は`.env`ファイルに分離し、リポジトリには含めていません(`.gitignore`で除外)。

- 例外処理・早期終了設計: API取得失敗・メール送信失敗時は、エラー内容をログに記録した上で`sys.exit()`により処理を安全に停止します。

- ロギング: 実行時刻、天気取得の成否、メール送信の成否を`log/app.log`へ一元的に記録します。

- モジュール分割設計: 天気取得(`weather.py`)・メール送信(`send_mail.py`)・スケジューリング(`main.py`)を機能ごとに分離し、それぞれ独立して呼び出し・確認できる構成にしています。

- テストコード: pytestによる単体テスト(生存率計算などの主要ロジック検証)を別プロジェクトで実践済み。同様の設計思想を踏襲しています。


# Requirement
- Python 3.13
- 使用ライブラリ: requests, smtplib(標準ライブラリ), python-dotenv, apscheduler, logging(標準ライブラリ)


# App Profile
- 開発ツール: VSCode
- 管理手法: Study plusによる学習記録、GitHubでのコミット管理


# Installation
- リポジトリをクローンし、対象のディレクトリへ移動します。

```bash
git clone https://github.com/takuto-seto/scheduler_sender_app.git
cd schedule-weather-mailer
```

- 仮想環境を作成し、有効化します。

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- 必要なライブラリをインストールします。

```bash
pip install requests python-dotenv apscheduler
```

- プロジェクトルートに`.env`ファイルを作成し、以下のキーを設定します(値は各自のGmailアカウント情報に置き換えてください)。

```
SENDER_EMAIL=送信元のメールアドレス
SENDER_PASSWORD=Gmailのアプリパスワード(16桁、スペースなし)
RECEIVER_EMAIL=送信先のメールアドレス
```

**注意**:`SENDER_PASSWORD`には通常のGoogleログインパスワードではなく、2段階認証を有効にした上で発行する「アプリパスワード」が必要です。


# Usage
- `log`フォルダを作成します(初回のみ)。

```bash
mkdir log
```

- スケジューラを起動します。

```bash
python3 main.py
```

- 実行すると、`main.py`内で指定した時刻(`hour`, `minute`)に、毎日自動で天気予報メールが送信されます。停止する場合は`Ctrl+C`を押してください。


# Note
- API連携の堅牢性: 気象庁APIのレスポンスが`200`以外の場合、天気取得関数はエラーをログに記録した上で`sys.exit()`により処理を停止し、不完全な情報でメールが送信されることを防いでいます。

- ロギング設計: `logging.basicConfig()`は実行の起点となる`main.py`側でのみ設定し、各モジュール(`weather.py`, `send_mail.py`)では設定を行わない一元管理方式を採用しています(複数箇所での設定によるログ出力先の競合を回避するため)。

- スレッドとGUIの制約: 本ツール自体はグラフ描画を行いませんが、同様の設計を用いた別プロジェクト(Titanic分析ツール)にて、APSchedulerのワーカースレッド上でmatplotlibのGUIバックエンドを使用するとエラーになることを確認し、`matplotlib.use('Agg')`による非対話的backendへの切り替えで対応した実績があります。

- 認証情報の分離: `.env`は`.gitignore`に含めており、Gitの追跡対象外です。リポジトリをクローンした場合、各自で`.env`を作成する必要があります。

- 実行環境依存の注意: 本ツールはmacOS環境で開発・動作確認しています。Windows環境で使用する場合、`APScheduler`自体はOS非依存で動作しますが、`smtplib`のSMTP接続やパス指定については別途動作確認が必要です。


# Author
t.seto
