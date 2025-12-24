# Pythonプログラムを気軽に作り始められる環境

## 概要

このツールは、Pythonベースのツール実行環境を簡単にセットアップし、ツールを起動するためのスクリプトです。Scoopを使用して必要なツールやライブラリを自動的にインストールし、Pythonの仮想環境を構築します。これにより、環境構築の手間を大幅に削減できます。

---

## 使い方（とても簡単😁）

1. このフォルダを任意の場所に展開します。
2. `_setup.bat` をダブルクリックします。
  処理概要
    - [Scoop](https://scoop.sh/)のインストール（未インストールの場合）
    [Scoopとは](https://qiita.com/talesleaves/items/0880bf31359715035a3c) / [Windowsで環境を極力汚さずにPythonを動かす方法 (Scoop編)](https://qiita.com/rhene/items/a5616857981293d06940)
    - gitのインストール（Scoop使用）
    - gitのsslbackendの設定
    [GitでWindowsの認証局ストアに登録されたルート証明書を使用する](https://qiita.com/akayuki/items/1497ea6c53b63e8691bd)
    - versions bucketの追加
    - Pythonのインストール（Scoop使用）
    - 仮想環境の作成（venv）
    - 仮想環境のアクティベート
    - 仮想環境へpipのインストール
    - 必要なPythonパッケージのインストール（`requirements.txt`を使用）
<br>

3. `_start.bat` をダブルクリックします。
  処理概要
    - 仮想環境のアクティベート
    - 必要なPythonパッケージのインストール（`requirements.txt`を使用）
    - ツールの起動（`app.py`を実行）
    - 仮想環境のディアクティベート

うまく動作しないときは、`_clean.bat`を実行し、再度`_setup.bat`からやり直してください。

---

## 動作環境

- Windows 10 以降
- インターネット接続（初回セットアップ時に必要）

---

## 概要図

### スクリプト関連図

:::mermaid

```mermaid
flowchart LR
    developer[<font size="7">👩‍💻</font><br>開発者]@{ shape: stadium}
    subgraph venv
        cre((<font size="5">➕</font>))
        activate1((<font size="5">▶️</font>))
        subgraph setupvenv [setup on venv]
            installpip[[install pip]]
            installpackages[[pip install -r requirements.txt]]
        end
        deactivate1((<font size="5">⏸️</font>))
        activate2((<font size="5">▶️</font>))
        subgraph startvenv [start on venv]
            python[[python]]
        end
        app.py
        deactivate2((<font size="5">⏸️</font>))
    end
    developer -->|環境構築| _setup.bat
    _setup.bat -->|環境構築| setup_env.ps1
    setup_env.ps1 -->|scoopインストール<br>Pythonインストール| scoop[[scoop]]

    _setup.bat -->|環境構築| setup_venv.ps1
    setup_venv.ps1 -->|Python仮想環境作成| cre

    setup_venv.ps1 -->|仮想環境アクティベート| activate1
    activate1 --> setupvenv
    setup_venv.ps1 -->|pipをインストール| installpip
    setup_venv.ps1 -->|requirements.txtから<br>パッケージインストール| installpackages
    setup_venv.ps1 -->|仮想環境非アクティブ化<br>| deactivate1
    deactivate1 --> setupvenv
    developer -->|コーディング| app.py

    developer -->|スタート| _start.bat
    _start.bat -->|アプリ起動| start_app.ps1
    start_app.ps1 -->|仮想環境アクティベート<br>| activate2
    activate2 --> startvenv
    start_app.ps1 -->|アプリ起動| python
    python --> app.py
    start_app.ps1 -->|仮想環境非アクティブ化<br>| deactivate2
    deactivate2 --> startvenv
```

:::

### スクリプト動作シーケンス図

:::mermaid

```mermaid
 sequenceDiagram

    actor Developer as 開発者<br>👩‍💻
    participant BAT as .bat
    participant SP as .ps1
    participant V as venv
    participant APP as app.py
    participant SC as scoop

    Developer->>BAT: _setup.bat<br>ダブルクリック
    activate BAT
    BAT->>SP: setup_env.ps1<br>環境構築
    activate SP
    SP->>SC: scoop インストール<br>Python インストール
    activate SC
    SP -->>BAT: 完了
    deactivate SP

    BAT->>SP: setup_venv.ps1<br>仮想環境構築
    activate SP
    SP->>V: 仮想環境作成
    activate V
    SP->>V: activate.bat
    activate V
    SP->>V: pipインストール
    SP->>V: パッケージインストール
    SP-XV: deactivate.bat
    deactivate V
    SP -->>BAT: 完了
    deactivate SP
    BAT -->>Developer: 完了
    deactivate BAT

    Developer->>APP: コーディング

    Developer->>BAT: _start.bat<br>ダブルクリック
    activate BAT
    BAT->>SP: start_app.ps1<br>ツールスタート
    activate SP
    SP->>V: activate.bat
    activate V
    SP->>V: アプリ起動
    V->>APP: アプリ起動
    activate APP
    deactivate APP
    destroy APP
    APP-->>V: 完了

    SP-XV: deactivate.bat
    deactivate V
    SP-->>BAT: 完了
    deactivate SP
    BAT-->>Developer: 完了
    deactivate BAT

    deactivate V
    deactivate SC
```
:::

---
