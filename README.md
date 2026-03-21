# 汇率数据分析与可视化项目

这是一个Python项目，用于实时抓取汇率数据、进行数据分析，并生成图表展示趋势。

## 功能
- 实时抓取USD/CNY汇率数据（每5分钟）
- 计算移动平均趋势
- 生成汇率走势图
- Web应用展示图表
- 单独CNY/EUR近7日走势图

## 依赖
- requests
- pandas
- matplotlib
- flask
- schedule

## 安装
1. 安装依赖：`pip install -r requirements.txt`
2. 运行主程序：`python main.py`
3. 访问 http://localhost:5000 查看图表

## 文件说明
- `main.py`: 主程序，启动web服务器和调度器
- `data_fetcher.py`: 数据抓取模块
- `analyzer.py`: 数据分析模块
- `plotter.py`: 图表生成模块
- `cny_eur_plot.py`: CNY/EUR单独图表程序
- `requirements.txt`: 依赖列表
- `data.csv`: 存储的汇率数据

## 注意
- 需要设置ExchangeRate-API密钥在`data_fetcher.py`中
- 图表保存为PNG文件