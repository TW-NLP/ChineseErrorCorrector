# ChineseErrorCorrector：中文文本纠错综合平台

[**🇨🇳中文**](https://github.com/TW-NLP/ChineseErrorCorrector/blob/main/README.md)   [**English**](https://github.com/TW-NLP/ChineseErrorCorrector/blob/main/README_EN.md)

<div align="center">
  <a href="https://github.com/TW-NLP/ChineseErrorCorrector">
    <img src="images/image_fx_.jpg" alt="Logo" height="156">
  </a>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/ACL_2026-Main_(ChineseErrorCorrector4--4B)-red" alt="ACL 2026 Main">
  <a href="https://pypi.org/project/ChineseErrorCorrector/"><img src="https://img.shields.io/pypi/v/ChineseErrorCorrector?label=pypi%20-%20data%20augmentation" alt="PyPI"></a>
  <a href="https://huggingface.co/twnlp/ChineseErrorCorrector4-4B"><img src="https://img.shields.io/badge/HuggingFace-ChineseErrorCorrector4--4B-yellow" alt="HuggingFace"></a>
  <a href="https://huggingface.co/twnlp/ChineseErrorCorrector3-4B"><img src="https://img.shields.io/badge/HuggingFace-ChineseErrorCorrector3--4B-yellow" alt="HuggingFace"></a>
  <a href="https://www.modelscope.cn/models/tiannlp/ChineseErrorCorrector3-4B"><img src="https://img.shields.io/badge/ModelScope-ChineseErrorCorrector3--4B-blueviolet" alt="ModelScope"></a>
</p>

-----------------

## 📌 项目定位

**ChineseErrorCorrector** 是一个面向中文文本纠错任务的**综合平台**，集 **学术研究 · 模型评测 · 推理部署 · 数据增强 · 模型训练** 于一体，覆盖 **拼写纠错（CSC）** 与 **语法纠错（CGEC）** 两大核心方向，如有帮助，感谢您的 Star ✨。

🏆 荣获 **2026 ACL Main Oral**（ChineseErrorCorrector4-4B）🎉 · [2024 CCL 冠军](https://aclanthology.org/2024.ccl-3.31/) · [2023 NLPCC-NaCGEC 纠错冠军](#nacgec-数据集-) · [2022 FCGEC 纠错冠军](#fcgec-数据集-)。


### ✨ 平台四大支柱 + 训练入口

| 模块 | 能力 | 入口 |
|:--|:--|:--|
| 🎓 **学术研究** | 持续更新的中文纠错论文集 |  [论文清单](README_paper.md) |
| 📏 **模型评测** | Common Errant：覆盖 80 种语言的通用文本纠错评测工具 | [评测工具文档](ChineseErrorCorrector/scores/README.md)  |
| 🚀 **推理部署** | ChineseErrorCorrector系列模型 + 可选 ELECTRA 字级门控加速 | [快速开始](#-快速开始推理部署) · [ELECTRA 说明](README_ELECTRA.md) |
| 🧪 **数据增强** | 14 种语法错误一键增强（2024 CCL 冠军方案），获得行业监督数据 | [PyPI](https://pypi.org/project/ChineseErrorCorrector/) · [使用文档](ChineseErrorCorrector/README_DAT.md) |
| 🤖 **模型训练** | 开源大规模高质量数据： [34万COT](https://huggingface.co/datasets/twnlp/ChineseErrorCorrector4-4B) 、[200万监督数据](https://huggingface.co/datasets/twnlp/ChinseseErrorCorrectData) 等。| [训练说明](#-模型训练推荐-llama-factory) |

## 🔥🔥🔥 新闻

[2026/06/02] 🎉🎉🎉 **ChineseErrorCorrector4-4B 论文发布！**  [查看论文](https://aclanthology.org/2026.acl-long.1733/)

[2026/05/19] 🎉🎉🎉 **ChineseErrorCorrector4-4B 正式开源发布！** 论文荣获 **ACL 2026 Main**，在 NACGEC 和 CSCD 双榜刷新 SOTA，全面超越 GPT-4 及同量级模型！ 🤗 [HuggingFace 模型地址](https://huggingface.co/twnlp/ChineseErrorCorrector4-4B)

[2026/05/14] 🎉 开源**字级检错门控模型** [xurong123/ChineseErrorDetectorElectra](https://huggingface.co/xurong123/ChineseErrorDetectorElectra)：基于 Chinese ELECTRA 的轻量字级判别器，作为大模型纠错前的可选门控，**仅对疑似有错的句子调用 4B 大模型**，显著节省推理算力。详见 [README_ELECTRA.md](README_ELECTRA.md)。

[2026/02/28] 我们在 HuggingFace 和 ModelScope 开源了 ChineseErrorCorrector3 模型体验地址 🥳，欢迎大家访问进行试用。

  🤗 [HuggingFace 体验地址](https://huggingface.co/spaces/twnlp/ChineseErrorCorrector3) &nbsp;|&nbsp; 👉 [ModelScope 体验地址](https://www.modelscope.cn/studios/tiannlp/ChineseErrorCorrector)

<details>
<summary>📋 查看更多历史更新</summary>

[2025/12/11] 我们正在加速研发全新一代 **ChineseErrorCorrector4-4B** ⚡🔥（即 ACL 2026 Main 论文模型），并同步筹备论文发布！这一版本将力求打造最强的中文文本纠错基线，提供更稳、更快、更准的整体体验。期待与大家再次相遇！🎉

[2025/11/25] 发布[ChineseErrorCorrector3-4B论文](https://arxiv.org/abs/2511.17562) 🎉，更多技术细节，欢迎大家查阅。

[2025/08/08] 发布[通用的文本评测工具-Common Errant（支持80种语言）](https://github.com/TW-NLP/ChineseErrorCorrector/blob/main/ChineseErrorCorrector/scores/README.md) 🎉，可以在高（中文、英文）、低资源（印地语、孟加拉语等）上进行文本纠错的评测。

[2025/08/06] 发布[文本纠错相关论文（持续更新版）](https://github.com/TW-NLP/ChineseErrorCorrector/blob/main/README_paper.md) 🥳，方便大家进行研学。

[2025/08/01] 发布[twnlp/ChineseErrorCorrector3-4B](https://huggingface.co/twnlp/ChineseErrorCorrector3-4B) 🎉🎉🎉，泛化性全面提升，在开源的所有模型中，位列第一，[榜单详情](https://github.com/TW-NLP/ChineseErrorCorrector?tab=readme-ov-file#evaluation%E6%B3%9B%E5%8C%96%E6%80%A7%E8%AF%84%E6%B5%8B)。

[2025/05/01] 根据[建议](https://github.com/TW-NLP/ChineseErrorCorrector/issues/17)，我们重新训练纠错模型(ChineseErrorCorrector2-7B)，并完全开源训练步骤，支持结果复现，[复现教程](https://github.com/TW-NLP/ChineseErrorCorrector/tree/v0.4.0?tab=readme-ov-file#%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C%E5%A4%8D%E7%8E%B0)

[2025/03/17] 更新批量错误文本的解析，[transformers批量解析](https://github.com/TW-NLP/ChineseErrorCorrector?tab=readme-ov-file#transformers-%E6%89%B9%E9%87%8F%E6%8E%A8%E7%90%86) ;[VLLM批量解析](https://github.com/TW-NLP/ChineseErrorCorrector?tab=readme-ov-file#vllm-%E5%BC%82%E6%AD%A5%E6%89%B9%E9%87%8F%E6%8E%A8%E7%90%86)

[2025/03/10] 模型支持多种推理方式，包括 transformers、VLLM、modelscope。

[2025/02/25] 🎉🎉🎉使用200万纠错数据进行多轮迭代训练，发布了[twnlp/ChineseErrorCorrector2-7B](https://huggingface.co/twnlp/ChineseErrorCorrector2-7B)，在 [NaCGEC-2023NLPCC官方评测数据集](https://github.com/masr2000/NaCGEC)上，超越第一名华为10个点，遥遥领先，[技术详情](https://blog.csdn.net/qq_43765734/article/details/145858955)

[2025/02] 为方便部署，使用38万开源拼写数据，发布了[twnlp/ChineseErrorCorrector-1.5B](https://huggingface.co/twnlp/ChineseErrorCorrector-1.5B)

[2025/01] 使用38万开源拼写数据，基于Qwen2.5训练中文拼写纠错模型，支持语似、形似等错误纠正，发布了[twnlp/ChineseErrorCorrector-7B](https://huggingface.co/twnlp/ChineseErrorCorrector-7B)，[twnlp/ChineseErrorCorrector-32B-LORA](https://huggingface.co/twnlp/ChineseErrorCorrector-32B-LORA/tree/main)

[2024/06] v0.1.0版本：🎉🎉🎉开源一键语法错误增强工具，该工具可以进行14种语法错误的增强，不同行业可以根据自己的数据进行错误替换，来训练自己的语法和拼写模型。详见[Tag-v0.1.0](https://github.com/TW-NLP/ChineseErrorCorrector/tree/0.1.0)

</details>

## 🎯 模型列表

| 模型名称 | 纠错类型 | 是否开源 | 描述 |
|:--------|:--------|:-----|:----|
| [**twnlp/ChineseErrorCorrector4-4B**](https://huggingface.co/twnlp/ChineseErrorCorrector4-4B) | 语法+拼写 | ✅ 🔥 | ACL 2026 Main 论文模型。NACGEC $F_{0.5}$ = **50.99**，CSCD Correction F1 = **59.61**，双榜刷新 SOTA，全面超越 GPT-4。 |
| [twnlp/ChineseErrorCorrector3-4B](https://huggingface.co/twnlp/ChineseErrorCorrector3-4B) | 语法+拼写 | ✅  | 使用200万纠错数据进行全量训练，适用于语法纠错和拼写纠错，效果较好。 |
| [twnlp/ChineseErrorCorrector2-7B](https://huggingface.co/twnlp/ChineseErrorCorrector2-7B) | 语法+拼写 | ✅  | 使用200万纠错数据进行多轮迭代训练，适用于语法纠错和拼写纠错，效果较好。 |
| [twnlp/ChineseErrorCorrector-7B](https://huggingface.co/twnlp/ChineseErrorCorrector-7B) | 拼写 | ✅  | 使用38万开源拼写数据，支持语似、形似等拼写错误纠正，拼写纠错效果好。 |
| [twnlp/ChineseErrorCorrector-1.5B](https://huggingface.co/twnlp/ChineseErrorCorrector-1.5B) | 拼写 | ✅  | 使用38万开源拼写数据，支持语似、形似等拼写错误纠正，拼写纠错效果一般。 |
| [xurong123/ChineseErrorDetectorElectra](https://huggingface.co/xurong123/ChineseErrorDetectorElectra) | 字级检错门控（辅助推理） | ✅  | 基于 Chinese ELECTRA 的轻量字级判别器，作为大模型纠错前的可选门控，仅对疑似有错的句子调用 4B 大模型，节省推理算力。详见 [README_ELECTRA.md](README_ELECTRA.md)。 |

## 📊 数据集

| 数据集名称 | 数据链接 | 数据量和类别说明 | 描述 |
|:---------|:--------|:--------------|:----|
| ChinseseErrorCorrect4 Data | [ChinseseErrorCorrect4 Data](https://huggingface.co/datasets/twnlp/ChineseErrorCorrector4-4B) | 34万 | ChineseErrorCorrector4 COT数据集 |
| ChinseseErrorCorrect3 Data | [ChinseseErrorCorrect3 Data](https://huggingface.co/datasets/twnlp/ChinseseErrorCorrectData) | 200万 | ChineseErrorCorrector3 训练数据集 |
| CSC（拼写纠错数据集） | [twnlp/csc_data](https://huggingface.co/datasets/twnlp/csc_data) | W271K(279,816) Medical(39,303) Lemon(22,259) ECSpell(6,688) CSCD(35,001) | 中文拼写纠错的数据集 |
| CGC（语法纠错数据集） | [twnlp/cgc_data](https://huggingface.co/datasets/twnlp/cgc_data) | CGED(20,449) FCGEC(37,354) MuCGEC(2,467) NaCGEC(7,568) | 中文语法纠错的数据集 |
| Lang8+HSK（百万语料-拼写和语法错误混合数据集） | [twnlp/lang8_hsk](https://huggingface.co/datasets/twnlp/lang8_hsk) | 1,568,885 | 中文拼写和语法数据集 |


## 🏗️ Evaluation

为了验证ChineseErrorCorrector系列模型的有效性，我们从泛化性和专业性两个方面进行了全面的对比，都为业界的**Sota**。

说明：泛化性评测 为[pycorrector](https://github.com/shibing624/pycorrector)提出的评测榜单，专业性评测是顶会论文中公认的评测数据集。

### 1、泛化性评测
- 评估指标：F1
- CSC(Chinese Spelling Correction): 拼写纠错模型，表示模型可以处理音似、形似、语法等长度对齐的错误纠正
- CTC(Chinese Text Correction): 文本纠错模型，表示模型支持拼写、语法等长度对齐的错误纠正，还可以处理多字、少字等长度不对齐的错误纠正
- GPU：Tesla V100，显存 32 GB

| Model Name | Model Link | Base Model | Avg | SIGHAN-2015 | EC-LAW | MCSC | GPU | QPS |
|:-----------|:-----------|:-----------|:----|:------------|:-------|:-----|:----|:----|
| Kenlm-CSC | [shibing624/chinese-kenlm-klm](https://huggingface.co/shibing624/chinese-kenlm-klm) | kenlm | 0.3409 | 0.3147 | 0.3763 | 0.3317 | CPU | 9 |
| Mengzi-T5-CSC | [shibing624/mengzi-t5-base-chinese-correction](https://huggingface.co/shibing624/mengzi-t5-base-chinese-correction) | mengzi-t5-base | 0.3984 | 0.7758 | 0.3156 | 0.1039 | GPU | 214 |
| ERNIE-CSC | [PaddleNLP/ernie-csc](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/legacy/examples/text_correction/ernie-csc) | PaddlePaddle/ernie-1.0-base-zh | 0.4353 | 0.8383 | 0.3357 | 0.1318 | GPU | 114 |
| MacBERT-CSC | [shibing624/macbert4csc-base-chinese](https://huggingface.co/shibing624/macbert4csc-base-chinese) | hfl/chinese-macbert-base | 0.3993 | 0.8314 | 0.1610 | 0.2055 | GPU | **224** |
| ChatGLM3-6B-CSC | [shibing624/chatglm3-6b-csc-chinese-lora](https://huggingface.co/shibing624/chatglm3-6b-csc-chinese-lora) | THUDM/chatglm3-6b | 0.4538 | 0.6572 | 0.4369 | 0.2672 | GPU | 3 |
| Qwen2.5-1.5B-CTC | [shibing624/chinese-text-correction-1.5b](https://huggingface.co/shibing624/chinese-text-correction-1.5b) | Qwen/Qwen2.5-1.5B-Instruct | 0.6802 | 0.3032 | 0.7846 | 0.9529 | GPU | 6 |
| Qwen2.5-7B-CTC | [shibing624/chinese-text-correction-7b](https://huggingface.co/shibing624/chinese-text-correction-7b) | Qwen/Qwen2.5-7B-Instruct | 0.8225 | 0.4917 | 0.9798 | 0.9959 | GPU | 3 |
| Qwen3-4B-CTC (CEC3) | [twnlp/ChineseErrorCorrector3-4B](https://huggingface.co/twnlp/ChineseErrorCorrector3-4B) | Qwen/Qwen3-4B | 0.8521 | 0.6340 | 0.9360 | 0.9864 | GPU | 5 |

### 2、语法纠错（两个权威数据集Sota）

#### NaCGEC 数据集 🏆

- 评估工具：ChERRANT  [评测工具](https://github.com/HillZhang1999/MuCGEC)
- 评估数据：[NaCGEC](https://github.com/masr2000/NaCGEC)
- 评估指标：F0.5

| Model Name | Model Link | Prec | Rec | F0.5 |
|:-----------|:-----------|:-----|:----|:-----|
| **twnlp/ChineseErrorCorrector4-4B** 🏆 | [HuggingFace](https://huggingface.co/twnlp/ChineseErrorCorrector4-4B) | **0.5717** | 0.3560 | **0.5099** |
| twnlp/ChineseErrorCorrector3-4B | [HuggingFace](https://huggingface.co/twnlp/ChineseErrorCorrector3-4B) · [ModelScope](https://www.modelscope.cn/models/tiannlp/ChineseErrorCorrector3-4B) | 0.542 | 0.3475 | 0.4874 |
| HW_TSC_nlpcc2023_cgec（华为） | 未开源 | 0.5095 | 0.3129 | 0.4526 |
| 鱼饼啾啾Plus（北京大学） | 未开源 | 0.5708 | 0.1294 | 0.3394 |
| CUHK_SU（香港中文大学） | 未开源 | 0.3882 | 0.1558 | 0.2990 |


#### CSCD 数据集 🏆（拼写检查新 SOTA）

- 评估指标：Correction F1

| Model Name | Correction F1 |
|:-----------|:---:|
| **twnlp/ChineseErrorCorrector4-4B** 🏆 | **59.61** |
| GPT-4 (Few-shot) | 54.41 |
| MDCSpell+ARM | 48.93 |
| SMBERT | 44.67 |

## 🚀 快速开始（推理部署）
<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

本仓库提供 3 种推理调用方式，覆盖单机调试、工程化部署、国内镜像三类场景：

- **🤗 transformers**：单机本地推理，适合调试与小规模评测。
- **👍 VLLM 异步批量推理（工程推荐）**：通过 OpenAI 兼容接口 + 本仓库 `main.py` 后处理，工程化首选。
- **🤖 modelscope**：国内用户镜像下载。

> 以下示例均以最新旗舰模型 **ChineseErrorCorrector4-4B** 为例。如需使用上一代模型，将 model_name 替换为 `twnlp/ChineseErrorCorrector3-4B` 即可。

### 🤗 transformers

```shell
pip install -U transformers torch
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "twnlp/ChineseErrorCorrector4-4B"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

instruction = (
    "假如你是一名专业的纠错专家，请分析输入句子的语法错误类型和修改原因，"
    "并只输出纠正后的语句，错误类型如下：错别字、词语搭配错误、词性错误、"
    "语序错误、成分残缺、成分赘余、关联词使用错误、指代不明、语义逻辑不通、无误。"
)
text_input = "对待每一项工作都要一丝不够。"

messages = [
    {"role": "system", "content": instruction},
    {"role": "user", "content": text_input}
]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.1
)
response = tokenizer.decode(
    generated_ids[0][len(model_inputs.input_ids[0]):],
    skip_special_tokens=True
)
print(response)
```



### 👍 VLLM 异步批量推理（工程推荐）

本仓库的推理主链路通过 OpenAI 兼容接口调用 4B 大模型，需要先用 vLLM 启动模型服务，再通过 `config.py` 配置接口地址即可使用。

- Clone the repo

```sh
git clone https://github.com/TW-NLP/ChineseErrorCorrector
cd ChineseErrorCorrector
```

- Install Conda: please see https://docs.conda.io/en/latest/miniconda.html
- Create Conda env:

```sh
conda create -n zh_correct -y python=3.10
conda activate zh_correct
pip install -r requirements.txt
# 国内镜像：
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
```

使用 vLLM 启动 4B 大模型（OpenAI 兼容接口）：

```sh
# v4（推荐）
CUDA_VISIBLE_DEVICES=0 nohup vllm serve twnlp/ChineseErrorCorrector4-4B \
    --port 8000 \
    --max-model-len 2048 \
    --gpu-memory-utilization 0.9 \
    --seed 42 \
    >chinese_corrector.log 2>&1 &
# 想用 v3：把模型名替换为 twnlp/ChineseErrorCorrector3-4B 即可，--max-model-len 1024 够用
```

在 `ChineseErrorCorrector/config.py` 的 `TextCorrectConfig` 中按需修改接口配置（或用环境变量 `CEC_OPENAI_BASE_URL` / `CEC_OPENAI_API_KEY` / `CEC_OPENAI_MODEL` 覆盖）：

| 配置项 | 默认值 | 说明 |
|:------|:------|:----|
| `OPENAI_BASE_URL` | `http://localhost:8000/v1` | OpenAI 兼容服务地址 |
| `OPENAI_API_KEY` | `EMPTY` | API Key，vLLM serve 默认不校验 |
| `OPENAI_MODEL` | `twnlp/ChineseErrorCorrector4-4B` | 模型名，需与 `vllm serve` 加载的模型一致 |

> 本仓库会按 `OPENAI_MODEL` 名字自动判定 v3/v4（名字含 `4-4B` / `Corrector4` 视为 v4），自动适配 prompt 并解析 v4 输出里的 `<think>...</think>` 思考块；对外接口 v3/v4 一致，v4 时返回结果会额外携带**错误类型**与**修改原因**字段（v3 则为 `None`）。如需手动指定版本，可改 `MODEL_VERSION`（`auto`/`v3`/`v4`）。

批量预测：

```sh
python main.py
# v3 输出（error_type / error_reason 为 None）：
# [{'source': '对待每一项工作都要一丝不够。', 'target': '对待每一项工作都要一丝不苟。',
#   'errors': [('够', '苟', 12)], 'error_type': None, 'error_reason': None},
#  {'source': '大约半个小时左右', 'target': '大约半个小时',
#   'errors': [('左右', '', 6)], 'error_type': None, 'error_reason': None}]

# v4 输出（额外带 error_type / error_reason）：
# [{'source': '下个星期，我跟我朋唷打算去法国玩儿。', 'target': '下个星期，我跟我朋友打算去法国玩儿。',
#   'errors': [('唷', '友', 8)],
#   'error_type': '错别字',
#   'error_reason': '原句中的"朋唷"应为"朋友"，"唷"是语气助词，不能用于表示同伴的词语中，属于同音字误用...'}]
```

## ELECTRA 字级门控（可选）

主链路默认仅调用 4B 大模型 OpenAI 接口。若希望在调用大模型前先过滤明显无错的句子以省算力、降延迟，可启用可选的 ELECTRA 字级判别器门控：在 `ChineseErrorCorrector/config.py` 中将 `TextCorrectConfig.USE_DETECTOR` 设为 `True` 即可，模型、阈值、batch 等细节、性能数据、训练/验证语料与示例代码均见单独文档：[README_ELECTRA.md](README_ELECTRA.md)。

## 数据增强（PyPI 包 · 2024 CCL 冠军方案）

开源「一键语法错误增强工具」，支持 **14 种语法错误增强**，可在任意行业数据上合成训练语料，是 **2024 CCL 冠军方案** 的核心组件。

📦 PyPI 主页：[https://pypi.org/project/ChineseErrorCorrector/](https://pypi.org/project/ChineseErrorCorrector/) · 📖 完整 API 文档：[ChineseErrorCorrector/README_DAT.md](ChineseErrorCorrector/README_DAT.md)

**支持的错误类型**：缺字漏字 / 错别字 / 缺少标点 / 错用标点 / 主语不明 / 谓语残缺 / 宾语残缺 / 其他成分残缺 / 虚词多余 / 其他成分多余 / 主语多余 / 语序不当 / 动宾搭配不当 / 其他搭配不当。

```shell
pip install ChineseErrorCorrector
# 国内镜像：
# pip install ChineseErrorCorrector -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
```

```python
from ChineseErrorCorrector.utils.dat import GrammarErrorDat

dat = GrammarErrorDat()
print(dat.lack_word("小明住在北京"))       # 缺字漏字
print(dat.error_word("小明住在北京"))      # 错别字
print(dat.lack_punctuation("小明住在北京")) # 缺少标点
# 更多 11 种增强类型详见 README_DAT.md
```

## 🤖 模型训练（推荐 LLaMA-Factory）

本仓库不再内置训练代码。如需在自有领域数据上训练或继续微调中文纠错模型，推荐使用业界主流框架 [**LLaMA-Factory**](https://github.com/hiyouga/LLaMA-Factory)：

- 训练数据：直接使用我们开源的 [34万COT数据集](https://huggingface.co/datasets/twnlp/ChineseErrorCorrector4-4B)、 [200 万条监督数据](https://huggingface.co/datasets/twnlp/ChinseseErrorCorrectData)、[`twnlp/csc_data`](https://huggingface.co/datasets/twnlp/csc_data)、[拼写数据集](https://huggingface.co/datasets/twnlp/cgc_data)
- 数据增强：领域语料不足时，先用本仓库 `pip install ChineseErrorCorrector` 增强出语法/拼写错误样本，再喂给 LLaMA-Factory。
- 基座模型：若有COT数据，训练模型，优先使用`ChineseErrorCorrector4`作为基座进行训练，若有常规监督数据（例如：src,tgt），基座模型推荐使用 `ChineseErrorCorrector3`进行训练。
- 训练 Prompt：`ChineseErrorCorrector4` 参考：[34万COT数据集](https://huggingface.co/datasets/twnlp/ChineseErrorCorrector4-4B)、`ChineseErrorCorrector3` 参考： [200 万条监督数据](https://huggingface.co/datasets/twnlp/ChinseseErrorCorrectData)

训练完成后，将权重路径喂给 vLLM `vllm serve <your_model>`，在 `config.py` 把 `OPENAI_MODEL` 改成你自己的模型名即可无缝接入本仓库的推理与评测流程。

## Citation

如果本工作对您有帮助，欢迎引用：

```bibtex
@inproceedings{tian-etal-2026-csrp,
    title = "{CSRP}: Chain-of-Thought Reasoning for {C}hinese Text Correction via Reinforcement Learning with Efficiency-Aware Rewards",
    author = "Tian, Wei  and
      Zhou, Yuhao  and
      Lan, Man",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.1733/",
    pages = "37349--37365",
    ISBN = "979-8-89176-390-6",
    abstract = "Large Language Model (LLM) based Chinese Grammatical Error Correction (CGEC) systems face two critical challenges: general-purpose models lack specialized linguistic priors for subtle grammatical distinctions, and Supervised Fine-Tuning (SFT) with Maximum Likelihood Estimation fails to optimize for precision-focused metrics, leading to systematic over-correction. We propose CSRP, a three-stage framework that progressively builds correction capability through Continual Pre-training (CPT) on 5.9M balanced samples to internalize domain knowledge, Chain-of-Thought SFT with explicit error reasoning for diagnostic transparency, and Group Relative Policy Optimization with a novel Efficiency-Aware Reward that explicitly penalizes unnecessary edits. On the NACGEC benchmark, CSRP achieves state-of-the-art performance with 50.99 $F_{0.5}$ and 57.17 precision, substantially outperforming previous best results while effectively mitigating the over-correction bias inherent in MLE-trained models. Our method also advances CSCD spelling correction to 59.61 F1, surpassing GPT-4 by 5.20 points. Comprehensive ablation studies demonstrate that the RL alignment stage contributes a 8{\%} relative gain over the SFT baseline, and that this gain is orthogonal to the contribution of large-scale CPT, validating that explicit optimization for edit efficiency is essential for high-quality grammatical error correction. Our code is available at https://github.com/TW-NLP/ChineseErrorCorrector."
}
```

```bibtex
@misc{tian2025chineseerrorcorrector34bstateoftheartchinesespelling,
      title={ChineseErrorCorrector3-4B: State-of-the-Art Chinese Spelling and Grammar Corrector},
      author={Wei Tian and YuhaoZhou},
      year={2025},
      eprint={2511.17562},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.17562},
}
```

## 🤝 Contributing（贡献指南）

欢迎任何形式的贡献：报告 Issue、完善文档、补充数据、修复 Bug、提交新特性等。提交前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，了解 Issue / Pull Request 的提交规范与代码风格要求。

## 📄 License（开源协议）

本项目基于 [Apache-2.0 License](LICENSE) 开源，可自由用于学术研究与商业用途，使用时请保留版权与协议声明。

## Contact

**微信：** NLP技术交流群。

<img src="https://github.com/TW-NLP/ChineseErrorCorrector/blob/main/images/chat_630.jpg" width="200" />


## References

* [中文纠错系统](https://github.com/shibing624/pycorrector)
* [纠错论文](https://github.com/nghuyong/Chinese-text-correction-papers)
* [纠错评测](https://github.com/open-writing-evaluation/jp_errant_bea)



## GitHub Star History

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/TW-NLP/ChineseErrorCorrector?style=social)](https://github.com/TW-NLP/ChineseErrorCorrector/stargazers)

[![Star History Chart](https://star-history.dera.page/svg?repos=TW-NLP/ChineseErrorCorrector&type=Date)](https://star-history.dera.page/#TW-NLP/ChineseErrorCorrector&Date)

</div>
