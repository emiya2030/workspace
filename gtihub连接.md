# 取消与远程仓库的连接
git remote remove origin

# 与远程仓库建立连接
git remote add origin https://github.com/emiya2030/workspace.git

# 初始化
git init


1. 查看远程连接
git remote -v
2. 取消与远程仓库的连接
git remote remove origin
3. 初始化仓库
git init
4. 添加所有文件
git add .
5. 提交所有文件到本地仓库
git commit -m '备注信息'
6. 连接到远程仓库
git remote add origin 你的远程仓库地址
PS：“远程仓库地址”为新建的空仓库

7. 将项目推送到远程仓库
git push -u origin master