import subprocess
import os
import sys

def run_command(command, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def setup_git_repo():
    """设置Git仓库并提交代码"""
    project_dir = r"c:\Users\ajyq2\.vscode\汇率"

    print("正在检查Git安装...")
    returncode, stdout, stderr = run_command("git --version")
    if returncode != 0:
        print("错误：Git未安装。请先安装Git for Windows：")
        print("1. 访问 https://git-scm.com/download/win")
        print("2. 下载并安装Git")
        print("3. 重新运行此脚本")
        return False

    print("Git已安装，版本：", stdout.strip())

    # 检查是否已经是Git仓库
    if not os.path.exists(os.path.join(project_dir, ".git")):
        print("初始化Git仓库...")
        returncode, stdout, stderr = run_command("git init", cwd=project_dir)
        if returncode != 0:
            print(f"初始化失败：{stderr}")
            return False

    # 配置用户信息（需要用户提供）
    print("请提供您的Git用户信息：")
    name = input("姓名：")
    email = input("邮箱：")

    run_command(f'git config user.name "{name}"', cwd=project_dir)
    run_command(f'git config user.email "{email}"', cwd=project_dir)

    # 添加文件
    print("添加文件到Git...")
    returncode, stdout, stderr = run_command("git add .", cwd=project_dir)
    if returncode != 0:
        print(f"添加文件失败：{stderr}")
        return False

    # 提交
    print("提交更改...")
    returncode, stdout, stderr = run_command('git commit -m "Initial commit: 汇率数据抓取与可视化程序"', cwd=project_dir)
    if returncode != 0:
        print(f"提交失败：{stderr}")
        return False

    print("本地提交成功！")
    print("\n接下来请手动操作：")
    print("1. 访问 https://github.com/new 创建新仓库")
    print("2. 仓库命名为 'exchange-rate-analysis' 或您喜欢的名字")
    print("3. 不要初始化README（因为我们已经有了）")
    print("4. 复制仓库URL")
    print("5. 运行以下命令（替换为您的仓库URL）：")
    print(f'git remote add origin <您的仓库URL>')
    print(f'git push -u origin master')

    return True

if __name__ == "__main__":
    setup_git_repo()