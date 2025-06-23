#!/usr/bin/env python3
"""
英語テキストファイルを日本語HTMLに変換するスクリプト
使用方法: python convert_to_html.py <input_file> <output_file> <template_type>
template_type: preface, part_intro, chapter
"""

import sys
import os
from datetime import datetime

def create_html_template(title, content, template_type, nav_items=None):
    """HTMLテンプレートを生成"""
    
    # ナビゲーションメニューの生成
    nav_html = ""
    if nav_items:
        nav_html = "\n".join([f'            <li><a href="{item["href"]}">{item["text"]}</a></li>' for item in nav_items])
    
    # 基本的なナビゲーション項目
    default_nav = [
        {"href": "../index.html" if template_type == "chapter" else "index.html", "text": "ホーム"},
        {"href": "../preface.html" if template_type == "chapter" else "preface.html", "text": "はじめに"},
        {"href": "../part1/index.html" if template_type == "chapter" else "part1/index.html", "text": "第1部"}
    ]
    
    nav_html = "\n".join([f'            <li><a href="{item["href"]}">{item["text"]}</a></li>' for item in default_nav])
    
    template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - SnowflakeによるデータモデリングLab</title>
    <link rel="stylesheet" href="../css/style.css" if template_type == "chapter" else "css/style.css">
</head>
<body>
    <nav>
        <ul>
{nav_html}
        </ul>
    </nav>

    <div class="container">
        {content}
        
        <footer>
            <p>個人学習用コンテンツ | 最終更新: {datetime.now().strftime('%Y年%m月%d日')}</p>
        </footer>
    </div>
</body>
</html>"""
    
    # CSSパスの修正
    if template_type == "chapter":
        template = template.replace('href="css/style.css"', 'href="../css/style.css"')
    else:
        template = template.replace('if template_type == "chapter" else "css/style.css"', '')
    
    return template

def process_content(text, template_type):
    """テキストコンテンツを処理してHTML形式に変換"""
    lines = text.strip().split('\n')
    html_content = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        
        if not line:
            if in_list:
                html_content.append("</ul>")
                in_list = False
            continue
        
        # タイトル処理
        if template_type == "preface" and line == "Preface":
            html_content.append("<h1>はじめに</h1>")
            html_content.append('<div class="notice">')
            html_content.append('    <div class="notice-title">📝 翻訳についての注記</div>')
            html_content.append('    <p>この内容は「Data Modeling with Snowflake」の序文を日本語に翻訳し、')
            html_content.append('    理解を深めるためにLLMの支援を受けて補完・拡張したものです。</p>')
            html_content.append('</div>')
            continue
        elif template_type == "chapter" and "Unlocking the Power of Modeling" in line:
            html_content.append('<h1><span class="chapter-number">第1章</span>モデリングの力を解き放つ</h1>')
            continue
        elif template_type == "part_intro" and "Part 1:" in line:
            html_content.append("<h1>第1部: データモデリングとSnowflakeアーキテクチャの基本概念</h1>")
            continue
        
        # セクションヘッダー処理
        if line in ["Who this book is for", "What this book covers", "Technical requirements", 
                    "Modeling with purpose", "Leveraging the modeling toolkit"]:
            section_titles = {
                "Who this book is for": "本書の対象読者",
                "What this book covers": "本書の内容",
                "Technical requirements": "技術要件",
                "Modeling with purpose": "目的を持ったモデリング",
                "Leveraging the modeling toolkit": "モデリングツールキットの活用"
            }
            html_content.append(f"<h2>{section_titles.get(line, line)}</h2>")
            continue
        
        # リスト項目の処理
        if line.startswith("Chapter "):
            if not in_list:
                html_content.append("<ul>")
                in_list = True
            # 章番号を日本語に変換
            chapter_num = line.split(",")[0].replace("Chapter ", "第") + "章"
            chapter_title = line.split(", ", 1)[1] if ", " in line else ""
            html_content.append(f"    <li><strong>{chapter_num}</strong>: {chapter_title}（準備中）</li>")
            continue
        
        # 通常の段落
        if in_list:
            html_content.append("</ul>")
            in_list = False
        
        # 図表の参照を処理
        if "Figure" in line:
            line = line.replace("Figure", "図")
        
        html_content.append(f"<p>{line}</p>")
    
    if in_list:
        html_content.append("</ul>")
    
    return "\n        ".join(html_content)

def translate_placeholder(content):
    """翻訳プレースホルダーを追加"""
    notice = """
        <div class="notice">
            <div class="notice-title">🔄 翻訳待機中</div>
            <p>このセクションの日本語翻訳は準備中です。以下は原文の内容です：</p>
        </div>
        
        <blockquote>
"""
    
    # 原文を blockquote で囲む
    lines = content.split('\n')
    formatted_lines = ['            ' + line if line.strip() else '' for line in lines]
    original_content = '\n'.join(formatted_lines)
    
    return notice + original_content + "\n        </blockquote>"

def main():
    if len(sys.argv) < 4:
        print("使用方法: python convert_to_html.py <input_file> <output_file> <template_type>")
        print("template_type: preface, part_intro, chapter")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    template_type = sys.argv[3]
    
    # 入力ファイルを読み込む
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # タイトルを設定
    titles = {
        "preface": "はじめに",
        "part_intro": "第1部の概要",
        "chapter": "第1章: モデリングの力を解き放つ"
    }
    title = titles.get(template_type, "ページ")
    
    # コンテンツを処理
    processed_content = process_content(content, template_type)
    
    # 翻訳プレースホルダーを追加（実際の翻訳が完了するまでの一時的な措置）
    processed_content = translate_placeholder(content)
    
    # HTMLを生成
    html = create_html_template(title, processed_content, template_type)
    
    # 出力ファイルに書き込む
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"HTMLファイルを生成しました: {output_file}")

if __name__ == "__main__":
    main()