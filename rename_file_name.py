import re
import os

def generate_file_name(file_content):
    # updated_atとtitleを正規表現を使って抽出
    pattern_updated_at = r"updated_at: '(\d{4}-\d{2}-\d{2})"
    pattern_title = r"title: (.+)"
    updated_at_match = re.search(pattern_updated_at, file_content)
    title_match = re.search(pattern_title, file_content)

    # ファイル名を生成
    if updated_at_match and title_match:
        updated_at = updated_at_match.group(1).replace("-", "")
        title = title_match.group(1)
        new_file_name = f"{updated_at}_{title}.md"
        return new_file_name
    else:
        return None

def rename_file(file_path):
    try:
        # ファイルを読み取りモードで開く
        with open(file_path, "r", encoding="utf-8") as file:
            # ファイルの内容を読み取る
            file_content = file.read()
            # 読み取った内容を処理する
            new_file_name = generate_file_name(file_content)
            if new_file_name:
                # ファイル名を変更する
                directory = os.path.dirname(file_path)
                new_file_path = os.path.join(directory, new_file_name)
                file.close()
                os.rename(file_path, new_file_path)
                print(f"ファイル名を変更しました: {new_file_path}")
            else:
                print("情報が見つかりませんでした。")

    except FileNotFoundError:
        print("ファイルが見つかりません。")
    except IOError as e:
        print(f"{e}: ファイルの読み取り中にエラーが発生しました。")

file_path = "public/0b32174fced2533da4ab.md"
rename_file(file_path)
