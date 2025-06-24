# CLAUDE.md - プロジェクト継続のためのコンテキスト

## プロジェクト概要
「Data Modeling with Snowflake」という英語書籍の内容を日本語化し、個人学習用にGitHub Pagesでホストするプロジェクト。

## 現在の進捗状況

### ✅ 完了したタスク
1. **基本構造のセットアップ**
   - `docs/` - GitHub Pages用のHTMLコンテンツ
   - `scripts/` - 翻訳・生成用のPythonスクリプト
   - `orig/` - オリジナルの英文コンテンツ（.gitignore対象）

2. **翻訳済みコンテンツ**
   - 序文（Preface）- 全文翻訳完了
   - 第1部イントロ - 全文翻訳完了
   - 第1章「モデリングの力を解き放つ」- 全文翻訳・画像配置完了

3. **セキュリティ対策**
   - robots.txt - クローラー拒否設定
   - HTMLメタタグ - noindex設定
   - .htaccess - 追加のアクセス制御

4. **画像の配置**
   - 図1.1: B19467_01_001.jpg - ベック以前のロンドン地下鉄マップ
   - 図1.2: B19467_01_002.jpg - Snowsight UIのテーブルリスト
   - 図1.3: B19467_01_003.jpg - カラスの足記法（概念モデル）
   - 図1.4: HTMLテーブル - トランザクションDBとDWHの比較
   - 図1.5: B19467_01_005.jpg - カラスの足記法（物理モデル）
   - 図1.6: B19467_01_006.jpg - 変換要件のリレーショナルモデル
   - 図1.7: B19467_01_007.jpg - 視覚的な変換モデリング

## ディレクトリ構造
```
modelingbook/
├── docs/                      # GitHub Pages用コンテンツ
│   ├── index.html            # トップページ
│   ├── preface.html          # はじめに
│   ├── part1/
│   │   ├── index.html        # 第1部概要
│   │   └── chapter1.html     # 第1章（画像付き）
│   ├── images/
│   │   └── chapter1/         # 第1章の画像
│   ├── css/
│   │   └── style.css         # 日本語対応スタイル
│   ├── robots.txt            # クローラー制御
│   ├── .htaccess             # アクセス制御
│   └── GITHUB_PAGES_SETUP.md # セットアップガイド
├── scripts/                   # ユーティリティ
│   ├── generate_japanese_content.py
│   ├── translate_full_content.py
│   ├── translate_chapter1_with_images.py
│   └── local_server.py       # ローカルプレビュー
├── orig/                      # オリジナルコンテンツ（.gitignore）
│   ├── preface.txt
│   ├── part1.txt
│   ├── part1_chapter1.txt
│   └── chapter1_images/      # 画像ファイル
├── .gitignore                 # Git除外設定
└── CLAUDE.md                  # このファイル
```

## 翻訳方針
1. **全文翻訳** - 原文を省略せずに完全に日本語化
2. **自然な日本語** - 直訳ではなく、日本語として読みやすい文章
3. **専門用語** - 適切な日本語訳を使用（例: surrogate key → サロゲートキー）
4. **画像の扱い** - 原書の画像は著作権保護のため.gitignore対象

## 次回の作業候補
1. **第2章以降の翻訳**
   - Chapter 2: An Introduction to the Four Modeling Types
   - Chapter 3: Mastering Snowflake's Architecture
   - 以降の章

2. **機能拡張**
   - 章間のナビゲーション改善
   - 検索機能の追加
   - 印刷用CSS
   - ダークモード対応

3. **コンテンツの充実**
   - 各章のサマリーページ
   - 用語集の作成
   - 練習問題の追加

## 技術的な注意事項
- **画像パス**: 章のHTMLからは `../images/chapter1/` を使用
- **CSS**: 日本語フォントに最適化済み
- **文字コード**: UTF-8で統一
- **改行**: LFで統一

## コマンド集
```bash
# ローカルプレビュー
python3 scripts/local_server.py

# 新しい章の翻訳生成（スクリプトの更新が必要）
python3 scripts/translate_full_content.py

# Gitステータス確認
git status

# GitHub Pagesへのデプロイ
git add docs/
git commit -m "Update: [変更内容]"
git push
```

## ユーザーの要望
- 英文コンテンツの要約ではなく、全文翻訳
- 個人学習用のため、検索エンジンにインデックスされないようにする
- 画像は適切な位置に配置

## 現在の課題
- 画像ファイルは著作権のため、GitHubにプッシュできない
- GitHub Pagesでの画像表示方法を検討する必要がある

---

最終更新: 2024-06-24
次回作業時は、このファイルを参照して作業を継続してください。