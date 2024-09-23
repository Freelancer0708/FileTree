import os

def generate_file_tree(dir_path, prefix="", exclude_dirs=None):
    # 結果を格納するリスト
    file_tree = []

    # 除外するディレクトリリストがNoneの場合、空のリストに設定
    if exclude_dirs is None:
        exclude_dirs = []

    # 指定されたディレクトリ内のファイルとディレクトリを取得
    items = sorted(os.listdir(dir_path))

    # 各アイテム（ファイルまたはディレクトリ）を処理
    for index, item in enumerate(items):
        # アイテムのフルパスを取得
        full_path = os.path.join(dir_path, item)
        
        # 除外リストに含まれるディレクトリはスキップ
        if os.path.isdir(full_path) and item in exclude_dirs:
            continue

        # ディレクトリとファイルを区別して適切なプレフィックスを決定
        connector = "├── " if index < len(items) - 1 else "└── "
        file_tree.append(prefix + connector + item)

        # ディレクトリであれば再帰的にファイルツリーを取得
        if os.path.isdir(full_path):
            sub_prefix = "│   " if index < len(items) - 1 else "    "
            file_tree.extend(generate_file_tree(full_path, prefix + sub_prefix, exclude_dirs))

    return file_tree

# 使用例: フォルダ内のファイルツリーを表示（特定のフォルダを除外）
directory_path = "D:/"  # ここに対象フォルダのパスを設定
exclude_folders = ["node_modules",".git"]  # 除外するフォルダ名をリストで指定
file_tree = generate_file_tree(directory_path, exclude_dirs=exclude_folders)

# ファイルツリーをテキストエリアで表示可能な形式に変換
file_tree_text = "\n".join(file_tree)
print(file_tree_text)
