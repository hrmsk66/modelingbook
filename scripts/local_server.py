#!/usr/bin/env python3
"""
ローカルでGitHub Pagesサイトをプレビューするための簡易サーバー
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).parent.parent / "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

def main():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"📚 Snowflake Data Modeling Lab - ローカルプレビュー")
        print(f"🌐 サーバーが起動しました: http://localhost:{PORT}")
        print(f"📁 提供ディレクトリ: {DIRECTORY}")
        print(f"\n✨ ブラウザで自動的に開きます...")
        print(f"🛑 終了するには Ctrl+C を押してください\n")
        
        # ブラウザで自動的に開く
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 サーバーを停止しました")

if __name__ == "__main__":
    main()