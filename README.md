# Project Goal

对每日上传的探针扫描文件进行涉密性研判，过滤非涉密文件，保留疑似涉密与涉密文件，减轻人工复检工作量和压力

# SOP

1. 数据采集与预处理

- 从业务数据库获取元数据（文件名、内容、大小、路径。。。）
- 预处理：根据文件类型调用不同的解析工具提取文本（功能待定）

2. 初筛过滤

- 利用正则和白名单词库进行全库快速扫描，过滤绝对安全的文件，减少Token使用，优化性能

3. 智能研判（concurrency）

- 判断数据对应的具体单位场景（消防、金融。。。），调取相关“定密标准库”
- 正反向涉密LLM研判：正向以“定密标准库”的相关标准为证据，判断文件内容是否为涉密；反向以通用文件标准为证据，判断文件是否为通用文件
- 仲裁审判LLM：根据正反向研判结果，以固定标准裁决文件是否涉密，并输出结论置信度

4. 人工复检/反馈

- 对于疑似涉密、涉密、低置信度非涉密文件推送到人工复检

5. 审计

- 记录完整的审计日志（模型、时间、判断依据），以备日后追溯

# Core Schema

1. Input Schema

```
file_name:str 文件名
summary:str 摘要
full_txt:str  全文
organization:str  组织
ip:str  ip地址
response_person:str 责任人
hit_keywords:str  命中关键词
```

2. output Schema

```
trace_id: int 用于追踪的唯一id
classification:enum[CONFIDENTIAL,SUSPICIOUS,NORMAL] 分类标签
status: enum[success,error]
confidence:float(0-1) 置信度
reasoning:str 研判理由
evidence:List[str]  证据片段
policy_reference: str 定密依据
```

# Tool List

- FileParse（文件解析）：docx、pdf、txt提取文字，图片OCR
- PolicyRetriever（知识库/RAG）：连接企业内部的“涉密管理方法”数据库，提供判断依据
- DBConnector（数据库连接）：读取待扫清单
- Regular（正则初筛）：根据定密规则，采用正则表达式进行初筛

# Environmental constraints

- 模型部署：私有化，防止数据外泄

# Optimize Opreation

- FeedBack Loop：人工复检后，将修正结果反馈至白名单库或作为Few-shot案例喂给LLM，实现系统自进化

# Benchmark

- 50-100份测试集
