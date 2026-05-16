# Novel Writer Skill

一个中文优先、场景优先的长篇小说创作 Skill。它把创作蓝图、大纲、场景规划、人物设定、章节写作、改稿、可选图片管理和 TXT 优先导出整理成一套可复用的 Agent 工作流。

## 特点

- 默认简体中文、单语写作。
- 默认 TXT 优先导出，DOCX / EPUB / PDF 仅在需要时启用。
- 图片是可选增强，不会默认进入流程。
- 写作生产顺序为 `场景 -> 章节 -> 卷 -> 全书`。
- 大纲是强参考，写作中途允许修改，但需要用户明确指令或确认。
- 支持中式轻小说、电影蒙太奇式人物世界观叙事等题材指导。
- 保留原工作流中的角色设定、语言设置、风格设置、资产映射和导出能力，并改造成通用 Skill 结构。

## 适用环境

### Codex Skill

将本仓库克隆或复制到 Codex skills 目录后即可使用：

```bash
git clone https://github.com/Yoyo-514/novel-writer-skill.git
```

在 Codex 中触发与小说创作、改稿、导出相关的任务时，读取 `SKILL.md` 作为入口。

### 通用 Agent / 其他 AI 工具

这套内容不依赖 Codex 专属语法。其他 Agent 可以这样使用：

1. 读取 `SKILL.md` 作为主工作流说明。
2. 按任务需要读取 `references/` 下的专题文件。
3. 需要导出时调用 `scripts/assemble_novel.py`。
4. 需要从 PDF 提取图片时调用 `scripts/extract_pdf_images.py`，图片流程默认可选。

## 目录结构

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── CHAPTER_TEMPLATE.md
│   ├── LANGUAGE_SETTING.json
│   ├── STYLE_SETTING.json
│   └── custom_style_guide_western_fantasy.md
├── references/
│   ├── workflow.md
│   ├── conception-blueprint.md
│   ├── outline-planning.md
│   ├── chapter-outline.md
│   ├── scene-chapter-writing.md
│   ├── chapter-prose-execution.md
│   ├── chapter-revision.md
│   ├── character-design.md
│   ├── novel-style.md
│   ├── style-language.md
│   ├── topic-guidance.md
│   ├── asset-map.md
│   └── export.md
└── scripts/
    ├── assemble_novel.py
    └── extract_pdf_images.py
```

## 基本用法

典型流程：

1. 从创意或现有资料创建 `CREATIVE_BLUEPRINT.md`。
2. 创建整体大纲和近期卷纲。
3. 将卷纲拆成场景卡，再组合成章节。
4. 先写场景，再汇总章节、卷、全书。
5. 默认导出 TXT。

导出示例：

```bash
python scripts/assemble_novel.py --project novel --lang zh --txt
```

导出脚本会按 `场景 -> 章节 -> 卷 -> 全书` 汇总，并在覆盖已有生成文件前创建时间戳备份。

## 推荐项目结构

Skill 会建议小说项目使用以下结构：

```text
novel/
  CREATIVE_BLUEPRINT.md
  OUTLINE.md
  CHAPTER_OUTLINE.md
  NOVEL_STATE.json
  MANIFEST.md
  characters/
    CHARACTER_BIBLE.md
  settings/
    LANGUAGE_SETTING.json
    STYLE_SETTING.json
    CHAPTER_TEMPLATE.md
    SCENE_PLAN.md
    TIMELINE.md
    TRANSLATION_GLOSSARY.md
  draft/
    zh/
      vol01/
        ch01/
          scene01.md
          scene02.md
        ch01_zh.md
      vol01_zh.md
    FULL_NOVEL_zh.md
  output/
    novel_zh.txt
```

## 验证

基础仓库检查：

```bash
python scripts/validate_skill.py
python -B scripts/assemble_novel.py --help
```

如果你在 Codex 环境中有 `skill-creator` 校验脚本，也可以运行：

```bash
python path/to/quick_validate.py .
```

## 许可证

[MIT License](./LICENSE) © Yoyo514
