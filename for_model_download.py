from huggingface_hub import snapshot_download
model_path = snapshot_download(repo_id="defog/sqlcoder-7b-2",repo_type="model", local_dir="../models/sqlcoder-7b-2", local_dir_use_symlinks=False)
print("welcome")