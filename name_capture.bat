rem カレントディレクトリをこの .bat ファイルの場所にする
cd /d %~dp0

rem 初回起動時に venv 環境を作成
if not exist venv (
  python -m venv venv
)

rem venv を有効化
call venv\Scripts\activate.bat

rem 依存パッケージをインストール
python -m pip install -r requirements.txt

rem ドラッグドロップされたファイルのパスを引数にしつつスクリプトを起動
python name_capture.py %*

pause
