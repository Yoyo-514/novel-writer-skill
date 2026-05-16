# Contributing

欢迎提交 issue 或 pull request。

## 内容原则

- 保持 `SKILL.md` 简洁，细节放入 `references/`。
- 新增超过 100 行的 reference 文件时，请添加 `## Contents`。
- 默认简体中文、单语写作、TXT 优先导出。
- 保持 `场景 -> 章节 -> 卷 -> 全书` 的生产顺序。
- 不要把某一平台的专用命令格式写入通用 reference。
- 不要照抄外部工作流或角色提示词；提炼成可复用规则。

## 代码原则

- 脚本使用 Python 标准库优先。
- 写文件前尽量避免静默覆盖用户内容。
- 生成内容、缓存、测试小说项目不要提交到仓库。

## 发布前检查

```bash
python scripts/validate_skill.py
python path/to/quick_validate.py .
python -B scripts/assemble_novel.py --help
```
