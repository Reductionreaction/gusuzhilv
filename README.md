## 项目概述:

姑苏智旅项目的目标是利用经过微调的**chinese-alphaca-pro-7b**模型，为用户提供涵盖苏州旅游、文化等方面的智能化服务。该项目采用了先进的预训练模型和微调框架，结合多个数据来源，通过网页搭建和设备配置，为用户提供了便捷的交互方式和全面的信息服务。

## 关键步骤:

1. **预训练模型来源:** 项目使用基于[llama-alpaca-7b]([meta-llama/Llama-2-7b-chat-hf · Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf))的预训练模型，并对其进行微调以更好地适应苏州文旅领域的需求。
2. **模型微调框架:** 使用灵活高效的firefly框架进行模型微调，以提升模型性能和适用性。
3. **数据来源:** 项目整合了多个数据来源，包括百度百科、马蜂窝、苏州本地宝、去哪儿等旅游平台，以及人工处理和ChatGPT3.5与4.0等渠道，确保信息的全面和准确。
4. **网页搭建:** 采用gradio+frp内网穿透技术实现了网页的搭建和公网访问，为用户提供了便捷的访问途径。
5. **设备配置:** 使用了2个a6000设备，保障了项目的稳定性和性能表现。
6. **二轮数据整理:** 在项目进行过程中进行了二轮数据整理，以确保数据的质量和准确性，为模型的训练和应用提供可靠基础。
7. **其他尝试:** 在项目中还尝试了**langchain**等技术，丰富了项目的技术栈和实践经验。

## 项目成果:

- 模型支持二轮对话。
- 提供webui和链接，公网访问链接为[姑苏智旅](http://47.120.72.255:24001/)
- 我们只上传了训练好的lora模型，请自行与预训练模型合并(合并脚本也可以参考firefly大佬们的merge.py,~为大佬们疯狂摇旗呐喊~)，[lora下载链接](https://pan.quark.cn/s/2ecf56a0174d)
- 爬虫部分可能会出现奇怪的结果，需自行分辨取用

PS: 链接可能会在一段时间后关闭，打开链接时请勿使用vpn，可能会导致错误

## 其他

如果在使用过程中遇到任何问题或异常情况，请随时联系我们，我们将尽力解决并改进。

联系方式：oxidationreaction@163.com，cjw6868595@163.com 

### TO DO

- langchain只是一个demo，只能在终端进行输入与输出，webui待实现，待更新
- 数据集待扩充(暂不公开)...

## 参考文献和致谢

**感谢以下项目提供的帮助:**

- [ymcui/Chinese-LLaMA-Alpaca: 中文LLaMA&Alpaca大语言模型+本地CPU/GPU训练部署 (Chinese LLaMA & Alpaca LLMs)](https://github.com/ymcui/Chinese-LLaMA-Alpaca)
- [yangjianxin1/Firefly: Firefly)](https://github.com/yangjianxin1/Firefly)

