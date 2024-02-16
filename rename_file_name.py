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

def rename_files_in_directory(directory):
    # 指定されたディレクトリ内のファイルを取得
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            try:
                # ファイルを読み取りモードで開く
                with open(file_path, "r", encoding="utf-8") as file:
                    # ファイルの内容を読み取る
                    file_content = file.read()
                # ファイル名を変更する前にファイルを閉じる
                file.close()

                # 読み取った内容を処理する
                new_file_name = generate_file_name(file_content)
                if new_file_name:
                    # 新しいファイルパスを生成
                    new_file_path = os.path.join(directory, new_file_name)
                    new_file_name = new_file_name.replace("/", "／")
                    # ファイル名を変更する
                    os.rename(file_path, new_file_path)
                    print(f"ファイル名を変更しました: {new_file_path}")
                else:
                    print(f"{file_path}: 情報が見つかりませんでした。")

            except FileNotFoundError:
                print(f"{file_path}: ファイルが見つかりません。")
            except IOError as e:
                print(f"{file_path}: {e}: ファイルの読み取り中にエラーが発生しました。")

directory_path = "public"
rename_files_in_directory(directory_path)
