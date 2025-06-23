# GitHub Pagesセットアップガイド

このガイドでは、作成した日本語コンテンツをGitHub Pagesでホストする手順を説明します。

## 前提条件

- GitHubアカウントを持っていること
- Gitがローカルマシンにインストールされていること

## セットアップ手順

### 1. GitHubリポジトリの作成

1. GitHubにログインします
2. 新しいリポジトリを作成します（プライベートリポジトリでOK）
   - リポジトリ名: `snowflake-modeling-lab`（任意の名前でOK）
   - プライベートリポジトリとして作成

### 2. ローカルリポジトリの初期化とプッシュ

ターミナルで以下のコマンドを実行します：

```bash
# プロジェクトディレクトリに移動
cd /Users/kake/work/modelingbook

# Gitリポジトリを初期化
git init

# .gitignoreファイルを作成
echo "*.pyc
__pycache__/
.DS_Store
*.txt" > .gitignore

# ファイルをステージング
git add docs/ scripts/ .gitignore

# 初回コミット
git commit -m "Initial commit: Snowflake Data Modeling Lab Japanese content"

# メインブランチに名前を変更（必要な場合）
git branch -M main

# リモートリポジトリを追加（YOUR_USERNAMEを自分のGitHubユーザー名に置き換えてください）
git remote add origin https://github.com/YOUR_USERNAME/snowflake-modeling-lab.git

# GitHubにプッシュ
git push -u origin main
```

### 3. GitHub Pagesの有効化

1. GitHubでリポジトリのページを開きます
2. 「Settings」タブをクリックします
3. 左側のメニューから「Pages」を選択します
4. 「Source」セクションで以下を設定：
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/docs`
5. 「Save」をクリックします

### 4. アクセス確認

設定後、数分待つと以下のURLでサイトにアクセスできるようになります：

```
https://YOUR_USERNAME.github.io/snowflake-modeling-lab/
```

## 更新方法

コンテンツを更新する場合：

1. ローカルでファイルを編集
2. 以下のコマンドで変更をプッシュ：

```bash
git add .
git commit -m "Update: 変更内容の説明"
git push
```

GitHub Pagesは自動的に更新されます（数分かかる場合があります）。

## トラブルシューティング

### ページが表示されない場合

1. リポジトリのSettings > Pagesで、デプロイステータスを確認
2. `docs/index.html`が存在することを確認
3. ブラウザのキャッシュをクリアして再度アクセス

### CSSが適用されない場合

1. HTMLファイル内のCSSパスが正しいことを確認
2. GitHub Pagesの基準URLを確認（リポジトリ名がパスに含まれる場合があります）

## セキュリティ設定（個人利用のみの場合）

プライベートリポジトリでもGitHub Pagesは公開されるため、以下の対策を検討してください：

1. **Basic認証の代替案**：
   - GitHub Pagesは直接的なアクセス制限をサポートしていません
   - 代わりに、予測困難なリポジトリ名を使用することで、実質的にプライベートにできます

2. **より安全な方法**：
   - GitHub PagesではなくGitHub Codespacesを使用
   - ローカルでHTMLファイルを直接開く
   - Netlifyなどの他のホスティングサービスでアクセス制限を設定

## 次のステップ

1. 新しい章を追加する場合は、`scripts/generate_japanese_content.py`を更新
2. 必要に応じてCSSスタイルをカスタマイズ
3. 目次やナビゲーションを拡張

何か問題が発生した場合は、お気軽にお尋ねください！