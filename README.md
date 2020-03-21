### conda常用命令
```
conda list ：查看安装哪些包
conda upgrade --all：更新所有包
conda install 安装包
conda search search_term 进行搜索
```

### wxPython依賴環境 
- Python2.7
### 依赖包
environment.yaml

### 导出依赖环境
```
conda env export >environment.yaml
### 导入依赖环境
conda env import environment.yaml

```
### python转化为exe可执行程序
```
pip install pyinstaller


pyinstaller -F test04.py
```

### wxpython可视化界面开发
- 界面开发工具
wxFormBuilder
